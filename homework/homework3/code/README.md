To set up the environment for running the code, follow the steps below:
```bash
conda create -n CS270 python=3.10
conda activate CS270
pip install -r requirements.txt
```

To run the code, use the following command:
```bash
cd ./$PATH_TO_FOLDER_WITH_README
python ./$problem_number/$subproblem_number.py
```

Where problem numbers are
```bash
p2, p3
```

subproblem numbers are
```bash
p2a, p2b, p3
```

Specifically, in order to load the `sinogram.mat` file, the `p1/p1` is apply in matlab.

To run the code, use the following command in matlab in folder `$PATH_TO_FOLDER_WITH_README/p1`:
```bash
p1
```
