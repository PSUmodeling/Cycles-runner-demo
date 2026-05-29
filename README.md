# Cycles-runner-demo

A demo of using the [`Cycles-utils` Python package](https://pypi.org/project/Cycles-utils/) `CyclesRunner` module to run Cycles simulations on the Penn State Roar cluster.
This repository contains a `Cycles v1.5.20` executable, and requires `Cycles-utils v4.0.2`.
You can refer to the [Cycles User Reference Guide Cycles on Roar section](https://psumodeling.github.io/Cycles/roar/) for instructions on how to install the `Cycles-utils` package on Roar.

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
You can also change the number of nodes requested (`nodes`), number of cores (`ntasks`), maximum wall time (`time`), and minimum memory required per CPU (`mem-per-cpu`).
