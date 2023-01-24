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

    keys = list(map(str, data_dict.keys()))
    keys = [key[2:-3] for key in keys]
    print(keys)
