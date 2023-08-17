import re

from exceptions import ValidationError


def is_valid(url):
    url_validate = r'^[a-zA-Z]+:\/\/[a-zA-Z]+\.[a-zA-Z]+\/.*$'
    if not re.match(url_validate, url):
        return False
    return True
