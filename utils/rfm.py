import pandas as pd

def create_rfm(df):

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Create Sales column
    df["Sales"] = df["Quantity"] * df["UnitPrice"]

    # Reference date
    snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    rfm = df.groupby("CustomerID").agg({
        "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
        "InvoiceNo": "nunique",
        "Sales": "sum"
    })

    rfm.columns = [
        "Recency",
        "Frequency",
        "Monetary"
    ]

    return rfm