from sqlalchemy import create_engine
from sqlalchemy import Column, Integer,String, ForeignKey

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cellar(Base):
    __tablename__ = 'cellar'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    Litres = Column(Integer)
    count = Column(Integer)
    group = Column(String)

    def __init__(self, name, Litres, count, group):
        self.name = name
        self.Litres = Litres
        self.count = count 
        self.group = group

    # def __repr__(self):
    #     info: str = f'''
    #     Наименование: {self.name}
    #     Литраж: {self.Litres}
    #     Кол-во: {self.count}
    #     Группа: {self.group}
    #     '''
    #     return info

engine = create_engine('sqlite:///.\db.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def create_db():
    Base.metadata.create_all(engine)

def add_request(group, name, Litres, count):
    request = Cellar(name=name, Litres=Litres, count=count, group=group)
    session.add(request)
    session.commit()

def get_data():
    request = session.query(Cellar).all()
    name_field = '       Название       '
    Litres_field = '    Объём     '
    count_field = '    Кол-во    '
    group_field = '   Группа     '
    text = group_field + '|' + name_field +'|' + Litres_field + '|' + count_field + ' \n===============================================\n'
    for raw in request:
        text = text+f'{raw.group:^14}|{raw.name:^25}|{raw.Litres:^14}|{raw.count:^14}\n'
    return text
