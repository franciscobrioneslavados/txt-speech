from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import MONEY

Base = declarative_base()

class Sentiments(Base):
    __tablename__ = 'sentiments'
    _id = Column(Integer, primary_key=True)
    listSentiment = Column(jsonb[])
    jsonBlob = Column(jsonb)
    eventId = Column(String)
    createdAt = Column(Date)
    updatedAt = Column(Date)

    def __repr__(self):
        return "<Book(title='{}', author='{}', pages={}, published={}, price={})>" \
            .format(self.title, self.author, self.pages, self.published, self.price)