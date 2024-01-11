from sqlalchemy import create_engine, text

engine = create_engine("postgresql://user_good:pass_good@localhost:5432/postgres", echo=True)