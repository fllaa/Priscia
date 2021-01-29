import html
import time

from pyrogram import filters
from pyrogram.errors import BadRequest

from priscia import LOGGER, pciabot
from priscia.modules.log_channel import loggable


@loggable
@pciabot.on_message(filters.command("purge"))
async def purge(client, message):
    args = message.text.split(None, 1)
    if message.reply_to_message:
        user = message.from_user
        chat = message.chat
        bot = await client.get_me()
        user_rights = (await chat.get_member(user.id)).can_delete_messages
        if not user_rights:
            await message.reply_text("You're not admin!")
            return
        bot_rights = (await chat.get_member(bot.id)).can_delete_messages
        if bot_rights:
            message_id = message.reply_to_message.message_id
            delete_to = message.message_id - 1
            if args and len(args) == 2:
                new_del = message_id + int(args[1])
                # No point deleting messages which haven't been written yet.
                if new_del < delete_to:
                    delete_to = new_del

            for m_id in range(
                delete_to, message_id - 1, -1
            ):  # Reverse iteration over message ids
                try:
                    await client.delete_messages(chat.id, m_id)
                except BadRequest as err:
                    if err == "Message can't be deleted":
                        client.send_message(
                            chat.id,
                            "Cannot delete all messages. The messages may be too old, I might "
                            "not have delete rights, or this might not be a supergroup.",
                        )

                    elif err != "Message to delete not found":
                        LOGGER.exception("Error while purging chat messages.")

            try:
                await message.delete()
            except BadRequest as err:
                if err == "Message can't be deleted":
                    client.send_message(
                        chat.id,
                        "Cannot delete all messages. The messages may be too old, I might "
                        "not have delete rights, or this might not be a supergroup.",
                    )

                elif err != "Message to delete not found":
                    LOGGER.exception("Error while purging chat messages.")

            del_msg = client.send_message(chat.id, "Purge complete.")
            time.sleep(2)

            try:
                await del_msg.delete()

            except BadRequest:
                pass

            return (
                "<b>{}:</b>"
                "\n#PURGE"
                "\n<b>Admin:</b> {}"
                "\nPurged <code>{}</code> messages.".format(
                    html.escape(chat.title), user.first_name, delete_to - message_id
                )
            )

    else:
        await message.reply_text(
            "Reply to a message to select where to start purging from."
        )

    return


@loggable
@pciabot.on_message(filters.command("del"))
async def del_message(client, message) -> str:
    if message.reply_to_message:
        user = message.from_user
        chat = message.chat
        bot = await client.get_me()
        user_rights = (await chat.get_member(user.id)).can_delete_messages
        if not user_rights:
            await message.reply_text("You're not admin!")
            return
        bot_rights = (await chat.get_member(bot.id)).can_delete_messages
        if bot_rights:
            await message.reply_to_message.delete()
            await message.delete()
            return (
                "<b>{}:</b>"
                "\n#DEL"
                "\n<b>Admin:</b> {}"
                "\nMessage deleted.".format(html.escape(chat.title), user.first_name)
            )
    else:
        await message.reply_text("Whadya want to delete?")

    return


__help__ = """
Deleting messages made easy with this command. Bot purges \
messages all together or individually.

*Admin only:*
 × /del: Deletes the message you replied to
 × /purge: Deletes all messages between this and the replied to message.
 × /purge <integer X>: Deletes the replied message, and X messages following it.
"""

__mod_name__ = "Purges"
