from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class StreamItemModel(Base):
    __tablename__ = 'streamitems'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text)
    description = Column(Text)
    topic = Column(Text)
    category = Column(Text)
    object_path = Column(Text)
