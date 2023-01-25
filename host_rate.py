from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def load_host_rate():
    HERE = Path(__file__).parent
    DATA_FOLDER = HERE / "data"

    acceptance = pd.read_csv(
        DATA_FOLDER / "listings.csv",
        converters={'host_acceptance_rate': str},
        usecols=['host_acceptance_rate'],
    )

    analyze(source=acceptance, title='Host acceptance rate')

    response = pd.read_csv(
        DATA_FOLDER / "listings.csv",
        converters={'host_response_rate': str},
        usecols=['host_response_rate'],
    )

    analyze(source=response, title='Host response rate')


def analyze(source, title):
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

    num_of_each = {'Excellent': 0, 'Good': 0, 'Average': 0, 'Below average': 0, 'Bad': 0, 'N/A': 0}

    status = []

    idx = 0
    for key in keys:
        match key:
            case 'N/A':
                status.append('N/A')
                num_of_each['N/A'] = num_of_each.get('N/A', 0) + values[idx]
            case _:
                for label, (low, high) in ranges:
                    if high <= int(key[:-1]) <= low:
                        status.append(label)
                        num_of_each[label] = num_of_each.get(label, 0) + values[idx]
                        idx += 1
                        break

    labels = num_of_each.keys()
    sizes = num_of_each.values()
    max_value = np.argmax(sizes)

    explode = [0 for _ in range(len(sizes))]
    explode[max_value] = 0.1

    fig, ax = plt.subplots()
    ax.set_title(title, fontweight='bold')
    ax.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', pctdistance=0.5, shadow=True)
    ax.axis('equal')

    plt.show()
