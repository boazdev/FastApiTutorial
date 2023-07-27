""" from sqlalchemy.orm import Session

from app import crud, schemas
#from app.core.config import settings
from sql_app import base  # noqa: F401


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    Base.metadata.create_all(bind=engine) """