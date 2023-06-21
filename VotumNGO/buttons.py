from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

gm1 = InlineKeyboardMarkup()
bgm1 = InlineKeyboardButton(text="Головне меню", callback_data="bgm1")
gm1.add(bgm1)



om1 = InlineKeyboardMarkup()
bom1 = InlineKeyboardButton(text="📋Статус ВПО", callback_data="bom1")
bom2 = InlineKeyboardButton(text="🏡Житло", callback_data="bom2")
bom3 = InlineKeyboardButton(text="💳Фін. допомога", callback_data="bom3")
bom4 = InlineKeyboardButton(text="📦Гуманітарна допомога", callback_data="bom4")
bom5 = InlineKeyboardButton(text="🚑Медична допомога", callback_data="bom5")
bom6 = InlineKeyboardButton(text="📁Документи", callback_data="bom6")
bom7 = InlineKeyboardButton(text="♿Людям з інвалідністю", callback_data="bom7")
bom8 = InlineKeyboardButton(text="📚Освіта", callback_data="bom8")
bom9 = InlineKeyboardButton(text="👵🏻👴🏻Пенсіонерам", callback_data="bom9")
bom10 = InlineKeyboardButton(text="👨‍👩‍👧Родинам з дітьми", callback_data="bom10")
bom11 = InlineKeyboardButton(text="🗣️Психологічна допомога", callback_data="bom11")
bom12 = InlineKeyboardButton(text="📝Юр. допомога", callback_data="bom12")
bom13 = InlineKeyboardButton(text="🆘Гарячі лінії", callback_data="bom13")
bom14 = InlineKeyboardButton(text="👩🏼‍💻🧑🏻‍🏫 Працевлаштування", callback_data="bom14")
bom15 = InlineKeyboardButton(text="🚌Евакуація", callback_data="bom15")
bom16 = InlineKeyboardButton(text="⚡️Пункти незламності", callback_data="bom16")
bom17 = InlineKeyboardButton(text="☎️Зворотній зв’язок", callback_data="bom17")
# iid = InlineKeyboardButton(text="id", callback_data="iid")
# om1.add(iid)
om1.add(bom1, bom2)
om1.row(bom3)
om1.row(bom4)
om1.add(bom5)
om1.row(bom8, bom15)
om1.row(bom7)
om1.row(bom9, bom13)
om1.row(bom10)
om1.row(bom11)
om1.row(bom12, bom6)
om1.row(bom14)
om1.row(bom16)
om1.row(bom17)




