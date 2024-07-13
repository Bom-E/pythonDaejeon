# 프로젝트의 규모가 커지면 이 파일을 이용하여 Base의 설정을 한다고 함.

# 장점 

# 1. 중앙 집중화 : 관리 및 유지보수가 쉬워짐
# 2. 재사용성 : Base, engine, SessionLocal, get_db() 등을 base.py에 정의함으로써 쉽게 import
# 3. 설정분리 : 데이터베이스 url 같은 설정 정보를 별도의 파일에 두면 환경에 띠라 쉽게 변경 가능
# 4. 의존성 관리 : 다른 모듈들이 이 basse.py를 import하게 함으로써, 데이터베이스 관련 설정에대한 의존성을 명확히 할 수 있음.
# 5. 초기화 순서 : SQLAlchemy 설정의 초기화 순서가 중요할 경우도 있는데, 이를 한 파일에서 관리하면 순서를 보장하기 쉬움.
# 6. 확장성 : 나중에 데이터베이스 관련 유틸리티 함수나 추가 설정을 넣게 쉬움. 

# 설정 사용 에시

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# 데이터베이스 URL
# DATABASE_URL = "mysql+pymysql://python_daejeon:1111@127.0.0.1:3306/python_daejeon"

# 엔진 생성
# engine = create_engine(DATABASE_URL)

# 세션 팩토리 생성
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스 생성
# Base = declarative_base()

# 데이터베이스 세션을 얻는 함수
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()