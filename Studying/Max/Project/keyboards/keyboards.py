from maxapi.utils.inline_keyboard import InlineKeyboardBuilder
from maxapi.types import CallbackButton

# --- Клавиатуры ---


def get_streets_kb(streets_list):
    builder = InlineKeyboardBuilder()
    row_buttons = []

    for street_name in streets_list:
        btn = CallbackButton(
            text=street_name,
            payload=f"{street_name}"
        )
        row_buttons.append(btn)

        if len(row_buttons) == 2:  # оставил как у тебя, но логичнее 3
            builder.row(*row_buttons)
            row_buttons = []

    if row_buttons:
        builder.row(*row_buttons)

    builder.row()

    return builder.as_markup()


#🗑️
def get_report_kb():
    builder = InlineKeyboardBuilder()
    btn_report = CallbackButton(text='🚮Сообщить о сборе мусора', payload='Сообщить о сборе мусора')
    btn_stat = CallbackButton(text='📊Получить статистику', payload='Получить статистику')
    builder.row(btn_report)
    builder.row(btn_stat)
    return builder.as_markup()


def get_yes_no_kb():
    builder = InlineKeyboardBuilder()
    btn_yes = CallbackButton(text='✅️Да', payload='Да')
    btn_no = CallbackButton(text='❌️Нет', payload='Нет')
    builder.row(btn_yes, btn_no)
    return builder.as_markup()


def get_yes_no_trash_kb():
    builder = InlineKeyboardBuilder()
    btn_yes = CallbackButton(text="✅️Да, собран", payload='Да, собран')
    btn_no = CallbackButton(text="❌️Нет, не собран", payload='Нет, не собран')
    builder.row(btn_yes, btn_no)
    return builder.as_markup()


def get_edit_kb():
    builder = InlineKeyboardBuilder()
    btn = CallbackButton(text="✏️Изменить ответ", payload="Изменить ответ")
    builder.row(btn)
    return builder.as_markup()


def get_restart_kb():
    builder = InlineKeyboardBuilder()
    btn = CallbackButton(text="🔁Начать сначала", payload="Начать сначала")
    builder.row(btn)
    return builder.as_markup()

def get_statistic_types_kb():
    builder = InlineKeyboardBuilder()
    btn_all = CallbackButton(text="✅️❌️➖️ Полная", payload="Полная")
    btn_yes = CallbackButton(text="✅ Да", payload="Да")
    btn_no = CallbackButton(text="❌️ Нет", payload="Нет")
    btn_none = CallbackButton(text="➖️ Без ответа", payload="Без ответа")
    builder.row(btn_all)
    builder.row(btn_yes)
    builder.row(btn_no)
    builder.row(btn_none)
    return builder.as_markup()

def get_statistic_kb():
    builder = InlineKeyboardBuilder()
    btn_stat = CallbackButton(text='📊Получить статистику', payload='Получить статистику')
    builder.row(btn_stat)
    return builder.as_markup()

def get_commands_kb():
    builder = InlineKeyboardBuilder()
    btn_stat = CallbackButton(text='📊Получить статистику',payload='Получить статистику')
    btn_repeat = CallbackButton(text='✉️Повторить рассылку',payload='Повторить рассылку')
    builder.row(btn_repeat)
    builder.row(btn_stat)
    return builder.as_markup()