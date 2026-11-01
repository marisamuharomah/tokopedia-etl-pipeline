
import pandas as pd

def extract_data():

    file_path = "data/raw/tokopedia-product-reviews-2019.csv"
    df = pd.read_csv(file_path)
    print(df.head())

    print("\nINFORMASI DATASET")
    print("Ukuran dataset:", df.shape)
    print("Nama kolom:")
    print(df.columns.tolist())

    df.info()

# Informasi tambahan dataset
    print("Missing Values:", df.isnull().sum())
    print("Jumlah duplikat:", df.duplicated().sum())
    print("Rating Statistics:", df["rating"].describe())
    print("Rating Distribution:", df["rating"].value_counts().sort_index())
    print("Sample Sold Values:", df["sold"].dropna().unique()[:20])

    return df
