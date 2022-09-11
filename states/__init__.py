from aiogram.dispatcher.filters.state import StatesGroup, State

class Request_reg(StatesGroup):
    
    group = State()
    name = State()
    L = State()
    count = State()
    _confirm = State()