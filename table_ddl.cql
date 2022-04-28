
// FYI:
// 1. Таблички старався створювати, щоб максимально уникнути data redundancy (щоб
//    можна було юзнути декілька queries в одній табличці)
// 2. Ігнорував логіку в даних з амазону: наприклад деякі колонки можна було б додати
//    в PRIMARY KEY, бо вони б не мали дублюватись


// For queries 1,2,4

CREATE TABLE hw3_valyavka.reviews_by_product_id (
   marketplace text, 
   customer_id bigint, 
   review_id UUID, 
   product_id UUID, 
   product_parent bigint,
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
   PRIMARY KEY ((product_id), star_rating, customer_id))
WITH CLUSTERING ORDER BY (star_rating DESC);


// For queries 3,5

CREATE TABLE hw3_valyavka.reviews_by_customer_id (
   marketplace text, 
   customer_id bigint, 
   review_id UUID, 
   product_id UUID, 
   product_parent bigint,
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
   PRIMARY KEY ((customer_id), star_rating))
WITH CLUSTERING ORDER BY (star_rating DESC);