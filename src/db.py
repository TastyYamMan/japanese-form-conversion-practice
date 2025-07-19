from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Word  # Ensure models.py is accessible

engine = create_engine('sqlite:///japanese_practice.db')
Session = sessionmaker(bind=engine)
session = Session()
