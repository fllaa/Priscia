import os

import nekos
import requests
from nekos.errors import InvalidArgument
from pyrogram import filters

from priscia import pciabot


@pciabot.on_message(filters.command("neko"))
async def neko(client, message):
    args = message.text.split()
    if len(args) == 3:
        flag = args[1]
        query = args[2]
    else:
        await message.reply_text("use format `/nekos` <flag> <query>!", parse_mode="markdown")
        return
    try:
        img = nekos.img(query)
    except InvalidArgument:
        await message.reply_text(f"{query} are'nt available! check available query on help!")
        return
    try:
        if flag == "-i":
            await message.reply_photo(photo=img, parse_mode="markdown")
        elif flag == "-d":
            await message.reply_document(document=img, parse_mode="markdown")
        elif flag == "-s":
            stkr = "sticker.webp"
            with open(stkr, "wb") as f:
                f.write(requests.get(img).content)
            await message.reply_sticker(sticker=open(stkr, "rb"))
            os.remove("sticker.webp")
        elif flag == "-v":
            await message.reply_video(video=img, parse_mode="markdown")
        else:
            await message.reply_text("Put flags correctly!!!")
    except Exception as excp:
        await message.reply_text(f"Failed to find image. Error: {excp}")


__help__ = """
× /neko <flags> <query>: Get random images from [Nekos API](nekos.life)
*Available flags:*
-i = send as image
-d = send as document(full resolution)
-s = send as sticker
-v = send as video(only for some query)
*Available query:*
Check this : [List Query](https://telegra.ph/List-Query-of-Nekos-01-19)
"""

__mod_name__ = "Nekos"
