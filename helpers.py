from lib.models import User
from config.setup import Session


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

def get_user_by_email(email):
    session=Session()
    user=session.query(User).filter(User.email == email).first()
    session.close()
    return user


def update_user_budget(user_id, new_budget):
    session = Session()
    user = session.query(User).get(user_id)
    if user:
        user.monthly_budget = new_budget
        session.commit()
    session.close()
    return user

def delete_user(user_id):
    session = Session()
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        session.close()
        return True
    session.close()
    return False

    



