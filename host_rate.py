import pandas as pd
from pathlib import Path


def load_host_rate():
    HERE = Path(__file__).parent
    DATA_FOLDER = HERE / "data"

    df = pd.read_csv(
        DATA_FOLDER / "listings.csv",
        converters={'host_response_time': str},
        usecols=['host_response_time'],
    )

    analyze(source=df)


def analyze(source):
    pass
