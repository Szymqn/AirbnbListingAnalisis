from pathlib import Path
import pandas as pd
import plotly.express as px


def load():
    HERE = Path(__file__).parent
    DATA_FOLDER = HERE / "data"

    room_data = pd.read_csv(
        DATA_FOLDER / "listings.csv",
        converters={"room_type": str.lower},
        usecols=["room_type"],
    )

    prob = room_data.value_counts()
    print(prob)
