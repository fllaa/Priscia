from pyrogram import filters

from priscia import pciabot

normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]
bubblefont = [
    "ⓐ",
    "ⓑ",
    "ⓒ",
    "ⓓ",
    "ⓔ",
    "ⓕ",
    "ⓖ",
    "ⓗ",
    "ⓘ",
    "ⓙ",
    "ⓚ",
    "ⓛ",
    "ⓜ",
    "ⓝ",
    "ⓞ",
    "ⓟ",
    "ⓠ",
    "ⓡ",
    "ⓢ",
    "ⓣ",
    "ⓤ",
    "ⓥ",
    "ⓦ",
    "ⓧ",
    "ⓨ",
    "ⓩ",
]
fbubblefont = [
    "🅐",
    "🅑",
    "🅒",
    "🅓",
    "🅔",
    "🅕",
    "🅖",
    "🅗",
    "🅘",
    "🅙",
    "🅚",
    "🅛",
    "🅜",
    "🅝",
    "🅞",
    "🅟",
    "🅠",
    "🅡",
    "🅢",
    "🅣",
    "🅤",
    "🅥",
    "🅦",
    "🅧",
    "🅨",
    "🅩",
]
squarefont = [
    "🄰",
    "🄱",
    "🄲",
    "🄳",
    "🄴",
    "🄵",
    "🄶",
    "🄷",
    "🄸",
    "🄹",
    "🄺",
    "🄻",
    "🄼",
    "🄽",
    "🄾",
    "🄿",
    "🅀",
    "🅁",
    "🅂",
    "🅃",
    "🅄",
    "🅅",
    "🅆",
    "🅇",
    "🅈",
    "🅉",
]
fsquarefont = [
    "🅰",
    "🅱",
    "🅲",
    "🅳",
    "🅴",
    "🅵",
    "🅶",
    "🅷",
    "🅸",
    "🅹",
    "🅺",
    "🅻",
    "🅼",
    "🅽",
    "🅾",
    "🅿",
    "🆀",
    "🆁",
    "🆂",
    "🆃",
    "🆄",
    "🆅",
    "🆆",
    "🆇",
    "🆈",
    "🆉",
]
bluefont = [
    "🇦 ",
    "🇧 ",
    "🇨 ",
    "🇩 ",
    "🇪 ",
    "🇫 ",
    "🇬 ",
    "🇭 ",
    "🇮 ",
    "🇯 ",
    "🇰 ",
    "🇱 ",
    "🇲 ",
    "🇳 ",
    "🇴 ",
    "🇵 ",
    "🇶 ",
    "🇷 ",
    "🇸 ",
    "🇹 ",
    "🇺 ",
    "🇻 ",
    "🇼 ",
    "🇽 ",
    "🇾 ",
    "🇿 ",
]
latinfont = [
    "𝒶",
    "𝒷",
    "𝒸",
    "𝒹",
    "ℯ",
    "𝒻",
    "ℊ",
    "𝒽",
    "𝒾",
    "𝒿",
    "𝓀",
    "𝓁",
    "𝓂",
    "𝓃",
    "ℴ",
    "𝓅",
    "𝓆",
    "𝓇",
    "𝓈",
    "𝓉",
    "𝓊",
    "𝓋",
    "𝓌",
    "𝓍",
    "𝓎",
    "𝓏",
]
linedfont = [
    "𝕒",
    "𝕓",
    "𝕔",
    "𝕕",
    "𝕖",
    "𝕗",
    "𝕘",
    "𝕙",
    "𝕚",
    "𝕛",
    "𝕜",
    "𝕝",
    "𝕞",
    "𝕟",
    "𝕠",
    "𝕡",
    "𝕢",
    "𝕣",
    "𝕤",
    "𝕥",
    "𝕦",
    "𝕧",
    "𝕨",
    "𝕩",
    "𝕪",
    "𝕫",
]


