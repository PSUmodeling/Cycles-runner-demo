import pandas as pd
from cycles import CyclesRunner
from pathlib import Path

CYCLES = Path('./') / 'Cycles'

YEAR_START=1980
YEAR_END=2020


def main():
    control_dict = {
        'simulation_name': lambda x: x['GID'],
        'simulation_start_year': YEAR_START,
        'simulation_end_year': YEAR_END,
        'rotation_size': 1,
        'crop_file': 'Maize.crop',
        'operation_file': lambda x: f'{x["GID"]}.operation',
        'soil_file': lambda x: f'soil/{x["soil"]}',
        'weather_file': lambda x: f'weather/{x["weather"]}',
        'automatic_nitrogen': 1,
        'daily_weather_out': 1,
        'daily_crop_out': 1,
        'daily_residue_out': 1,
        'daily_water_out': 1,
        'daily_nitrogen_out': 1,
        'daily_soil_carbon_out': 1,
        'daily_soil_lyr_cn_out': 1,
    }

    operation_dict = {
        'PD1': lambda x: x['maize_plant_start'],
        'PD2': lambda x: x['maize_plant_end'],
        'SOIL_TEMP': 12.0,
        'CROP': lambda x: f'MaizeRM.{int(x["relative_maturity_group"])}',
    }

    cycles_runner = CyclesRunner(
        executable=CYCLES,
    )

    cycles_runner.run(
        simulations=pd.read_csv(Path('./simulations.csv')),
        summary='summary.csv',
        control_dict=control_dict,
        operation_template=Path('./template') / 'monoculture.operation',
        operation_dict=operation_dict,
        options='-sg',
        rm_input=False,
        silence=True,
        rm_output=False,
    )

if __name__ == '__main__':
    main()
