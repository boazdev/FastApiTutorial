# Import all the models, so that Base has them before being
# imported by Alembic
from sql_app.base_class import Base  # noqa
#from app.models.item import Item  # noqa
from models.user_model import User  # noqa