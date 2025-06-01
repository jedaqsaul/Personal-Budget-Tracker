from lib.models import User, Category
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
        
        result = {
            "name": user.name,
            "monthly_budget": user.monthly_budget,
            "currency": user.currency
        }
        session.close()
        return result
    session.close()
    return None


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

def get_all_users():
    session=Session()
    users=session.query(User).all()
    session.close()
    return users


def get_all_categories():
    session=Session()
    categories=session.query(Category).all()
    session.close()
    return categories


def add_category(name):
    session=Session()
    category=Category(name=name)
    session.add(category)
    session.commit()
    session.close()
    return category

    



