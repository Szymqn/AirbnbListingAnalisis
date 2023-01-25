from pathlib import Path
import pandas as pd
from functools import reduce


def load_host_rate():
    HERE = Path(__file__).parent
    DATA_FOLDER = HERE / "data"

    df = pd.read_csv(
        DATA_FOLDER / "listings.csv",
        converters={'host_acceptance_rate': str},
        usecols=['host_acceptance_rate'],
    )

    analyze(source=df)


def analyze(source):
    data = source.value_counts()

    data_dict = data.to_dict()

    keys = list(map(str, data_dict.keys()))
    keys = [key[2:-3] for key in keys]

    ranges = [('Excellent', (100, 90)),
              ('Good', (90, 80)),
              ('Average', (80, 60)),
              ('Below average', (60, 40)),
              ('Bad', (40, 0))]

    status = []

    for key in keys:
        match key:
            case 'N/A':
                status.append('N/A')
            case _:
                for label, (low, high) in ranges:
                    if high <= int(key[:-1]) <= low:
                        status.append(label)
                        break

    list_of_dicts = [{k: v} for k, v in zip(status, data_dict.values())]

    merged_dict = {}
    for idx, d in enumerate(list_of_dicts):
        for key, value in d.items():
            if key in merged_dict:
                key = key + f"_{idx}"
            merged_dict[key] = value

    print(merged_dict)
