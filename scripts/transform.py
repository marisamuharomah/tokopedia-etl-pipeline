
import pandas as pd


def transform_data(df):

    print("\nDATA SEBELUM TRANSFORM")
    print("Jumlah baris:", len(df))

    text_columns = ["text", "category", "product_name", "product_url"]

    for column in text_columns:
        df[column] = df[column].str.strip()

    def clean_sold(value):
        if pd.isna(value):
            return pd.NA

        value = str(value).strip().lower()

        if value == "":
            return pd.NA

        if value.endswith("rb"):
            try:
                number = value.replace("rb", "").replace(",", ".")
                return int(float(number) * 1000)
            except ValueError:
                return pd.NA

        return pd.to_numeric(value, errors="coerce")

    df["sold"] = df["sold"].apply(clean_sold).astype("Int64")

    invalid_rating = ~df["rating"].between(1, 5)

    print("\nVALIDASI DATA")
    print("Rating tidak valid:", invalid_rating.sum())
    print("Rating kosong:", df["rating"].isna().sum())
    print("Duplikat:", df.duplicated().sum())

    output_path = "data/processed/tokopedia_clean.csv"
    df.to_csv(output_path, index=False)

    print("\nHASIL TRANSFORM")
    print("Jumlah baris:", len(df))
    print("Sold terisi:", df["sold"].notna().sum())
    print("Sold kosong:", df["sold"].isna().sum())
    print("Tipe data sold:", df["sold"].dtype)
    print("File tersimpan:", output_path)

    return df
