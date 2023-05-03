from sqlalchemy import Column, Integer, String, ForeignKey
from models.database import Base

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    discount = Column(Integer)
    manager_id = Column(Integer, ForeignKey('salesdep.id'))

    def __init__(self, name, discount, manager_id):
        self.name = name
        self.discount = discount
        self.manager_id = manager_id

    def __repr__(self):
        return f"Клиент (название: {self.name}," \
               f" скидка: {self.discount}%, ID менеджера: {self.manager_id})"
    