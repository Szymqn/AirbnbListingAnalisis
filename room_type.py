from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


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

    values = data_dict.values()
    keys = list(map(str, data_dict.keys()))
    keys = [key[2:-3] for key in keys]  # remove brackets and comma

    fig, ax = plt.subplots()

    ax.bar(keys, values)
    ax.set_title('Room types')

    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=max(values)))

    plt.show()
