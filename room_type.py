from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def load():
    HERE = Path(__file__).parent
    DATA_FOLDER = HERE / "data"

    df = pd.read_csv(
        DATA_FOLDER / "listings.csv",
        converters={'room_type': str.lower},
        usecols=['room_type'],
    )
    analize(source=df)


def analize(source):
    data = source.value_counts()

    data_dict = data.to_dict()

    fig, ax = plt.subplots()

    t_keys = data_dict.keys()
    keys = []

    for key in t_keys:
        keys.append(*key)

    values = data_dict.values()

    ax.bar(keys, values)
    ax.set_title('Room types')

    plt.show()
