from sqlalchemy import Column, Integer, String
from .base import Base
from sqlalchemy.orm import relationship

class RevisionStatus(Base):
    __tablename__ = 'revision_status'

    id = Column(Integer, primary_key=True)
    decription = Column(String, nullable=False)

    words_e_to_j = relationship(
        "Word",
        back_populates="e_to_j_revision_status",
        foreign_keys="Word.e_to_j_revision_status_id"
    )
    words_j_to_e = relationship(
        "Word",
        back_populates="j_to_e_revision_status",
        foreign_keys="Word.j_to_e_revision_status_id"
    )

    def __repr__(self):
        return f"<RevisionStatus(id={self.id}, description={self.description})>"