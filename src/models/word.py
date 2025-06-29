from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models import Base
from sqlalchemy.orm import relationship

class Word(Base):
    __tablename__ = 'word'

    id = Column(Integer, primary_key=True)
    kanji = Column(String, nullable=True)
    kana = Column(String, nullable=False)
    romaji = Column(String, nullable=False)
    meaning = Column(String, nullable=False)
    lesson = Column(String, nullable=False)
    #verb_id = Column(Integer, nullable=True)
    #adjective_id = Column(Integer, nullable=True)
    revision_status_id = Column(ForeignKey("revision_status.id"), nullable=True)
    last_time_revised = Column(DateTime, nullable=True)

    revision_status = relationship("RevisionStatus", back_populates="word")

    def __repr__(self):
        return f"<Word(kanji={self.kanji}, kana={self.kana}, romaji={self.romaji}, meaning={self.meaning}, lesson={self.lesson})>"