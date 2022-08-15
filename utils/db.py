from peewee import *

db = SqliteDatabase('db.db')

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class Cellar(BaseModel):
    
    NAME = CharField()
    L = IntegerField()
    COUNT = IntegerField()
    GROUP = CharField()

def init():
    with db:
        querry = db.create_tables([Cellar])

def get_group_from_category(name: str):
    with db:
        try:
            querry = Cellar.select().where(group=name)
            return querry
        except:
            return 'По данной категории еще не заведено позиций'
        pass


def add(name: str,L:int,count: int,group: str):
    "Добавляет позицию"
    with db:
        querry = Cellar(NAME=name,L=L,COUNT=count,GROUP=group).save()

def get_all_in_group(group_name):
    with db:
        querry = Cellar.select(Cellar.NAME, Cellar.COUNT, Cellar.L).where(GROUP=group_name)
    return querry    


def get_all():
    
    querry = Cellar.select().order_by(Cellar.GROUP).execute()
    upper = '''
    -----------------------------------------
    |   Имя   | Литраж | Кол-во |  Группа   |
    =========================================
    '''
    text = upper + "\n".join(['| '.join(map(str, x)) for x in querry])
    # for text in querry:
    #     print(text['NAME'])
    #     text = upper+f'|{text.NAME:^9}|{text.L:^8}|{text.COUNT:^8}|{text.GROUP:^11}|' 
    return text

    # import sqlite3
    # conn = sqlite3.connect("db.db")
    # c = conn.cursor()
    # lists = "SELECT NAME,L,COUNT,GROUP from cellar"
    # c.execute(lists)
    # text = '''
    #      -----------------------------------------
    #      |   Имя   | Литраж | Кол-во |  Группа   |
    #      =========================================
    #      '''
    # text = text + '\n'.join(['| '.join(map(str, x)) for x in c])
    # return text


print(get_all())