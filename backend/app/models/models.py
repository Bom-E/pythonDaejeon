from sqlalchemy import Column, Integer, String, Numeric, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import UniqueConstraint

Base = declarative_base()

# 구현 할 검색 기능들 생각하며 인덱스 짜기.

class CrimeDay(Base):
    __tablename__ = 'CRIME_DAY'

    YEAR = Column(Integer, primary_key=True)
    CRIME_NAME = Column(String(5), primary_key=True)
    SUNDAY = Column(Integer)
    MONDAY = Column(Integer)
    TUESDAY = Column(Integer)
    WEDNESDAY = Column(Integer)
    THURSDAY = Column(Integer)
    FRIDAY = Column(Integer)
    SATURDAY = Column(Integer)

    __table_args__ = (
        UniqueConstraint('YEAR', 'CRIME_NAME', name='day_year_crime')
        , Index()
        ,)

    def __repr__(self):
        return f"<CrimeDay(YEAR={self.YEAR}, CRIME_NAME='{self.CRIME_NAME}')>"

class CrimeTime(Base):
    __tablename__ = 'CRIME_TIME'

    YEAR = Column(Integer, primary_key=True)
    CRIME_NAME = Column(String(5), primary_key=True)
    RANGE_00H_TO_04H = Column(Integer)
    RANGE_04H_TO_07H = Column(Integer)
    RANGE_07H_TO_12H = Column(Integer)
    RANGE_12H_TO_18H = Column(Integer)
    RANGE_18H_TO_20H = Column(Integer)
    RANGE_20H_TO_24H = Column(Integer)

    __table_args__ = (
        UniqueConstraint('YEAR', 'CRIME_NAME', name='time_year_crime')
        ,Index()
        ,)

    def __repr__(self):
        return f"<CrimeTime(YEAR={self.YEAR}, CRIME_NAME='{self.CRIME_NAME}')>"

class CrimeFive(Base):
    __tablename__ = 'CRIME_FIVE'

    YEAR = Column(Integer, primary_key=True)
    POLICE_STATION = Column(String(7), primary_key=True)
    CATEGORY = Column(String(4), primary_key=True)
    TOTAL = Column(Integer)
    MURDER = Column(Integer)
    ROBBERY = Column(Integer)
    SEXUAL_ASSAULT = Column(Integer)
    THEFT = Column(Integer)
    VIOLENCE = Column(Integer)

    __table_args__ = (
        UniqueConstraint('YEAR', 'POLICE_STATION', 'CATEGORY', name='five_year_police_cate')
        , Index()
        ,)

    def __repr__(self):
        return f"<CrimeFive(YEAR={self.YEAR}, POLICE_STATION='{self.POLICE_STATION}', CATEGORY='{self.CATEGORY}')>"

class CrimeCctv(Base):
    __tablename__ = 'CRIME_CCTV'

    MANAGE_NO = Column(String(20), primary_key=True)
    ADDRESS_NAME = Column(String(20))
    DISTRICT = Column(String(4))
    DONG = Column(String(10))
    ADDRESS = Column(String(20))
    X = Column(Numeric(11, 8))
    Y = Column(Numeric(10, 8))

    __table_args__ = (
        Index('idx_district_dong', 'DISTRICT', 'DONG')
        ,)

    def __repr__(self):
        return f"<CrimeCctv(MANAGE_NO='{self.MANAGE_NO}')>"

class CrimeHouse(Base):
    __tablename__ = 'CRIME_HOUSE'

    SI_GUN_GU_NAME = Column(String(5), primary_key=True)
    DONG = Column(String(10))
    HOUSE_NAME = Column(String(30), primary_key=True)
    ROAD_ADDR = Column(String(70))
    LAND_NAME_ADDR = Column(String(70))
    CALL_NUMBER = Column(String(40))
    # CALL_NUMBER 부분은 전화번호 없음 하고 그 NAME에 따라 소비자 보호센터 데이터를 받아 오는 게 더 효울적인지, 아니면 그냥 이렇게 하는 게 효율적인지.
    POLICE_STATION = Column(String(30))
    X = Column(Numeric(9, 6))
    Y = Column(Numeric(8, 6))
    REG_DATE = Column(DateTime)

    __table_args__ = (
        UniqueConstraint('SI_GUN_GU_NAME', 'HOUSE_NAME', name='house_si_gun_gu_house_name')
        , Index()
        ,)

    def __repr__(self):
        return f"<CrimeHouse(SI_GUN_GU_NAME='{self.SI_GUN_GU_NAME}', HOUSE_NAME='{self.HOUSE_NAME}')>"