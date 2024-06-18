import numpy as np
import PIL.Image as Image
import cv2

def compute_dice(pred, gt):
    # print(pred.max(), pred.min(), gt.max(), gt.min())
    intersection = np.sum(pred & gt)
    union = np.sum(pred) + np.sum(gt)
    dice = 2 * intersection / union
    
    return dice

def compute_RMSE(pred, gt):
    rmse = np.sqrt(np.mean((pred - gt) ** 2))
    return rmse

if __name__ == "__main__":
    gt_path = "/sdb/DIP/result/gt/PALA_InVivoRatBrain_example_MatOut_gt.tif"
    gt = np.array(Image.open(gt_path))
    # print(gt.max(), gt.min())
    gt_binary = cv2.cvtColor(gt, cv2.COLOR_RGB2GRAY)
    
    gt_binary[gt_binary<=1] = 0
    gt_binary[gt_binary>1] = 1
    
    RBFs = ['gt', 'GA', 'IMQ', 'MQ']
    Hzs = ['100', '250', '500']
    metrics = ['Dice', 'RMSE']
    
    for metric in metrics:
        print(f"{metric} : ")

        for rbf in RBFs:
            print(f"{rbf} : ")
            for Hz in Hzs:
                pred_path = f"/sdb/DIP/result/{rbf}/PALA_InVivoRatBrain_example_MatOut_{rbf}_{Hz}Hz.tif"
                pred = np.array(Image.open(pred_path))
                # print(pred.max(), pred.min())

                if metric == 'Dice':
                    # rbg2gray
                    pred_binary = cv2.cvtColor(pred, cv2.COLOR_RGB2GRAY)                 
                    pred_binary[pred_binary<=1] = 0
                    pred_binary[pred_binary>1] = 1
                    print(f"{Hz}Hz Dice: {compute_dice(pred_binary, gt_binary)}")

                elif metric == 'RMSE':
                    print(f"{Hz}Hz RMSE: {compute_RMSE(pred, gt)}")
    
    print("=========================")
    
    pred_path = f"/sdb/DIP/result/PALA_InVivoRatBrain_example_MatOut_GA_500Hz_ablation.tif"
    pred = np.array(Image.open(pred_path))
    pred_binary = cv2.cvtColor(pred, cv2.COLOR_RGB2GRAY)                 
    pred_binary[pred_binary<=1] = 0
    pred_binary[pred_binary>1] = 1
    print(f"{Hz}Hz Dice: {compute_dice(pred_binary, gt_binary)}")
    print(f"{Hz}Hz RMSE: {compute_RMSE(pred, gt)}")
    