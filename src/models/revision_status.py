from sqlalchemy import Column, Integer, String
from models import Base
from sqlalchemy.orm import relationship

class RevisionStatus(Base):
    __tablename__ = 'revision_status'

    id = Column(Integer, primary_key=True)
    decription = Column(String, nullable=False)

    word = relationship("Word", back_populates="revision_status")

    def __repr__(self):
        return f"<RevisionStatus(id={self.id}, description={self.description})>"