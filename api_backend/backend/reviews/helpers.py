"""Helpers for /reviews route."""


from backend.cassandra import cs


REVIEWS_BY_PRODUCT_ID_STMT = """
    SELECT review_id, product_id, customer_id, star_rating FROM reviews_by_product_id_and_star_rating
    WHERE product_id = %s;
"""

REVIEWS_BY_PRODUCT_ID_AND_STAR_RATING_STMT = """
    SELECT review_id, product_id, customer_id, star_rating FROM reviews_by_product_id_and_star_rating
    WHERE product_id = %s AND star_rating = %s;
"""

REVIEWS_BY_CUSTOMER_ID_STMT = """
    SELECT review_id, product_id, customer_id, star_rating FROM reviews_by_customer_id
    WHERE customer_id = %s;
"""


def get_reviews(by_filters, limit=None):

    get_reviews_func_by_filter = {
        frozenset(["productId", "starRating"]): get_reviews_by_product_id_and_star_rating,
        frozenset(["productId"]): get_reviews_by_product_id,
        frozenset(["customerId"]): get_reviews_by_customer_id,
    }

    filter_ = frozenset(by_filters.keys())
    reviews = get_reviews_func_by_filter[filter_](by_filters)

    if limit:
        return reviews[:limit]
    return reviews


def get_reviews_by_product_id_and_star_rating(by_filters, limit=None):
    product_id = by_filters.get("productId")
    star_rating = by_filters.get("starRating")

    reviews = cs.session.execute(
        REVIEWS_BY_PRODUCT_ID_AND_STAR_RATING_STMT,
        [product_id, star_rating]
    ).all()
    if limit:
        reviews = reviews[:limit]
    return prepare_review_response(reviews)


def get_reviews_by_product_id(by_filters, limit=None):
    product_id = by_filters.get("productId")

    reviews = cs.session.execute(
        REVIEWS_BY_PRODUCT_ID_STMT, [product_id]
    ).all()
    if limit:
        reviews = reviews[:limit]
    return prepare_review_response(reviews)


def get_reviews_by_customer_id(by_filters, limit=None):
    customer_id = by_filters.get("customerId")

    reviews = cs.session.execute(
        REVIEWS_BY_CUSTOMER_ID_STMT, [customer_id]
    ).all()

    if limit:
        reviews = reviews[:limit]
    return prepare_review_response(reviews)


def prepare_review_response(reviews):

    return [{
        "reviewId": review_id,
        "productId": product_id,
        "customerId": customer_id,
        "starRating": star_rating
    } for review_id, product_id, customer_id, star_rating in reviews]
