# app/db/init_db.py

from app.db.database import engine, Base
import app.db.models  # noqa

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()