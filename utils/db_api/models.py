from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer,String, ForeignKey


Base = declarative_base()

class Cellar(Base):
    __tablename__ = 'cellar'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer) # id пользователя
    uid_name = Column(String) # Имя пользователя
    name = Column(String)
    L = Column(Integer)
    count = Column(Integer)
    group = Column(String)

    def __init__(self, name: str, L: int, count: int, group: str):
        self.name = name
        self.L = L
        self.count = count, 
        self.group = group

    def __repr__(self):
        info: str = f'''
        Наименование: {self.name}
        Литраж: {self.L}
        Кол-во: {self.count}
        Группа: {self.group}
        '''
        return info
