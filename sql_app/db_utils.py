from .database import SessionLocal
from sqlalchemy import text
def check_db() -> bool:
    try:
        db = SessionLocal()
        # Try to create session to check if DB is awake
        db.execute(text("SELECT 1"))
        print("connected to mysql database successfully")
        return True
    except Exception as e:
        """ print("db error:",e) """
        print("could not connect to mysql db")
        return False
        """ raise e """
