from pathlib import Path
import pandas as pd


def load_review_score():
    HERE = Path(__file__).parent
    DATA_FOLDER = HERE / "data"

    df = pd.read_csv(
        DATA_FOLDER / "listings.csv",
        usecols=['review_scores_rating',
                 'review_scores_accuracy',
                 'review_scores_cleanliness',
                 'review_scores_checkin',
                 'review_scores_communication',
                 'review_scores_location',
                 'review_scores_value'],
    )

    analyze_float(source=df)


def analyze_float(source):
    data = source.value_counts()
    labels = data.keys().names

    avg = []

    for col in labels:
        avg.append(source[col].mean())
