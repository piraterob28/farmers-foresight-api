from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, ARRAY, Numeric
from sqlalchemy.orm import declarative_base

# declarative base class
Base = declarative_base()


class Zone(Base):
    __tablename__ = 'zones'

    id = Column(Integer, primary_key=True)
    farm_id = Column(Integer)
    zone_name = Column(String(255))
    length = Column(Float)
    width = Column(Float)
    map_x = Column(Float)
    map_y = Column(Float)
    indoor = Column(Boolean)
    covered= Column(Boolean)
    inserted_at = Column(DateTime)
    update_at = Column(DateTime)
    active = Column(Boolean)