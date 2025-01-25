from typing import Any, Generator
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base, sessionmaker
import config


engine = create_engine(config.DB_CONNECTION_URL, echo=False)
metadata = MetaData()
LocalSession = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base(metadata=metadata)


def get_session() -> Generator[Session, Any, None]:
    try:
        with LocalSession() as session:
            yield session
    finally:
        session.close()
