from pathlib import Path
import matplotlib.pyplot as plt
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

    df_p = pd.read_csv(
        DATA_FOLDER / "listings.csv",
        converters={'id': int},
        usecols=['id',
                 'review_scores_rating',
                 'review_scores_accuracy',
                 'review_scores_cleanliness',
                 'review_scores_checkin',
                 'review_scores_communication',
                 'review_scores_location',
                 'review_scores_value'],
    )

    analyze_overview(source=df)

    analyze_place(source=df_p, place_id=42932)


def analyze_overview(source):
    data = source.value_counts()
    labels = data.keys().names

    avg = []

    for col in labels:
        avg.append(source[col].mean())

    labels = [label.replace('review_scores_', ' ') for label in labels]

    fig, ax = plt.subplots()

    ax.set_title('Reviews overview')
    ax.bar(labels, avg)

    for i, v in enumerate(avg):
        plt.text(i-0.2, v, str(round(v, 2)) + "*", color='black')

    plt.xticks(rotation=11, fontsize=8)
    plt.show()


def analyze_place(source, place_id):
    data_values = source.query(f'id == {place_id}')

    keys = list(data_values.keys().delete(0))

    keys = [key.replace('review_scores_', '') for key in keys]

    values = data_values.value_counts()
    values = values.to_dict()
    values = list(*values.keys())
    values.pop(0)

    fig, ax = plt.subplots()

    ax.set_title(f'Reviews of {place_id} place id')
    ax.bar(keys, values)

    for i, v in enumerate(values):
        plt.text(i - 0.2, v, str(round(v, 2)) + "*", color='black')

    plt.xticks(rotation=11, fontsize=8)
    plt.show()
