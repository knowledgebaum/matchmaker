from sqlalchemy import Table, Column, Integer, Numeric, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Myco_DB(Base):
    __tablename__ = 'mushrooms'

    mushroom_id = Column(Integer(), primary_key=True)
    family = Column(Text())
    latin_name = Column(Text())
    english_name = Column(Text())
    notes = Column(Text())
    chemical_reaction = Column(Text())
    cap = Column(Text())
    flesh = Column(Text())
    underside = Column(Text())
    stem = Column(Text())
    odor = Column(Text())
    taste = Column(Text())
    edibility = Column(Text())
    habitat = Column(Text())
    spore_deposit = Column(Text())
    microscopic = Column(Text())
    name_origin = Column(Text())
    similar = Column(Text())
    sources = Column(Text())

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')

Base.metadata.create_all(engine)



