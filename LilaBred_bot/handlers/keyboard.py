from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Опции

price = KeyboardButton("Прайс")

courses = KeyboardButton("Курсы")

contacts = KeyboardButton("Контакты")

first_choice_button = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(price).insert(courses).insert(contacts)
)

# Прайс

afro = KeyboardButton("Афрокосички точечно")

breds = KeyboardButton("Брейды")

afrotail = KeyboardButton("Афрохвост")

back_type_options = KeyboardButton("Назад к выбору опций")

price_choice_button = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .add(afro)
    .insert(breds)
    .insert(afrotail)
    .insert(back_type_options)
)

# Афрокосички зона

afro_head = KeyboardButton("На всю голову")

afro_undercut = KeyboardButton("На андеркат(макушка)")

back_type_choice = KeyboardButton("Назад к выбору прически")

afro_zone_choice_button = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .add(afro_head)
    .insert(afro_undercut)
    .insert(back_type_choice)
)


# Афрокосички > зона: вся голова > толщина

afro_head_big = KeyboardButton("Крупные(20-40 шт.)")

afro_head_thick = KeyboardButton("Толстые(40-60 шт.)")

afro_head_middle = KeyboardButton("Средние(60-80 шт.)")

afro_head_small = KeyboardButton("Мелкие(80-100 шт.)")

back_zone_afro = KeyboardButton("Назад к выбору зоны для афрокосичек")

afro_head_thickness_button = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    .add(afro_head_big)
    .insert(afro_head_thick)
    .insert(afro_head_middle)
    .insert(afro_head_small)
    .insert(back_zone_afro)
)

# Афрокосички > зона: вся макушка > толщина

afro_undercut_big = KeyboardButton("Крупные(10-20 шт.)")

afro_undercut_thick = KeyboardButton("Толстые(30-40 шт.)")

afro_undercut_middle = KeyboardButton("Средние(40-60 шт.)")

back_zone_afro = KeyboardButton("Назад к выбору зоны для афрокосичек")

afro_undercut_thickness_button = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    .add(afro_undercut_big)
    .insert(afro_undercut_thick)
    .insert(afro_undercut_middle)
    .insert(back_zone_afro)
)


# Афрохвост > толщина

tail_long = KeyboardButton("Длинный хвост(75-80 см.)")

tail_middle = KeyboardButton("Средний хвост(55-60 см.)")

tail_short = KeyboardButton("Короткий хвост(40-45 см.)")

back_type_choice = KeyboardButton("Назад к выбору прически")

tail_length_button = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    .add(tail_long)
    .insert(tail_middle)
    .insert(tail_short)
    .insert(back_type_choice)
)


# Брейды зона

breds_head_material = KeyboardButton("Вся голова")

breds_undercut_material = KeyboardButton("Андеркат(макушка)")

back_type_choice = KeyboardButton("Назад к выбору прически")

breds_zone_choice_button = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    .add(breds_head_material)
    .insert(breds_undercut_material)
    .insert(back_type_choice)
)


# Брейды > зона: вся голова > с материалом > толщина

breds_head_materials_big = KeyboardButton("2-4 шт.")

breds_head_materials_thick = KeyboardButton("5-7 шт.")

breds_head_materials_middle = KeyboardButton("8-10 шт.")

back_zone_breds = KeyboardButton("Назад к выбору наличия материалов")

breds_head_material_thickness_button = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    .add(breds_head_materials_big)
    .insert(breds_head_materials_thick)
    .insert(breds_head_materials_middle)
    .insert(back_zone_breds)
)


# Брейды > зона: вся голова > без материала > толщина

breds_head_big = KeyboardButton("2-4 шт.")

breds_head_thick = KeyboardButton("5-7 шт.")

breds_head_middle = KeyboardButton("8-10 шт.")

back_zone_breds = KeyboardButton("Назад к выбору наличия материалов")

breds_head_thickness_button = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    .add(breds_head_big)
    .insert(breds_head_thick)
    .insert(breds_head_middle)
    .insert(back_zone_breds)
)


# Брейды > зона: макушка > с материалом > толщина

breds_undercut_materials_big = KeyboardButton("2-4 шт.")

breds_undercut_materials_thick = KeyboardButton("5-7 шт.")

breds_undercut_materials_middle = KeyboardButton("8-10 шт.")

back_zone_breds = KeyboardButton("Назад к выбору наличия материалов")

breds_undercut_material_thickness_button = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    .add(breds_undercut_materials_big)
    .insert(breds_undercut_materials_thick)
    .insert(breds_undercut_materials_middle)
    .insert(back_zone_breds)
)


# Брейды > зона: макушка > без материала > толщина

breds_undercut_big = KeyboardButton("2-4 шт.")

breds_undercut_thick = KeyboardButton("5-7 шт.")

breds_undercut_middle = KeyboardButton("8-10 шт.")

back_breds_undercut_material = KeyboardButton("Назад к выбору наличия материалов")

breds_undercut_thickness_button = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    .add(breds_undercut_big)
    .insert(breds_undercut_thick)
    .insert(breds_undercut_middle)
    .insert(back_zone_breds)
)

# Брейды > зона: макушка > с материалом / без материала

breds_undercut_with_material = KeyboardButton("С материалом")

breds_undercut_without = KeyboardButton("Без материала")

back_zone_breds = KeyboardButton("Назад к выбору зоны для брейдов")

breds_undercut_material_button = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    .add(breds_undercut_with_material)
    .insert(breds_undercut_without)
    .insert(back_zone_breds)
)

# Брейды > зона: голова > с материалом / без материала

breds_head_with_material = KeyboardButton("С материалом")

breds_head_without = KeyboardButton("Без материала")

back_zone_breds = KeyboardButton("Назад к выбору зоны для брейдов")

breds_head_material_button = (
    ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    .add(breds_head_with_material)
    .insert(breds_head_without)
    .insert(back_zone_breds)
)
