from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Word(Base):
    __tablename__ = 'word'

    id = Column(Integer, primary_key=True)
    kanji = Column(String, nullable=True)
    kana = Column(String, nullable=False)
    romaji = Column(String, nullable=False)
    meaning = Column(String, nullable=False)
    lesson = Column(String, nullable=False)
    incorrect_count = Column(Integer, nullable=False, default=0)

    e_to_j_revision_status_id = Column(Integer, ForeignKey("revision_status.id"), nullable=True)
    j_to_e_revision_status_id = Column(Integer, ForeignKey("revision_status.id"), nullable=True)

    e_to_j_last_time_revised = Column(DateTime, nullable=True)
    j_to_e_last_time_revised = Column(DateTime, nullable=True)

    e_to_j_revision_status = relationship(
        "RevisionStatus",
        foreign_keys=[e_to_j_revision_status_id],
        back_populates="words_e_to_j"
    )
    j_to_e_revision_status = relationship(
        "RevisionStatus",
        foreign_keys=[j_to_e_revision_status_id],
        back_populates="words_j_to_e"
    )

    def __repr__(self):
        return (
            f"<Word(kanji={self.kanji}, kana={self.kana}, romaji={self.romaji}, "
            f"meaning={self.meaning}, lesson={self.lesson})>"
        )
