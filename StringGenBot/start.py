from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""ٲهلٲ بك عزيزي {msg.from_user.mention},

⎊¦ فـي بـوت اسـتـخـراج الـجـلـسـات
⎊¦ يمكنك استخراج الجلسات الـتالية
⎊¦ بايروجرام للحسابات & بايروجرام للبوتات
⎊¦ بـايـروجـرام مـيوزك احـدث إصـدار 
⎊¦ تيرمـكـس للحسابات & تيرمـكـس للبوتات

⎊¦ بواسطـة ✗𝙰𝙻𝙴𝚇𝙴𝚂✗ @z_z_zv
 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="بدٲ ٲستخرٲج جلسه", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("قنٲة ٲلمطؤر", url="https://t.me/T_T_T_U"),
                    InlineKeyboardButton("✘𝙰𝙻𝙴𝚇𝙴𝚂✘", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
