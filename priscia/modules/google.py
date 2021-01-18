import os
import re
import urllib
from urllib.error import HTTPError, URLError

import html2text
import requests
from bs4 import BeautifulSoup
from telegram import InputMediaPhoto, TelegramError

from priscia import dispatcher
from priscia.modules.disable import DisableAbleCommandHandler

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.38 Safari/537.36"
# useragent = 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36'
opener.addheaders = [("User-agent", useragent)]


def reverse(update, context):
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")

    msg = update.effective_message
    chat_id = update.effective_chat.id
    rtmid = msg.message_id
    args = context.args
    imagename = "okgoogle.png"

    reply = msg.reply_to_message
    if reply:
        if reply.sticker:
            file_id = reply.sticker.file_id
        elif reply.photo:
            file_id = reply.photo[-1].file_id
        elif reply.document:
            file_id = reply.document.file_id
        else:
            msg.reply_text("Reply to an image or sticker to lookup.")
            return
        image_file = context.bot.get_file(file_id)
        image_file.download(imagename)
        if args:
            txt = args[0]
            try:
                lim = int(txt)
            except BaseException:
                lim = 2
        else:
            lim = 2
    elif args:
        splatargs = msg.text.split(" ")
        if len(splatargs) == 3:
            img_link = splatargs[1]
            try:
                lim = int(splatargs[2])
            except BaseException:
                lim = 2
        elif len(splatargs) == 2:
            img_link = splatargs[1]
            lim = 2
        else:
            msg.reply_text("/reverse <link> <amount of images to return.>")
            return
        try:
            urllib.request.urlretrieve(img_link, imagename)
        except HTTPError as HE:
            if HE.reason == "Forbidden":
                msg.reply_text(
                    "Couldn't access the provided link, The website might have blocked accessing to the website by bot or the website does not existed."
                )
                return
            elif HE.reason == "Not Found":
                msg.reply_text("Image not found.")
                return
        except URLError as UE:
            msg.reply_text(f"{UE.reason}")
            return
        except ValueError as VE:
            msg.reply_text(f"{VE}\nPlease try again using http or https protocol.")
            return
    else:
        msg.reply_markdown(
            "Please reply to a sticker, or an image to search it!\nDo you know that you can search an image with a link too? `/reverse [picturelink] <amount>`."
        )
        return

    try:
        searchUrl = "https://www.google.com/searchbyimage/upload"
        multipart = {
            "encoded_image": (imagename, open(imagename, "rb")),
            "image_content": "",
        }
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        fetchUrl = response.headers["Location"]

        if response != 400:
            xx = context.bot.send_message(
                chat_id,
                "Image was successfully uploaded to Google."
                "\nParsing source now. Maybe.",
                reply_to_message_id=rtmid,
            )
        else:
            xx = context.bot.send_message(
                chat_id, "Google told me to go away.", reply_to_message_id=rtmid
            )
            return

        os.remove(imagename)
        match = ParseSauce(fetchUrl + "&hl=en")
        guess = match["best_guess"]
        if match["override"] and match["override"] != "":
            imgspage = match["override"]
        else:
            imgspage = match["similar_images"]

        if guess and imgspage:
            xx.edit_text(
                f"[{guess}]({fetchUrl})\nLooking for images...",
                parse_mode="Markdown",
                disable_web_page_preview=True,
            )
        else:
            xx.edit_text("Couldn't find anything.")
            return

        images = scam(imgspage, lim)
        if len(images) == 0:
            xx.edit_text(
                f"[{guess}]({fetchUrl})\n[Visually similar images]({imgspage})"
                "\nCouldn't fetch any images.",
                parse_mode="Markdown",
            )
            return

        imglinks = []
        for link in images:
            lmao = InputMediaPhoto(media=str(link))
            imglinks.append(lmao)

        context.bot.send_media_group(
            chat_id=chat_id, media=imglinks, reply_to_message_id=rtmid
        )
        xx.edit_text(
            f"[{guess}]({fetchUrl})\n[Visually similar images]({imgspage})",
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )
    except TelegramError as e:
        print(e)
    except Exception as exception:
        print(exception)


