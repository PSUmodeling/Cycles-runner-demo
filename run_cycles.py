import pandas as pd
from cycles import CyclesRunner

CYCLES = './Cycles'

YEAR_START=1980
YEAR_END=2020


def main():
    simulation_name = lambda x: x['GID']

    control_dict = lambda x: {
        'simulation_start_date': YEAR_START,
        'simulation_end_date': YEAR_END,
        'rotation_size': 1,
        'crop_file': 'Maize.crop',
        'operation_file': f'{simulation_name(x)}.operation',
        'soil_file': f'soil/{x["soil"]}',
        'weather_file': f'weather/{x["weather"]}',
        'automatic_nitrogen': 1,
        'daily_weather_out': 1,
        'daily_crop_out': 1,
        'daily_residue_out': 1,
        'daily_water_out': 1,
        'daily_nitrogen_out': 1,
        'daily_soil_carbon_out': 1,
        'daily_soil_lyr_cn_out': 1,
    }

    operation_dict = lambda x: {
        'PD1': x['maize_plant_start'],
        'PD2': x['maize_plant_end'],
        'SOIL_TEMP': 12.0,
        'CROP': f'MaizeRM.{int(x["relative_maturity_group"])}',
    }

    cycles_runner = CyclesRunner(
        simulations=pd.read_csv('./simulations.csv'),
        summary='summary.csv',
        simulation_name=simulation_name,
        control_dict=control_dict,
        operation_template=f'./template/monoculture.operation',
        operation_dict=operation_dict,
    )

    cycles_runner.run(
        CYCLES,
        options='-sg',
        rm_input=False,
        silence=True,
        rm_output=False,
    )

if __name__ == '__main__':
    main()
