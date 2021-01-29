import codecs
import os

from nekobin import NekoBin
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from priscia import pciabot


@pciabot.on_message(filters.command("paste"))
async def paste(client, message):
    nekobin = NekoBin()
    if message.reply_to_message:
        if message.reply_to_message.document:
            path = await message.reply_to_message.download("priscia/")
            text = codecs.open(path, "r+", encoding="utf-8")
            paste_text = text.read()
            os.remove(path)
        else:
            paste_text = message.reply_to_message.text
    else:
        await message.reply_text("What am I supposed to do with this?")
        return
    try:
        response = await nekobin.nekofy(paste_text)
        text = "**Pasted to Nekobin!!!**"
        buttons = [
            [
                InlineKeyboardButton(text="View Link", url=response.url),
                InlineKeyboardButton(
                    text="View Raw",
                    url=response.raw,
                ),
            ]
        ]
        await message.reply_text(
            text,
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode="markdown",
            disable_web_page_preview=True,
        )
    except Exception as excp:
        await message.reply_text(f"Pasting Failed. Error: {excp}")
        return


__help__ = """
Copy Paste your Text on Nekobin

 × /paste: Saves replied content to nekobin.com and replies with a url
"""

__mod_name__ = "Paste"
