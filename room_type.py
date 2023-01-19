from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


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
    keys = []

    data_dict = data.to_dict()
    t_keys = data_dict.keys()

    # Convert and add keys to list of keys
    for key in t_keys:
        keys.append(*key)

    values = data_dict.values()

    fig, ax = plt.subplots()

    ax.bar(keys, values)
    ax.set_title('Room types')

    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=max(values)))

    plt.show()
