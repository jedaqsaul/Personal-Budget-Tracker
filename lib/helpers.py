from lib.db.models import User
from lib.config.setup import Session

session=Session()

def add_user(name, email, password, monthly_budget, currency):

    user= User(
        name=name,
        email=email,
        password=password,
        monthly_budget=monthly_budget,
        currency=currency
    )

    session.add(user)
    session.commit()
    return user

