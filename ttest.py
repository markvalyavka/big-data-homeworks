import datetime
from random import randrange
from datetime import timedelta

def random_1mo_ago_date(delta=timedelta(days=31)):
    """
    This function will return a random datetime between
    [now() - 31days, now()]
    """
    date_31d_ago = datetime.datetime.now() - delta
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return date_31d_ago + timedelta(seconds=random_second)


print(random_1mo_ago_date())