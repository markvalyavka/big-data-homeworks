"""Helpers for /customers route."""


from backend.cassandra import cs


CUSTOMERS_OVER_TIME_PERIOD_W_PURCHASE_VERIF_STMT = """
    SELECT customer_id, count(*) FROM reviews_by_customer_id_and_date_and_verif 
    WHERE review_date > %s AND review_date < %s AND verified_purchase = %s 
    GROUP BY customer_id ALLOW FILTERING;
"""

CUSTOMERS_OVER_TIME_PERIOD_W_HATERS_STMT = """
    SELECT customer_id, count(*) FROM reviews_by_customer_id_and_date_and_stars 
    WHERE review_date > %s AND review_date < %s AND star_rating < 3
    GROUP BY customer_id ALLOW FILTERING;
"""

CUSTOMERS_OVER_TIME_PERIOD_W_BACKERS_STMT = """
    SELECT customer_id, count(*) FROM reviews_by_customer_id_and_date_and_stars 
    WHERE review_date > %s AND review_date < %s AND star_rating > 3
    GROUP BY customer_id ALLOW FILTERING;
"""

def get_customers(by_filters, limit=None):

    get_customers_func_by_filter = {
        frozenset(["date", "purchaseVerified"]): get_customers_over_period_w_purchase_verified,
        frozenset(["date", "isHater"]): get_customers_over_period_w_star_rating,
    }

    filter_ = frozenset(by_filters.keys())
    customers = get_customers_func_by_filter[filter_](by_filters, limit)

    return customers


def get_customers_over_period_w_purchase_verified(by_filters, limit=None):

    date_from, date_to = by_filters["date"]["from"], by_filters["date"]["to"]
    purchase_verified = by_filters.get("purchaseVerified")

    customers = cs.session.execute(
        CUSTOMERS_OVER_TIME_PERIOD_W_PURCHASE_VERIF_STMT,
        [date_from, date_to, purchase_verified]
    ).all()

    customers_sorted = sorted(customers, key=lambda row: row[1], reverse=True)
    if limit:
        customers_sorted = customers_sorted[:limit]
    return [{
        "customerId": customer_id,
        "reviewCount": review_cnt
    } for customer_id, review_cnt in customers_sorted]


def get_customers_over_period_w_star_rating(by_filters, limit=None):

    date_from, date_to = by_filters["date"]["from"], by_filters["date"]["to"]
    is_hater = by_filters.get("isHater")

    query = CUSTOMERS_OVER_TIME_PERIOD_W_BACKERS_STMT
    if is_hater:
        query = CUSTOMERS_OVER_TIME_PERIOD_W_HATERS_STMT

    customers = cs.session.execute(
        query, [date_from, date_to]
    ).all()

    customers_sorted = sorted(customers, key=lambda row: row[1], reverse=True)
    if limit:
        customers_sorted = customers_sorted[:limit]
    return [{
        "customerId": customer_id,
        "reviewCount": review_cnt
    } for customer_id, review_cnt in customers_sorted]
