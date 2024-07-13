from sqlalchemy import Column, Integer, String, Numeric, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import UniqueConstraint

Base = declarative_base()

# 구현 할 검색 기능들 생각하며 인덱스 짜기.

# SQLAlchemy의 Index
# '명시적인 것이 암시적인 것보다 낫다'는 파이썬 철학 반영
# 1. 모델 정의 시 생성.
# 2. 데이터베이스에 실제로 인덱스를 만듦.
# 3. 특정 컬럼에대한 검색, 정렬 등의 작업을 빠르게 만들어줌.
# 4. 하지만 데이터 삽입, 업데이트, 삭제 시 성능 저하가 발생할 수 있음.

class CrimeDay(Base):
    __tablename__ = 'crime_day'

    year = Column(Integer, primary_key=True)
    crime_name = Column(String(5), primary_key=True)
    sunday = Column(Integer)
    monday = Column(Integer)
    tuesday = Column(Integer)
    wednesday = Column(Integer)
    thursday = Column(Integer)
    friday = Column(Integer)
    saturday = Column(Integer)

    __table_args__ = (
        UniqueConstraint('year', 'crime_name', name='day_year_crime')
        ,)

    def __repr__(self):
        return f"<CrimeDay(year={self.year}, crime_name='{self.crime_name}')>"

class CrimeTime(Base):
    __tablename__ = 'crime_time'

    year = Column(Integer, primary_key=True)
    crime_name = Column(String(5), primary_key=True)
    range_00h_to_04h = Column(Integer)
    range_04h_to_07h = Column(Integer)
    range_07h_to_12h = Column(Integer)
    range_12h_to_18h = Column(Integer)
    range_18h_to_20h = Column(Integer)
    range_20h_to_24h = Column(Integer)

    __table_args__ = (
        UniqueConstraint('year', 'crime_name', name='time_year_crime')
        ,)

    def __repr__(self):
        return f"<CrimeTime(year={self.year}, CRIME_NAME='{self.crime_name}')>"

class CrimeFive(Base):
    __tablename__ = 'crime_five'

    year = Column(Integer, primary_key=True)
    police_station = Column(String(7), primary_key=True)
    category = Column(String(4), primary_key=True)
    total = Column(Integer)
    murder = Column(Integer)
    robbery = Column(Integer)
    sexual_assault = Column(Integer)
    theft = Column(Integer)
    violence = Column(Integer)

    __table_args__ = (
        UniqueConstraint('year', 'police_station', 'category', name='five_year_police_cate')
        ,)

    def __repr__(self):
        return f"<CrimeFive(year={self.year}, POLICE_STATION='{self.police_station}', CATEGORY='{self.category}')>"

class CrimeCctv(Base):
    __tablename__ = 'crime_cctv'

    manage_no = Column(String(20), primary_key=True)
    address_name = Column(String(20), index=True)
    district = Column(String(4))
    dong = Column(String(10))
    address = Column(String(20), index=True)
    x = Column(Numeric(11, 8))
    y = Column(Numeric(10, 8))

    __table_args__ = (
        Index('idx_district_dong', 'district', 'dong')
        , )

    def __repr__(self):
        return f"<CrimeCctv(manage_no='{self.manage_no}')>"

class CrimeHouse(Base):
    __tablename__ = 'crime_house'

    si_gun_gu_name = Column(String(5), primary_key=True)
    dong = Column(String(10), index=True)
    house_name = Column(String(30), primary_key=True)
    road_addr = Column(String(70), index=True)
    land_name_addr = Column(String(70), index=True)
    call_number = Column(String(40))
    police_station = Column(String(30))
    x = Column(Numeric(9, 6))
    y = Column(Numeric(8, 6))
    reg_date = Column(DateTime)

    __table_args__ = (
        UniqueConstraint('si_gun_gu_name', 'house_name', name='house_si_gun_gu_house_name')
        , Index('idx_si_gun_gu_dong', 'si_gun_gu_name', 'dong')
        ,)

    def __repr__(self):
        return f"<CrimeHouse(si_gun_gu_name='{self.si_gun_gu_name}', HOUSE_NAME='{self.house_name}')>"