@pciabot.on_message(filters.command("weebify"))
async def weebify(client, message):
    args = message.text.split(None, 1)
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower()

    if len(args) >= 2:
        string = args[1].lower()

    if not string:
        await message.reply_text("Usage is `/weebify <text>`", parse_mode="markdown")
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    if message.reply_to_message:
        await message.reply_to_message.reply_text(string)
    else:
        await message.reply_text(string)


@pciabot.on_message(filters.command("bubble"))
async def bubble(client, message):
    args = message.text.split(None, 1)
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower()

    if len(args) >= 2:
        string = args[1].lower()

    if not string:
        await message.reply_text("Usage is `/bubble <text>`", parse_mode="markdown")
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            bubblecharacter = bubblefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bubblecharacter)

    if message.reply_to_message:
        await message.reply_to_message.reply_text(string)
    else:
        await message.reply_text(string)


@pciabot.on_message(filters.command("fbubble"))
async def fbubble(client, message):
    args = message.text.split(None, 1)
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower()

    if len(args) >= 2:
        string = args[1].lower()

    if not string:
        await message.reply_text("Usage is `/fbubble <text>`", parse_mode="markdown")
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            fbubblecharacter = fbubblefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, fbubblecharacter)

    if message.reply_to_message:
        await message.reply_to_message.reply_text(string)
    else:
        await message.reply_text(string)


@pciabot.on_message(filters.command("square"))
async def square(client, message):
    args = message.text.split(None, 1)
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower()

    if len(args) >= 2:
        string = args[1].lower()

    if not string:
        await message.reply_text("Usage is `/square <text>`", parse_mode="markdown")
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            squarecharacter = squarefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, squarecharacter)

    if message.reply_to_message:
        await message.reply_to_message.reply_text(string)
    else:
        await message.reply_text(string)


@pciabot.on_message(filters.command("fsquare"))
async def fsquare(client, message):
    args = message.text.split(None, 1)
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower()

    if len(args) >= 2:
        string = args[1].lower()

    if not string:
        await message.reply_text("Usage is `/fsquare <text>`", parse_mode="markdown")
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            fsquarecharacter = fsquarefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, fsquarecharacter)

    if message.reply_to_message:
        await message.reply_to_message.reply_text(string)
    else:
        await message.reply_text(string)


@pciabot.on_message(filters.command("blue"))
async def blue(client, message):
    args = message.text.split(None, 1)
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower()

    if len(args) >= 2:
        string = args[1].lower()

    if not string:
        await message.reply_text("Usage is `/blue <text>`", parse_mode="markdown")
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            bluecharacter = bluefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bluecharacter)

    if message.reply_to_message:
        await message.reply_to_message.reply_text(string)
    else:
        await message.reply_text(string)


@pciabot.on_message(filters.command("latin"))
async def latin(client, message):
    args = message.text.split(None, 1)
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower()

    if len(args) >= 2:
        string = args[1].lower()

    if not string:
        await message.reply_text("Usage is `/latin <text>`", parse_mode="markdown")
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            latincharacter = latinfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, latincharacter)

    if message.reply_to_message:
        await message.reply_to_message.reply_text(string)
    else:
        await message.reply_text(string)


@pciabot.on_message(filters.command("lined"))
async def lined(client, message):
    args = message.text.split(None, 1)
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower()

    if len(args) >= 2:
        string = args[1].lower()

    if not string:
        await message.reply_text("Usage is `/lined <text>`", parse_mode="markdown")
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            linedcharacter = linedfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, linedcharacter)

    if message.reply_to_message:
        await message.reply_to_message.reply_text(string)
    else:
        await message.reply_text(string)


__help__ = """
Stylish your text!

 × /weebify <text>: weebify your text!
 × /bubble <text>: bubble your text!
 × /fbubble <text>: bubble-filled your text!
 × /square <text>: square your text!
 × /fsquare <text>: square-filled your text!
 × /blue <text>: bluify your text!
 × /latin <text>: latinify your text!
 × /lined <text>: lined your text!
"""

__mod_name__ = "StyleText"
