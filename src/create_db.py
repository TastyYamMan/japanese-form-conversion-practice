from sqlalchemy import create_engine
from models.base import Base
import models.word  # Import to register models
import models.revision_status  # Import to register models

# Create db
engine = create_engine('sqlite:///src/japanese_practice.db')

# Create tables
Base.metadata.create_all(engine)