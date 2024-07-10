from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import UniqueConstraint

Base = declarative_base()

# 배터리 없어서 오늘은 여기까지. 내일 테이블 구조 다 적고 alambic.ini에서 craete 하고 env.py 수정하기!

class CrimeDay(Base):
    __tablename__ = 'CRIME_DAY'

    OCCURRED_YEAR = Column(Integer, primary_key=True)
    CRIME_NAME = Column(String(5))
    SUNDAY = Column(Integer)
    MONDAY = Column(Integer)
    TUESDAY = Column(Integer)
    WEDNESDAY = Column(Integer)
    THURSDAY = Column(Integer)
    FRIDAY = Column(Integer)
    SATURDAY = Column(Integer)

    __table_args__ = (UniqueConstraint('OCCURRED_YEAR', 'CRIME_NAME', name='uix_year_crime'),)