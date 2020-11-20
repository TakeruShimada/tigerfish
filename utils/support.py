import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score


def fetch_titanic(train=True):
    original = sns.load_dataset("titanic")
    data = original.drop(columns="survived")
    targets = original["survived"]

    x_train, x_test, y_train, y_test = train_test_split(
        data, targets, test_size=0.3, random_state=0, shuffle=True
    )

    if train:
        return (x_train, y_train), x_test
    else:
        return y_test


def calc_score(predicts):
    y_test = fetch_titanic(False)
    return f1_score(y_test, predicts)
