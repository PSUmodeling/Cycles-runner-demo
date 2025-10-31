# Cycles-runner-demo

A demo of using the [`Cycles-utils` Python package](https://pypi.org/project/Cycles-utils/) `CyclesRunner` module to run Cycles simulations on the Penn State Roar cluster.
This repository contains a `Cycles v1.5.1` executable, and requires `Cycles-utils v3.0.0`.

## Update or install `Cycles-utils` 

To run the demo, first check that the latest version of `Cycles-utils` is installed.
Activate your Python environment using either
```shell
module load python/3.11.2
```
or, if you are using `conda` 
```shell
source activate my_env
```
to activate your Python environment. Replace `3.11.2` and `my_env` with your Python version number or environment name.

If you have not installed `Cycles-utils` before, run
```shell
python3 -m pip install cycles-utils
```
If errors occur due to missing packages, install the specific packages using the same `python3 -m pip install` command.

If `Cycles-utils` is already installed, run
```shell
python3 -m pip install --upgrade cycles-utils
```
to update it to the latest version.

## Run the demo
You can either do
```shell
./submit_cycles.job
```
to run the demo interactively, or submit the job by doing
```shell
sbatch ./submit_cycles.job
```
Note that you will need to edit the `submit_cycles.job` to put in your own email address.
You can also change the number of nodes requested (`nodes`), number of cores (`ntasks`), maximum wall time (`time`), and minimum memory required per CPU (`mem-per-cpu`)
