from sqlalchemy import create_engine
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from app.models import Base, CrimeDay, CrimeTime, CrimeFive, CrimeCctv, CrimeHouse

# 데이터베이스 url 설정
DATABASE_URL = "mysql+pymysql://python_daejeon:1111@127.0.0.1:3306/python_daejeon"

print(f"Connecting to database: {DATABASE_URL}")

# 엔진 생성
engine =create_engine(DATABASE_URL, echo=True)

print("Engine create.")

# 모든 테이블 생성
# Base.metadata.create_all(engine)

try:
    Base.metadata.create_all(engine)
    print("table create success.")
except Exception as e:
    print(f"error: {e}")

from sqlalchemy import inspect
inspector = inspect(engine)
tables = inspector.get_table_names()
print("tables in db:")
for table in tables:
    print(table)

print("end")