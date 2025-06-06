from sqlalchemy import MetaData, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime




convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata=MetaData(naming_convention=convention)
Base=declarative_base(metadata=metadata)


class User(Base):
    __tablename__ ='users'


    id=Column(Integer, primary_key=True)
    name=Column(String)
    email=Column(String, unique=True)
    password=Column(String)
    created_at=Column(DateTime(), default=datetime.now())
    monthly_budget=Column(Float)
    currency=Column(String)

    # let us add our relatinship code here
    categories =relationship("Category", back_populates="user")
    transactions = relationship("Transaction", back_populates="user")

class Category(Base):
    __tablename__='categories'

    id =Column(Integer, primary_key=True)
    name =Column(String)
    user_id=Column(Integer, ForeignKey('users.id'))

    # we will now define our relationship
    user=relationship("User", back_populates='categories')
    transactions = relationship("Transaction", back_populates="category")

class Transaction(Base):
    __tablename__='transactions'
    

    id =Column(Integer, primary_key=True)
    amount =Column(Float, nullable=False)
    type=Column(String, nullable=False)
    date= Column(DateTime(), default=datetime.now())

    user_id=Column(Integer, ForeignKey("users.id"))
    category_id=Column(Integer, ForeignKey("categories.id"))


    # what are our relationships -here
    user =relationship("User", back_populates="transactions")
    category=relationship("Category", back_populates="transactions")

    # add a repr method

    def __repr__(self):
        return f"<Transaction(id={self.id}, amount={self.amount}, type={self.type})>"