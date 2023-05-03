from models.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Salesdep(Base):
    __tablename__ = 'salesdep'

    id = Column(Integer, primary_key=True)
    manager_name = Column(String(250), nullable=False)
    client = relationship('Client')

    def __repr__(self):
        return f"Отдел продаж (ID менеджера: {self.id}, имя менеджера: {self.manager_name})"


