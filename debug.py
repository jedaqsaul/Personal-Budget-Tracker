from config.setup import Session
from lib.models import Category

session=Session()
categories=session.query(Category).all()
for c in categories:
    print(c.id, c.name)
session.close()