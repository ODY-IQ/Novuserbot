import asyncio

from userbot import iqthon

from ..core.managers import edit_or_reply
from ..helpers.utils import _format
from . import ALIVE_NAME

plugin_category = "fun"


@iqthon.iq_cmd(
    pattern="تهكير$",
    command=("تهكير", plugin_category),
    info={
        "header": "Fun hack animation.",
        "description": "Reply to user to show hack animation",
        "note": "This is just for fun. Not real hacking.",
        "usage": "{tr}hack",
    },
)
async def _(event):
    "Fun hack animation."
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        idd = reply_message.sender_id
        if idd == 1226408155:
            await edit_or_reply(
                event, "**⌔︙ عـذرا أنـة مبـرمج السـورس لايـمكن تهكيـرة. ⚜️**"
            )
        else:
            event = await edit_or_reply(event, "**⌔︙ جـاري التـهكير ⚠️**")
            animation_chars = [
                "**⌔︙ جـاري الاتصـال بجهـاز الضحـية لأختـراقـة  📳**",
                "**⌔︙ أختـراق جهـاز الضحـية الهـددف محـدد جـاري أختـراقـة ㊙️**",
                "**⌔︙ تحـميل الاخـتراق  ㊙️ .. 0%**\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
                "**⌔︙ تحـميل الاخـتراق  ㊙️ .. 4%**\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
                "**⌔︙ تحـميل الاخـتراق  ㊙️ ..10%**\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
                "**⌔︙ تحـميل الاخـتراق  ㊙️ .. 20%**\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
                "**⌔︙ تحـميل الاخـتراق  ㊙️ .. 36%**\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
                "**⌔︙ تحـميل الاخـتراق  ㊙️ .. 52%**\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
                "**⌔︙ تحـميل الاخـتراق  ㊙️ .. 84%**\n█████████████████████▒▒▒▒ `",
                "**⌔︙ تحـميل الاخـتراق  ㊙️ .. 100%**\n████████████████████████`",
                f"**⌔︙ تـم اخـتراق الضحـية 🆘 الفـديـة لألغـاء الاخـتراق تشـريب بالـحم لـ السيـد 🙂 : `{ALIVE_NAME}` . بـدون تنـازل**",
            ]
            animation_interval = 3
            animation_ttl = range(11)
            for i in animation_ttl:
                await asyncio.sleep(animation_interval)
                await event.edit(animation_chars[i % 11])
    else:
        await edit_or_reply(
            event,
            "**⌔︙ لم يتم تعريف أي مستخدم قم برد على الضحية**",
            parse_mode=_format.parse_pre,
        )
