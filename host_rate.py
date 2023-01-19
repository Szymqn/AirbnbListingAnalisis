import pandas as pd
from pathlib import Path


def load():
    HERE = Path(__file__).parent
    DATA_FOLDER = HERE / "data"

    df = pd.read_csv(
        DATA_FOLDER / "listings.csv",
        converters={},
        usecols=[],
    )

    analyze(source=df)


def analyze(source):
    pass
