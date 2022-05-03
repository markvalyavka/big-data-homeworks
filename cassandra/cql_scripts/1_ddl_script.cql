-- noinspection SqlNoDataSourceInspectionForFile

// FYI:
// 1. Ігнорував логіку в даних з амазону: наприклад деякі колонки можна було б додати
//    в PRIMARY KEY, бо вони б не мали дублюватись


// Create keyspace
CREATE KEYSPACE hw4_valyavka WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };


// For queries 1,2
CREATE TABLE hw4_valyavka.reviews_by_product_id_and_star_rating (
   marketplace text, 
   customer_id bigint, 
   review_id text,
   product_id text,
   product_parent text,
   product_title text,
   product_category text,
   star_rating int,
   helpful_votes int,
   total_votes int,
   vine boolean,
   verified_purchase boolean,
   review_headline text,
   review_body text,
   review_date date,
   PRIMARY KEY ((product_id), star_rating))
WITH CLUSTERING ORDER BY (star_rating DESC);


// For query 3
CREATE TABLE hw4_valyavka.reviews_by_customer_id (
   marketplace text,
   customer_id bigint,
   review_id text,
   product_id text,
   product_parent text,
   product_title text,
   product_category text,
   star_rating int,
   helpful_votes int,
   total_votes int,
   vine boolean,
   verified_purchase boolean,
   review_headline text,
   review_body text,
   review_date date,
   PRIMARY KEY (customer_id));


// For query 4
CREATE TABLE hw4_valyavka.reviews_by_product_id_and_review_date (
   marketplace text, 
   customer_id bigint, 
   review_id text,
   product_id text,
   product_parent text,
   product_title text,
   product_category text,
   star_rating int,
   helpful_votes int,
   total_votes int,
   vine boolean,
   verified_purchase boolean,
   review_headline text,
   review_body text,
   review_date date,
   PRIMARY KEY ((product_id), review_date))
WITH CLUSTERING ORDER BY (review_date DESC);


// For query 5
CREATE TABLE hw4_valyavka.reviews_by_customer_id_and_date_and_verif (
   marketplace text,
   customer_id bigint,
   review_id text,
   product_id text,
   product_parent text,
   product_title text,
   product_category text,
   star_rating int,
   helpful_votes int,
   total_votes int,
   vine boolean,
   verified_purchase boolean,
   review_headline text,
   review_body text,
   review_date date,
   PRIMARY KEY ((customer_id), review_date, verified_purchase))
WITH CLUSTERING ORDER BY (review_date DESC, review_date DESC, verified_purchase DESC);


// For query 6, 7
CREATE TABLE hw4_valyavka.reviews_by_customer_id_and_date_and_stars (
   marketplace text,
   customer_id bigint,
   review_id text,
   product_id text,
   product_parent text,
   product_title text,
   product_category text,
   star_rating int,
   helpful_votes int,
   total_votes int,
   vine boolean,
   verified_purchase boolean,
   review_headline text,
   review_body text,
   review_date date,
   PRIMARY KEY ((customer_id), review_date, star_rating))
WITH CLUSTERING ORDER BY (review_date DESC, review_date DESC, star_rating DESC);
