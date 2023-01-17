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

    df['room_type'].value_counts().plot(kind='bar')

    plt.show()
