import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score


def fetch_titanic(mode="easy", train=True):
    """タイタニックデータセットの読み込みを行う関数

    Example:
        >>> (x_train, y_train), x_test = fetch_titanic(mode="easy")
        >>> # or
        >>> (x_train, y_train), x_test = fetch_titanic(mode="hard")

    Args:
        mode: titanicデータセットの難易度設定 (default: easy)
        train: if True, return (x_train, y_train), x_test
    """
    if mode == "easy":
        test_size = 0.3
    else:
        test_size = 0.98

    original = sns.load_dataset("titanic")
    data = original.drop(columns="survived")
    targets = original["survived"]

    x_train, x_test, y_train, y_test = train_test_split(
        data, targets, test_size=test_size, random_state=0, shuffle=True
    )

    if train:
        return (x_train, y_train), x_test
    else:
        return y_test


def calc_score(predicts):
    y_test = fetch_titanic(False)
    return f1_score(y_test, predicts)
