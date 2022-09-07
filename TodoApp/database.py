from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

""" Create a new SQLAlchemy Engine instance. => 데이터베이스와의 연결
- check_same_thread: False
    데이터베이스는 연결 범위 내에서만 존재하기에 같은 연결 object 는 
    쓰레드들 사이에서 공유되기에 해당 옵션의 기능을 수행할 필요 x
"""
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

"""  
Session 객체는 ORM으로 매핑된 객체들을 지속적 작업을 관리해주는 역할
ORM 객체 자체는 세션 내에서 (=Identity map이라는 구조 내) 유지

- 코드로 데이터베이스 관련 작업을 하게 되면 바로 데이터베이스 시스템으로
    작업 내용을 보내는 것이 아니라 세션 객체에서 일시적으로 관리
- 반대로 데이터베이스로부터 데이터를 쿼리하는 SQL 쿼리문을 작성해 커밋을
    날리게 될 경우에도 세션 객체가 일시적으로 보관
=> 사용자는 세션 객체를 통해 데이터 베이스 관련 객체들을 관리

- sessionmaker: 생성한 DB의 데이터 처리, 대화를 위해 생성
    - autocommit: Defaults to False.
    - autoflush: if True, 모든 query에 대해 Session.flush() call to this Session 를 한다.
    - bind: 해당 Session 과 바인딩 되어야 하는 engine or connection 
"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

""" Mapping 매핑
데이터베이스의 구조와 코드를 연결.
데이터베이스에 user라는 테이블이 존재하면 코드 상에도 이 테이블과 정상적으로 연결될 수 있도록 
user 테이블을 코드로 구현함.

<ORM에서 매핑하는 법은 2가지가 있다.>
1) ORM에게 다룰 테이블을 알려주는 방법
2) 데이터베이스의 테이블에 매핑될 테이블 클래스들을 코드로 구현하는 방법

declarative_base: SQLAlchemy 는 위 두가지 방법을 하나로 묶어서 작업할 수 있게 해준다.
"""
Base = declarative_base()
