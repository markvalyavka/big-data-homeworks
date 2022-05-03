
-- Populate all tables

COPY hw4_valyavka.reviews_by_product_id_and_star_rating(
    marketplace,
    customer_id,
    review_id,
    product_id,
    product_parent,
    product_title,
    product_category,
    star_rating,
    helpful_votes,
    total_votes,
    vine,
    verified_purchase,
    review_headline,
    review_body,
    review_date)
FROM '/init_data/amazon_reviews_100k.tsv' WITH DELIMITER='\t' AND CHUNKSIZE=10 AND MAXBATCHSIZE=100;


COPY hw4_valyavka.reviews_by_customer_id(
    marketplace,
    customer_id,
    review_id,
    product_id,
    product_parent,
    product_title,
    product_category,
    star_rating,
    helpful_votes,
    total_votes,
    vine,
    verified_purchase,
    review_headline,
    review_body,
    review_date)
FROM '/init_data/amazon_reviews_100k.tsv' WITH DELIMITER='\t' AND CHUNKSIZE=10 AND MAXBATCHSIZE=100;


COPY hw4_valyavka.reviews_by_product_id_and_review_date(
    marketplace,
    customer_id,
    review_id,
    product_id,
    product_parent,
    product_title,
    product_category,
    star_rating,
    helpful_votes,
    total_votes,
    vine,
    verified_purchase,
    review_headline,
    review_body,
    review_date)
FROM '/init_data/amazon_reviews_100k.tsv' WITH DELIMITER='\t' AND CHUNKSIZE=10 AND MAXBATCHSIZE=100;



COPY hw4_valyavka.reviews_by_customer_id_and_date_and_verif(
    marketplace,
    customer_id,
    review_id,
    product_id,
    product_parent,
    product_title,
    product_category,
    star_rating,
    helpful_votes,
    total_votes,
    vine,
    verified_purchase,
    review_headline,
    review_body,
    review_date)
FROM '/init_data/amazon_reviews_100k.tsv' WITH DELIMITER='\t' AND CHUNKSIZE=10 AND MAXBATCHSIZE=100;


COPY hw4_valyavka.reviews_by_customer_id_and_date_and_stars(
    marketplace,
    customer_id,
    review_id,
    product_id,
    product_parent,
    product_title,
    product_category,
    star_rating,
    helpful_votes,
    total_votes,
    vine,
    verified_purchase,
    review_headline,
    review_body,
    review_date)
FROM '/init_data/amazon_reviews_100k.tsv' WITH DELIMITER='\t' AND CHUNKSIZE=10 AND MAXBATCHSIZE=100;