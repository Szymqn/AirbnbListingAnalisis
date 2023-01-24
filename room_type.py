from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def load_room_type():
    HERE = Path(__file__).parent
    DATA_FOLDER = HERE / "data"

    df = pd.read_csv(
        DATA_FOLDER / "listings.csv",
        converters={'room_type': str.lower},
        usecols=['room_type'],
    )

    analyze(source=df)

    
def analyze(source):
    data = source.value_counts()

    data_dict = data.to_dict()

    keys = list(map(str, data_dict.keys()))
    keys = [key[2:-3] for key in keys]  # remove brackets and comma

    fig, ax = plt.subplots()

    ax.set_title('Room types')

    values = data / data.sum() * 100
    ax.bar(keys, data_dict.values())

    for i, v in enumerate(values):
        plt.text(i - 0.2, v+50, str(round(v, 2)) + "%", color='black', fontweight='bold')

    plt.show()
