import random

from Projects.contacts.queries import get_user_code


def get_verification_code(email: str):
    code = random.randint(1000, 9999)
    if get_user_code(email=email, code=code):
        return get_verification_code(email=email)
    return code
