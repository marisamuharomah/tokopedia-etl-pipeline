
from sqlalchemy import text


def build_star_schema(engine):

    with engine.begin() as conn:

        conn.execute(text("DROP TABLE IF EXISTS fact_reviews"))
        conn.execute(text("DROP TABLE IF EXISTS dim_product"))
        conn.execute(text("DROP TABLE IF EXISTS dim_shop"))

        conn.execute(text("""
            CREATE TABLE dim_product (
                product_key SERIAL PRIMARY KEY,
                product_id BIGINT UNIQUE,
                product_name TEXT,
                category TEXT,
                product_url TEXT,
                sold BIGINT
            )
        """))

        conn.execute(text("""
            CREATE TABLE dim_shop (
                shop_key SERIAL PRIMARY KEY,
                shop_id BIGINT UNIQUE
            )
        """))

        conn.execute(text("""
            CREATE TABLE fact_reviews (
                review_key SERIAL PRIMARY KEY,
                product_key INT REFERENCES dim_product(product_key),
                shop_key INT REFERENCES dim_shop(shop_key),
                rating INT,
                review_text TEXT,
                review_count INT DEFAULT 1
            )
        """))

        conn.execute(text("""
            INSERT INTO dim_product (
                product_id,
                product_name,
                category,
                product_url,
                sold
            )
            SELECT
                product_id,
                MAX(product_name),
                MAX(category),
                MAX(product_url),
                MAX(sold)
            FROM clean_tokopedia_reviews
            GROUP BY product_id
        """))

        conn.execute(text("""
            INSERT INTO dim_shop (shop_id)
            SELECT DISTINCT shop_id
            FROM clean_tokopedia_reviews
            WHERE shop_id IS NOT NULL
        """))

        conn.execute(text("""
            INSERT INTO fact_reviews (
                product_key,
                shop_key,
                rating,
                review_text,
                review_count
            )
            SELECT
                dp.product_key,
                ds.shop_key,
                cr.rating,
                cr.text,
                1
            FROM clean_tokopedia_reviews AS cr
            JOIN dim_product AS dp
                ON cr.product_id = dp.product_id
            JOIN dim_shop AS ds
                ON cr.shop_id = ds.shop_id
        """))

    print("\nSTAR SCHEMA BERHASIL DIBANGUN")
