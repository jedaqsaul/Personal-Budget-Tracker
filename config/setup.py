from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

DATABASE_URL ="sqlite:///lib/db/store.db"

engine=create_engine(DATABASE_URL, echo=False)

Session=sessionmaker(bind=engine)