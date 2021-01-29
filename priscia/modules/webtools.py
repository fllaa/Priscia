import asyncio
import datetime
import html
import os
import platform
import subprocess
import sys
import time
import traceback
from platform import python_version

import aiohttp
import speedtest
from psutil import boot_time, cpu_percent, disk_usage, virtual_memory
from pyrogram import __version__ as __pyro__
from pyrogram import filters
from pyrogram.errors import BadRequest
from spamwatch import __version__ as __sw__
from telegram import __version__

from priscia import MESSAGE_DUMP, OWNER_ID, pciabot

session = aiohttp.ClientSession()


@pciabot.on_message(filters.command("ping"))
async def ping(client, message):
    start_time = time.time()
    msg = await message.reply_text("Pinging...")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    await msg.edit_text("*Pong!!!*\n`{}ms`".format(ping_time), parse_mode="markdown")


# Kanged from PaperPlane Extended userbot
def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "Mb/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@pciabot.on_message(
    filters.user(OWNER_ID) & filters.command("ip"),
)
async def get_bot_ip(client, message):
    """Sends the bot's IP address, so as to be able to ssh in if necessary.
    OWNER ONLY.
    """
    async with session.get("http://ipinfo.io/ip") as res:
        await message.reply_text(res.text)


@pciabot.on_message(
    filters.user(OWNER_ID) & filters.command("speedtest"),
)
async def speedtst(client, message):
    msg = await message.reply_text("Running high speed test . . .")
    test = speedtest.Speedtest()
    await msg.edit_text("Looking for best server . . .")
    test.get_best_server()
    await msg.edit_text("Downloading . . .")
    test.download()
    await msg.edit_text("Uploading . . .")
    test.upload()
    await msg.edit_text("Finalizing . . .")
    test.results.share()
    result = test.results.dict()
    await msg.edit_text(
        "Download "
        f"{speed_convert(result['download'])} \n"
        "Upload "
        f"{speed_convert(result['upload'])} \n"
        "Ping "
        f"{result['ping']} \n"
        "ISP "
        f"{result['client']['isp']}"
    )


@pciabot.on_message(
    filters.user(OWNER_ID) & filters.command("sysinfo"),
)
async def system_status(client, message):
    uptime = datetime.datetime.fromtimestamp(boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    status = "<b>======[ SYSTEM INFO ]======</b>\n\n"
    status += "<b>System uptime:</b> <code>" + str(uptime) + "</code>\n"

    uname = platform.uname()
    status += "<b>System:</b> <code>" + str(uname.system) + "</code>\n"
    status += "<b>Node name:</b> <code>" + str(uname.node) + "</code>\n"
    status += "<b>Release:</b> <code>" + str(uname.release) + "</code>\n"
    status += "<b>Version:</b> <code>" + str(uname.version) + "</code>\n"
    status += "<b>Machine:</b> <code>" + str(uname.machine) + "</code>\n"
    status += "<b>Processor:</b> <code>" + str(uname.processor) + "</code>\n\n"

    mem = virtual_memory()
    cpu = cpu_percent()
    disk = disk_usage("/")
    status += "<b>CPU usage:</b> <code>" + str(cpu) + " %</code>\n"
    status += "<b>Ram usage:</b> <code>" + str(mem[2]) + " %</code>\n"
    status += "<b>Storage used:</b> <code>" + str(disk[3]) + " %</code>\n\n"
    status += "<b>Python version:</b> <code>" + python_version() + "</code>\n"
    status += "<b>PTB version:</b> <code>" + str(__version__) + "</code>\n"
    status += "<b>Pyrogram version:</b> <code>" + str(__pyro__) + "</code>\n"
    status += "<b>Spamwatch API:</b> <code>" + str(__sw__) + "</code>\n"
    await message.reply_text(status, parse_mode="HTML")


@pciabot.on_message(filters.command("leavechat"))
async def leavechat(client, message):
    args = message.text.split(None, 1)
    if args:
        chat_id = int(args[1])
    else:
        await message.reply_text("Bro.. Give Me ChatId And boom!!")
    try:
        titlechat = client.get_chat(chat_id).title
        await asyncio.gather(
            client.send_message(
                chat_id,
                "I'm here trying to survive, but this world is too cruel, goodbye everyone 😌",
            ),
            client.leave_chat(chat_id),
            message.reply_text("I have left the group {}".format(titlechat)),
        )

    except BadRequest as excp:
        if excp == "bot is not a member of the supergroup chat":
            await message.reply_text(
                "I'Am not Joined The Group, Maybe You set wrong id or I Already Kicked out"
            )

        else:
            return


@pciabot.on_message(
    filters.user(OWNER_ID) & filters.command("gitpull"),
)
async def gitpull(client, message):
    args = message.text.split(None, 1)
    branch = args[1]
    sent_msg = await message.reply_text("Pulling all changes from remote...")
    subprocess.Popen(f"git pull {branch}", stdout=subprocess.PIPE, shell=True)

    sent_msg_text = (
        sent_msg.text
        + "\n\nChanges pulled... I guess..\nContinue to restart with /reboot "
    )
    await sent_msg.edit_text(sent_msg_text)


@pciabot.on_message(
    filters.user(OWNER_ID) & filters.command("reboot"),
)
async def restart(client, message):
    user = message.from_user

    await message.reply_text("Starting a new instance and shutting down this one")

    if MESSAGE_DUMP:
        datetime_fmt = "%H:%M - %d-%m-%Y"
        current_time = datetime.datetime.utcnow().strftime(datetime_fmt)
        message = (
            f"<b>Bot Restarted </b>"
            f"<b>By :</b> <code>{html.escape(user.first_name)}</code>"
            f"<b>\nDate Bot Restart : </b><code>{current_time}</code>"
        )
        await client.send_message(
            chat_id=MESSAGE_DUMP,
            text=message,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )

    os.system("bash start")


@pciabot.on_message(
    filters.user(OWNER_ID) & filters.command("eval"),
)
async def evaluator(client, message):
    if message.text:
        args = message.text.split(None, 1)
        code = args[1]
        try:
            exec(code)  # disable=W0122
        except BaseException:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(
                etype=exc_type, value=exc_obj, tb=exc_tb
            )
            await message.reply_text(
                "**Execute**\n`{}`\n\n*Failed:*\n```{}```".format(
                    code, "".join(errors)
                ),
                parse_mode="markdown",
            )


@pciabot.on_message(
    filters.user(OWNER_ID) & filters.command("exec"),
)
async def executor(client, message):
    if message.text:
        args = message.text.split(None, 1)
        code = args[1]
        run = subprocess.run(code, stdout=subprocess.PIPE, shell=True, check=True)
        output = run.stdout.decode()
        await message.reply_text(
            f"*Input:*\n`{code}`\n\n*Output:*\n`{output}`", parse_mode="HTML"
        )
