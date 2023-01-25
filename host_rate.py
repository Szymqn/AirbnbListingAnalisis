from pathlib import Path
import pandas as pd


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
    values = list(data_dict.values())

    keys = list(map(str, data_dict.keys()))
    keys = [key[2:-3] for key in keys]

    ranges = [('Excellent', (100, 90)),
              ('Good', (90, 80)),
              ('Average', (80, 60)),
              ('Below average', (60, 40)),
              ('Bad', (40, 0))]

    num_of_each = {'Excellent': 0, 'Good': 0, 'Average': 0, 'Below average': 0, 'Bad': 0}

    status = []

    idx = 0
    for key in keys:
        match key:
            case 'N/A':
                status.append('N/A')
            case _:
                for label, (low, high) in ranges:
                    if high <= int(key[:-1]) <= low:
                        status.append(label)
                        num_of_each[label] = num_of_each.get(label, 0) + values[idx]
                        idx += 1
                        break

    print(num_of_each)
