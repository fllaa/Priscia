import os
import shutil

import deezloader
import requests
from deezloader.exceptions import NoDataApi
from telegram import ParseMode
from telegram.ext import CommandHandler
from tswift import Song

import priscia.modules.sql.last_fm_sql as sql
from priscia import ARL, LASTFM_API_KEY, dispatcher
from priscia.modules.disable import DisableAbleCommandHandler

TEMP_PATH = "deez_temp/"


def music(update, context):
    if not os.path.exists(TEMP_PATH):
        os.makedirs(TEMP_PATH)
    msg = update.effective_message
    args = context.args
    track = ""
    try:
        loader = deezloader.Login(ARL)
    except Exception as excp:
        msg.reply_text(f"Failed to load token. Error: {excp}")
        return
    try:
        flag = args[0]
        query = args[1]
    except IndexError:
        msg.reply_text("use format: /music <flag> <link/song name> <quality>")
        return
    quality = "MP3_320"
    if len(args) == 3:
        quality = args[2]
    message = msg.reply_text(f"Searching the music as {quality} . . .")
    try:
        if flag == "-link":
            if "deezer" in query:
                track = loader.download_trackdee(
                    query,
                    output=TEMP_PATH,
                    quality=quality,
                    recursive_quality=True,
                    recursive_download=True,
                    not_interface=True,
                )
            if "spotify" in query:
                track = loader.download_trackspo(
                    query,
                    output=TEMP_PATH,
                    quality=quality,
                    recursive_quality=True,
                    recursive_download=True,
                    not_interface=True,
                )
        if flag == "-song":
            if len(query.split("-")) == 2:
                artist, song = query.split("-")
            else:
                message.edit_text("read /help music plox on me")
                return
            track = loader.download_name(
                artist=artist,
                song=song,
                output=TEMP_PATH,
                recursive_quality=True,
                recursive_download=True,
                not_interface=True,
            )
    except NoDataApi:
        message.edit_text("Song Not Found *sad")
        return
    except Exception as excp:
        message.edit_text(f"Failed. Error: {excp}")
        return
    try:
        message.edit_text("Uploading music . . .")
        msg.reply_audio(audio=open(track, "rb"))
        message.edit_text("Done. :)")
    except FileNotFoundError:
        message.edit_text("read /help music plox on me")
    shutil.rmtree(TEMP_PATH)


def set_user(update, context):
    msg = update.effective_message
    args = context.args
    if args:
        user = update.effective_user.id
        username = " ".join(args)
        sql.set_user(user, username)
        msg.reply_text(f"Username set as {username}!")
    else:
        msg.reply_text(
            "That's not how this works...\nRun /setuser followed by your username!"
        )


def clear_user(update, context):
    user = update.effective_user.id
    sql.set_user(user, "")
    update.effective_message.reply_text(
        "Last.fm username successfully cleared from my database!"
    )


def last_fm(update, context):
    msg = update.effective_message
    user = update.effective_user.first_name
    user_id = update.effective_user.id
    username = sql.get_user(user_id)
    if not username:
        msg.reply_text("You haven't set your username yet!")
        return

    base_url = "http://ws.audioscrobbler.com/2.0"
    res = requests.get(
        f"{base_url}?method=user.getrecenttracks&limit=3&extended=1&user={username}&api_key={LASTFM_API_KEY}&format=json"
    )
    if res.status_code != 200:
        msg.reply_text(
            "Hmm... something went wrong.\nPlease ensure that you've set the correct username!"
        )
        return

    try:
        first_track = res.json().get("recenttracks").get("track")[0]
    except IndexError:
        msg.reply_text("You don't seem to have scrobbled any songs...")
        return
    if first_track.get("@attr"):
        # Ensures the track is now playing
        image = first_track.get("image")[3].get("#text")  # Grab URL of 300x300 image
        artist = first_track.get("artist").get("name")
        song = first_track.get("name")
        loved = int(first_track.get("loved"))
        rep = f"{user} is currently listening to:\n"
        if not loved:
            rep += f"🎧  <code>{artist} - {song}</code>"
        else:
            rep += f"🎧  <code>{artist} - {song}</code> (♥️, loved)"
        if image:
            rep += f"<a href='{image}'>\u200c</a>"
    else:
        tracks = res.json().get("recenttracks").get("track")
        track_dict = {
            tracks[i].get("artist").get("name"): tracks[i].get("name") for i in range(3)
        }
        rep = f"{user} was listening to:\n"
        for artist, song in track_dict.items():
            rep += f"🎧  <code>{artist} - {song}</code>\n"
        last_user = (
            requests.get(
                f"{base_url}?method=user.getinfo&user={username}&api_key={LASTFM_API_KEY}&format=json"
            )
            .json()
            .get("user")
        )
        scrobbles = last_user.get("playcount")
        rep += f"\n(<code>{scrobbles}</code> scrobbles so far)"

    msg.reply_text(rep, parse_mode=ParseMode.HTML)


def lyrics(update, context):
    msg = update.effective_message
    query = " ".join(context.args)
    song = ""
    if not query:
        msg.reply_text("You haven't specified which song to look for!")
        return
    else:
        song = Song.find_song(query)
        if song:
            if song.lyrics:
                reply = song.format()
            else:
                reply = "Couldn't find any lyrics for that song!"
        else:
            reply = "Song not found!"
        if len(reply) > 4090:
            with open("lyrics.txt", "w") as f:
                f.write(f"{reply}\n\n\nOwO UwU OmO")
            with open("lyrics.txt", "rb") as f:
                msg.reply_document(
                    document=f,
                    caption="Message length exceeded max limit! Sending as a text file.",
                )
        else:
            msg.reply_text(reply)


__help__ = """
Like name this module, you can search anything about music

 × /music <flag> <query> <quality> : Download music [more info](https://telegra.ph/Music-Downloader-Info-01-20)
 × /lyrics <query>: search lyrics can be song name or artist name
 *Last.FM*
 × /setuser <username>: sets your last.fm username.
 × /clearuser: removes your last.fm username from the bot's database.
 × /lastfm: returns what you're scrobbling on last.fm.
"""

__mod_name__ = "Music"

SET_USER_HANDLER = CommandHandler("setuser", set_user, pass_args=True)
CLEAR_USER_HANDLER = CommandHandler("clearuser", clear_user)
MUSIC_HANDLER = DisableAbleCommandHandler("music", music, pass_args=True)
LASTFM_HANDLER = DisableAbleCommandHandler("lastfm", last_fm)
LYRICS_HANDLER = DisableAbleCommandHandler("lyrics", lyrics, pass_args=True)

dispatcher.add_handler(SET_USER_HANDLER)
dispatcher.add_handler(CLEAR_USER_HANDLER)
dispatcher.add_handler(MUSIC_HANDLER)
dispatcher.add_handler(LASTFM_HANDLER)
dispatcher.add_handler(LYRICS_HANDLER)
