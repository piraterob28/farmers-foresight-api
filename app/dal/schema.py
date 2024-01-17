from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, ARRAY, Numeric
from sqlalchemy.orm import declarative_base

# declarative base class
Base = declarative_base()


class Chore(Base):
    __tablename__ = 'chores'

    id = Column(Integer, primary_key=True)
    row_batch_id = Column(Integer)
    name = Column(String)
    description = Column(String)
    assigned_to = Column(ARRAY(Integer))
    recurring = Column(Boolean)
    recurr_type = Column(String)
    recurr_week_days = Column(String)
    start_date = Column(DateTime)
    tool_ids = Column(Integer)
    inserted_at = Column(DateTime)
    updated_at = Column(DateTime)
    active = Column(Boolean)


class DailyChoreList(Base):
    __tablename__ = 'daily_chore_lists'

    id = Column(Integer, primary_key=True)
    chore_id = Column(Integer)
    chore_batch_id = Column(Integer)
    todo_date = Column(DateTime)
    completed = Column(Boolean)
    completed_by = Column(ARRAY(Integer))
    record_time = Column(Boolean)
    time_start = Column(DateTime)
    time_end = Column(DateTime)
    notes = Column(String)
    inserted_at = Column(DateTime)
    updated_at = Column(DateTime)
    active = Column(Boolean)


class Farm(Base):
    __tablename__ = 'farms'

    id = Column(Integer, primary_key=True)
    farm_name = Column(String)
    farm_bio = Column(String)
    farm_address = Column(String)
    inserted_at = Column(DateTime)
    updated_at = Column(DateTime)
    farm_avatar_url = Column(String)
    farm_showcase_image_urls = Column(String)
    city = Column(String)
    state = Column(String)
    farm_email = Column(String)
    zip_code = Column(Integer)


class Fertilizer(Base):
    __tablename__ = 'fertilizers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    brand_name = Column(String)
    description = Column(String)
    nitrogen = Column(Integer)
    phosporous = Column(Integer)
    potash = Column(Integer)
    inserted_at = Column(DateTime)
    updated_at = Column(DateTime)
    active = Column(Boolean)


class FertilizerLot(Base):
    __tablename__ = 'fertilizer_lots'

    id = Column(Integer, primary_key=True)
    fertilizer_id = Column(Integer)
    cost = Column(Float)
    price_per_pound = Column(Float)
    quantity = Column(Float)
    quantity_remaining = Column(Float)
    credit_id = Column(Integer)
    inserted_at = Column(DateTime)
    updated_at = Column(DateTime)
    active = Column(Boolean)


class Harvest(Base):
    __tablename__ = 'harvests'

    id = Column(Integer, primary_key=True)
    row_batch_id = Column(Integer)
    harvest_date_planned = Column(DateTime)
    quantity = Column(Float)
    quantity_lost = Column(Float)
    quantity_type = Column(String)
    notes = Column(String)
    inserted_at = Column(DateTime)
    updated_at = Column(DateTime)
    active = Column(Boolean)
    completed = Column(Boolean)


class RowBatch(Base):
    __tablename__ = 'row_batches'

    id = Column(Integer, primary_key=True)
    row_id = Column(Integer)
    seedling_batch_ids = Column(ARRAY(Integer))
    fertilizer_batch_ids = Column(ARRAY(Integer))
    plant_date = Column(DateTime)
    inserted_at = Column(DateTime)
    updated_at = Column(DateTime)
    active = Column(Boolean)


class Row(Base):
    __tablename__ = 'rows'

    id = Column(Integer, primary_key=True)
    zone_id = Column(Integer)
    length = Column(Float)
    width = Column(Float)
    walkway = Column(Boolean)
    walkway_width = Column(Float)
    inserted_at = Column(DateTime)
    updated_at = Column(DateTime)
    active = Column(Boolean)
    is_planted = Column(Boolean)


class Tool(Base):
    __tablename__ = 'tools'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    use_guide = Column(String)
    inserted_at = Column(DateTime)
    updated_at = Column(DateTime)
    active = Column(Boolean)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    farm_id = Column(Integer)
    name = Column(String)
    email = Column(String)
    username = Column(String)
    description = Column(String)
    role = Column(String)
    inserted_at = Column(DateTime)
    updated_at = Column(DateTime)
    active = Column(Boolean)


class Zone(Base):
    __tablename__ = 'zones'

    id = Column(Integer, primary_key=True)
    farm_id = Column(Integer)
    farm_zone_number = Column(Integer)
    zone_name = Column(String(255))
    length = Column(Float)
    width = Column(Float)
    map_x = Column(Float)
    map_y = Column(Float)
    indoor = Column(Boolean)
    covered= Column(Boolean)
    inserted_at = Column(DateTime)
    updated_at = Column(DateTime)
    active = Column(Boolean)
