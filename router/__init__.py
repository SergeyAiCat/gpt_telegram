#импорт всех роутеров
from .callback_router import my_callback
from .command_router import my_command
from .dal_router import my_dal
from .gpt_router import my_gpt
#добавление роутеров в метод ALL для импорта через *
__all__=['my_callback','my_command','my_dal','my_gpt']
