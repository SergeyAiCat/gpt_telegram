from aiogram.fsm.state import State, StatesGroup
#создание состояний ожидания промптов для определённый моделей нейросети
class ai_model(StatesGroup):
    gpt3 = State()
    dal2 = State()