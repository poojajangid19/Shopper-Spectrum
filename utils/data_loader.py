from pathlib import Path
import pandas as pd

def load_data():

    file_path = Path(__file__).parent.parent / "data" / "onlineretail.csv"

    df = pd.read_csv(file_path, encoding="latin1")

    return df