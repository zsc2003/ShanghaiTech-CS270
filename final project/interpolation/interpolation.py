import os
from scipy.interpolate import Rbf
import scipy.io
import numpy as np
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
import math
import torch
import random
device = torch.device("cuda")

lam = 0.0
tau = 0

def rbf_basis(r, tau = None):
    epsilon = 316.364822
    # res = torch.exp(-epsilon * r ** 2)
    res = torch.sqrt(1 + (epsilon * r) ** 2).cuda()    # MQ
    return res

def rbf_basis_IMQ(r, tau = None):
    epsilon = 316.364822
    # res = torch.exp(-epsilon * r ** 2)
    res = 1 / torch.sqrt(1 + (epsilon * r) ** 2).cuda()    # IMQ
    return res

def rbf_basis_GA(r, tau = None):
    epsilon = 316.364822
    res = torch.exp(-epsilon * r ** 2).cuda()
    return res

def construct_coords(x, t, tau, lam):
    print("========= coords constructing ========")
    x_coords = np.repeat(np.arange(x), t)
    t_coords = np.tile(np.arange(t), x)
    x_coords = x_coords / x
    t_coords = t_coords / t
    coords = torch.tensor(np.stack((x_coords, t_coords), axis=1), dtype=torch.float32)
    print("========= coords constructed ========")
    return coords

def compute_phi(x, t, coords):
    r = coords.unsqueeze(0) - coords.unsqueeze(1)
    r = torch.norm(r, dim=2)

    phi = rbf_basis(r, tau)
    phi = torch.tensor(phi).type(torch.float32)
    # phi += lam * torch.eye(phi.size(0))
    print(f"=========== Calculating phi det: {torch.linalg.det(phi)} =============")
    # exit()

    phi_inv = torch.linalg.inv(phi).cuda()
    return phi, phi_inv

def rbf_interpolation(data_real, data_imag, downsample_framerate, final_framerate, phi, phi_inv, H):

    DS = final_framerate / downsample_framerate
    num_frames = data_real.shape[1]
    new_num_frames = int(num_frames * DS)

    F_real = torch.tensor(data_real.reshape(-1)).type(torch.float32).cuda()
    F_imag = torch.tensor(data_imag.reshape(-1)).type(torch.float32).cuda()

    B_real = phi_inv @ F_real
    B_imag = phi_inv @ F_imag

    F_est_real = H @ B_real
    F_est_imag = H @ B_imag

    F_est_real = F_est_real.reshape(data_real.shape[0], new_num_frames).cpu()
    F_est_imag = F_est_imag.reshape(data_imag.shape[0], new_num_frames).cpu()

    return F_est_real.numpy(), F_est_imag.numpy()


if __name__ == "__main__":
    downsample_framerate = 250
    final_framerate = 1000
    DS = int(final_framerate / downsample_framerate)

    mats_path = "PALA_data_InVivoRatBrain/IQ"
    new_mats_path = f"PALA_data_{downsample_framerate}Hz_MQ/IQ"
    os.makedirs(new_mats_path, exist_ok=True)

    tmp = int(800 / DS)
    x = 118

    # computing phi and H
    coords = construct_coords(x, tmp, tau, lam)
    phi, phi_inv = compute_phi(x, tmp, coords)
    coords_new = construct_coords(x, tmp * DS, tau, lam)
    r_new = coords.unsqueeze(0) - coords_new.unsqueeze(1)
    r_new = torch.norm(r_new, dim=2)

    H = rbf_basis(r_new, tau)
    # H += lam * torch.eye(H.size(0))
    # convert to gpu
    H = torch.tensor(H).type(torch.float32).cuda()

    for mat in sorted(os.listdir(mats_path)):
        if mat.endswith(".mat"):
            mat_path = os.path.join(mats_path, mat)
            data = scipy.io.loadmat(mat_path)
            data_IQ = np.array(data['IQ'])[:, :, ::DS]
            data_UF = np.array(data['UF'])
            data_PData = np.array(data['PData'])
            data_new_real = []
            data_new_imag = []

            # rbf with one mat
            for i in tqdm(range(data_IQ.shape[0])):
                total_frame_real = []
                total_frame_imag = []
                for frame in range(0, data_IQ.shape[2] - tmp + 1, tmp):
                    start = frame
                    end = start + tmp
                    grid_real = np.real(data_IQ[i, :, frame:end])
                    grid_imag = np.imag(data_IQ[i, :, frame:end])

                    F_est_real, F_est_imag = rbf_interpolation(grid_real, grid_imag, downsample_framerate, final_framerate, phi, phi_inv, H)
                    total_frame_real.append(F_est_real)
                    total_frame_imag.append(F_est_imag)

                total_frame_real = np.concatenate(total_frame_real, axis=1)
                total_frame_imag = np.concatenate(total_frame_imag, axis=1)

                data_new_real.append(total_frame_real)
                data_new_imag.append(total_frame_imag)
            
            data_new_real = np.array(data_new_real)
            data_new_imag = np.array(data_new_imag)
            data_new = data_new_real + 1j * data_new_imag

            scipy.io.savemat(os.path.join(new_mats_path, mat), {'IQ': data_new, 'UF': data_UF, 'PData': data_PData})
            # exit()
