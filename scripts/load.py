
import os

from sqlalchemy import create_engine
from dotenv import load_dotenv


def get_engine():

    load_dotenv()

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    connection_string = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    return create_engine(connection_string)


def load_data(df, engine):

    table_name = "clean_tokopedia_reviews"

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False,
        chunksize=1000
    )

    print("\nLOAD BERHASIL")
    print("Jumlah data:", len(df))
    print("Nama tabel:", table_name)
    print("Database: tokopedia_dw")
