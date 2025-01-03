"""В этом файле описываются хэндлеры которые срабатывают в карйних случаях, когда произошло, что-то незапланированное"""


from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message


exception_router = Router()


# Этот хэндлер будет срабатывать на любое сообщение, которое не предусмотрено логикой бота
@exception_router.message()
async def process_start_command(message: Message, state: FSMContext):
    await message.answer(
        text='Извините, но я вас не понимаю\n\n'
             'Попробуйте отправить команду /help'
    )
    # Сбрасываем состояние
    await state.clear()


# Этот хэндлер будет срабатывать на нажатие кнопки
# и переводить в состояние ожидания анекдота 2 категории
@exception_router.callback_query()
async def process_group_2_press(callback: CallbackQuery, state: FSMContext):

    # Удаляем сообщение с кнопками, потому что у нас произошла какая-то ошибка с ним
    # чтобы у пользователя не было желания тыкать кнопки
    await callback.message.delete()
    await callback.message.answer(
        text='Извините, произошла какая-то ошибка\nПопробуйте сначала с помощью команды /help',
    )
    # Сбрасываем состояние
    await state.clear()
