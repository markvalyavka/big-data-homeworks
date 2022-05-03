"""Helpers for /products route."""


from backend.cassandra import cs


MOST_REVIEWED_PRODUCTS_OVER_TIME_PERIOD_STMT = """
    SELECT product_id, count(*) FROM reviews_by_product_id_and_review_date 
    WHERE review_date > %s AND review_date < %s 
    GROUP BY product_id ALLOW FILTERING;
"""


def get_products(by_filters, limit=None):

    get_products_func_by_filter = {
        frozenset(["date"]): get_most_reviewed_over_period
    }

    filter_ = frozenset(by_filters.keys())
    products = get_products_func_by_filter[filter_](by_filters, limit)

    return products


def get_most_reviewed_over_period(by_filters, limit=None):

    date_from, date_to = by_filters["date"]["from"], by_filters["date"]["to"]

    products = cs.session.execute(
        MOST_REVIEWED_PRODUCTS_OVER_TIME_PERIOD_STMT,
        [date_from, date_to]
    ).all()

    products_sorted = sorted(products, key=lambda row: row[1], reverse=True)
    if limit:
        products_sorted = products_sorted[:limit]
    return [{
        "productId": product_id,
        "reviewCount": review_cnt
    } for product_id, review_cnt in products_sorted]
