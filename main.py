
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import get_engine, load_data
from scripts.star_schema import build_star_schema


def main():

    print("TOKOPEDIA ETL PIPELINE")

    df = extract_data()
    df_clean = transform_data(df)

    engine = get_engine()

    try:
        load_data(df_clean, engine)
        build_star_schema(engine)

    finally:
        engine.dispose()

    print("\nETL PIPELINE BERHASIL")


if __name__ == "__main__":
    main()