def ParseSauce(googleurl):
    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, "html.parser")

    results = {"similar_images": "", "override": "", "best_guess": ""}

    try:
        for bess in soup.findAll("a", {"class": "PBorbe"}):
            url = "https://www.google.com" + bess.get("href")
            results["override"] = url
    except BaseException:
        pass

    for similar_image in soup.findAll("input", {"class": "gLFyf"}):
        url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(
            similar_image.get("value")
        )
        results["similar_images"] = url

    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()

    return results


def scam(imgspage, lim):
    """Parse/Scrape the HTML code for the info we want."""

    single = opener.open(imgspage).read()
    decoded = single.decode("utf-8")
    if int(lim) > 10:
        lim = 10

    imglinks = []
    counter = 0

    pattern = r"^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$"
    oboi = re.findall(pattern, decoded, re.I | re.M)

    for imglink in oboi:
        counter += 1
        imglinks.append(imglink)
        if counter >= int(lim):
            break

    return imglinks


def app(update, context):
    try:
        args = context.args
        app_name = " ".join(args)
        remove_space = app_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get("https://play.google.com/store/search?q=" + final_name + "&c=apps")
        soup = BeautifulSoup(page.content, "lxml", from_encoding="utf-8")
        results = soup.findAll("div", "ZmHEEd")
        app_name = (
            results[0].findNext("div", "Vpfmgd").findNext("div", "WsMG1c nnK0zc").text
        )
        app_dev = results[0].findNext("div", "Vpfmgd").findNext("div", "KoLSrc").text
        app_dev_link = (
            "https://play.google.com"
            + results[0].findNext("div", "Vpfmgd").findNext("a", "mnKHRc")["href"]
        )
        app_rating = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "pf5lIe")
            .find("div")["aria-label"]
        )
        app_link = (
            "https://play.google.com"
            + results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "vU6FJ p63iDd")
            .a["href"]
        )
        app_icon = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "uzcko")
            .img["data-src"]
        )
        app_details = "<a href='" + app_icon + "'>📲&#8203;</a>"
        app_details += " <b>" + app_name + "</b>"
        app_details += (
            "\n\n<code>Developer :</code> <a href='"
            + app_dev_link
            + "'>"
            + app_dev
            + "</a>"
        )
        app_details += "\n<code>Rating :</code> " + app_rating.replace(
            "Rated ", "⭐ "
        ).replace(" out of ", "/").replace(" stars", "", 1).replace(
            " stars", "⭐ "
        ).replace(
            "five", "5"
        )
        app_details += (
            "\n<code>Features :</code> <a href='"
            + app_link
            + "'>View in Play Store</a>"
        )
        update.effective_message.reply_text(app_details, parse_mode="HTML")
    except IndexError:
        update.effective_message.reply_text(
            "No result found in search. Please enter **Valid app name**"
        )
    except Exception as err:
        update.effective_message.reply_text("Exception Occured:- " + str(err))


def google(update, context):
    args = context.args
    query = " ".join(args)
    remove_space = query.split(" ")
    # + " -inurl:(htm|html|php|pls|txt) intitle:index.of \"last modified\" (mkv|mp4|avi|epub|pdf|mp3)"
    input_str = "%20".join(remove_space)
    input_url = "https://bots.shrimadhavuk.me/search/?q={}".format(input_str)
    headers = {"USER-AGENT": "UniBorg"}
    response = requests.get(input_url, headers=headers).json()
    output_str = " "
    for result in response["results"]:
        text = result.get("title")
        url = result.get("url")
        description = result.get("description")
        last = html2text.html2text(description)
        output_str += "[{}]({})\n{}\n".format(text, url, last)
    update.effective_message.reply_text("{}".format(output_str), parse_mode="MARKDOWN")


__help__ = """
Searching, Reversing image. It's Google Stuff!!!

 × /google <query> : Search anything to google.
 × /app <query>: search an Application on Play Store
 × /reverse : Reverse searches image or stickers on google.
"""

__mod_name__ = "Google"

REVERSE_HANDLER = DisableAbleCommandHandler(
    "reverse", reverse, pass_args=True, admin_ok=True
)
APP_HANDLER = DisableAbleCommandHandler("app", app)
GOOGLE_HANDLER = DisableAbleCommandHandler("google", google)

dispatcher.add_handler(REVERSE_HANDLER)
dispatcher.add_handler(APP_HANDLER)
dispatcher.add_handler(GOOGLE_HANDLER)
