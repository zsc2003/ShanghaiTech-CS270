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
p1, p2, p3, p4
```

subproblem numbers are
```bash
p1a, p1b, p2a, p3a, p4a, p4b
```

Specifically, in order to use the `psf2otf` function, the `p4/p4c` is apply in matlab.

To run the code, use the following command in matlab in folder `$PATH_TO_FOLDER_WITH_README/p4`:
```bash
p4c
```
