from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@db:5432/dnd_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Esta linha cria as tabelas no banco de dados se ainda não existirem
Base.metadata.create_all(bind=engine)


# Função para pegar a sessão de conexão com o BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
