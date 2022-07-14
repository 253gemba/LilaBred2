from aiogram.dispatcher.filters.state import State, StatesGroup

class HaircutState(StatesGroup):
    initialize = State()

    haircut = State()

    afro = State()
    afro_full_head = State()
    afro_undercut = State()
    
    bred = State()
    bred_full_head = State()
    bred_undercut = State()
    
    tail = State()
