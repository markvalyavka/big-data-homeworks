


// Query 1 
// Отримувати всі відгуки за заданим product_id

SELECT * FROM reviews_by_product_id WHERE product_id = *value*


// Query 2
// Отримувати всі відгуки за заданим product_id та обраним star_rating

SELECT * FROM reviews_by_product_id WHERE product_id = *value* and star_rating = *value*


// Query 3
// Отримувати всі відгуки за заданим customer_id

SELECT * FROM reviews_by_customer_id WHERE customer_id = *value*


// Query 4
// Отримувати користувачів(customer_id), які залишили більше ніж N відгуків на платформі і 
// які також залишили відгук для продукту product_id (N та product_id повинне задаватися в 
// запиті)

SELECT customer_id FROM reviews_by_product_id 
WHERE product_id = *value* GROUP BY customer_id HAVING count(*) > *N_value*


// Query 5
// Дізнатися скільки позитивних відгуків (4 або 5 зірок) залишив вказаний користувач customer_id

SELECT * FROM reviews_by_customer_id WHERE customer_id = *value* and star_rating > 3

