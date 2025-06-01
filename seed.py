from lib.models import Category
from config.setup import Session


def seed_categories():
    session=Session()
    default_categories=[
        "Groceries", "Rent", "Utilities", "Transportation", "Entertainment", "Healthcare", "Education", "Savings", "Enjoyment"
    ]
    for name in default_categories:
        if not session.query(Category).filter_by(name=name).first():
            session.add(Category(name=name))
    session.commit()
    session.close()
if __name__=="__main__":
    seed_categories()