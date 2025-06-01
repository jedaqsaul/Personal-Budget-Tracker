from sqlalchemy import func
from lib.models import User, Category, Transaction
from config.setup import Session
from datetime import datetime


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


def add_transaction(user_id, category_id, amount, date=None, type=None):
    session=Session()


    if date is None:
        date=datetime.now()

    if not type:
        session.close()
        raise ValueError("Transaction type is required")

    transaction=Transaction(
        user_id=user_id,
        category_id=category_id,
        amount=amount,
        date=date,
        type=type
    )

    session.add(transaction)
    session.commit()
    session.close()


    return transaction


def get_transaction_by_user(user_id):
    session=Session()
    transactions=session.query(Transaction).filter(Transaction.user_id==user_id).all()
    session.close()
    return transactions



def getting_spending_by_category(user_id):
    session=Session()

    results=(
        session.query(Category.name, func.sum(Transaction.amount))
        .join(Transaction, Transaction.category_id ==Category.id)
        .filter(Transaction.user_id ==user_id)
        .group_by(Category.name)
        .all()
    )
    session.close()
    return results


def get_budget_summary(user_id):
    session = Session()

    
    user = session.query(User).get(user_id)
    total_spent = session.query(func.sum(Transaction.amount)).filter(Transaction.user_id == user_id).scalar() or 0

    remaining_budget = user.monthly_budget - total_spent
    percent_used = (total_spent / user.monthly_budget) * 100 if user.monthly_budget > 0 else 0

    session.close()

    return {
        "name": user.name,
        "total_spent": total_spent,
        "budget": user.monthly_budget,
        "remaining": remaining_budget,
        "percent_used": percent_used,
        "currency": user.currency
    }

    



