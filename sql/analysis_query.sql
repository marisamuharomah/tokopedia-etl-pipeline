-- 1. 10 Produk dengan Rating Tertinggi

SELECT
    dp.product_id,
    dp.product_name,
    dp.category,
    ROUND(AVG(fr.rating), 2) AS average_rating,
    COUNT(fr.review_key) AS total_reviews
FROM fact_reviews AS fr
JOIN dim_product AS dp
    ON fr.product_key = dp.product_key
GROUP BY
    dp.product_id,
    dp.product_name,
    dp.category
HAVING COUNT(fr.review_key) >= 10
ORDER BY average_rating DESC, total_reviews DESC
LIMIT 10;


-- 2. Perbandingan Rating Produk Berdasarkan Kategori

SELECT
    dp.category,
    ROUND(AVG(fr.rating), 2) AS average_rating,
    COUNT(fr.review_key) AS total_reviews,
    COUNT(DISTINCT dp.product_id) AS total_products
FROM fact_reviews AS fr
JOIN dim_product AS dp
    ON fr.product_key = dp.product_key
GROUP BY dp.category
ORDER BY average_rating DESC;


-- 3. 10 Produk dengan Jumlah Terjual Tertinggi

SELECT
    dp.product_name,
    dp.category,
    dp.sold
FROM dim_product AS dp
WHERE dp.sold IS NOT NULL
ORDER BY dp.sold DESC
LIMIT 10;


-- 4. Total Penjualan Produk Berdasarkan Kategori

SELECT
    category,
    COUNT(*) AS total_products,
    SUM(sold) AS total_sold,
    ROUND(AVG(sold), 0) AS average_sold
FROM dim_product
WHERE sold IS NOT NULL
GROUP BY category
ORDER BY total_sold DESC;