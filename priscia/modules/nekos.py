import nekos
from telegram import ParseMode
from telegram.ext import run_async

from priscia import dispatcher
from priscia.modules.disable import DisableAbleCommandHandler
from priscia.modules.helper_funcs.alternate import typing_action


def nekoimage(update, context, site: str):
    message = update.effective_message
    img = nekos.img(site)
    message.reply_photo(photo=img, parse_mode=ParseMode.MARKDOWN)


def nekovideo(update, context, site: str):
    message = update.effective_message
    img = nekos.img(site)
    message.reply_video(video=img, parse_mode=ParseMode.MARKDOWN)


def nekodoc(update, context, site: str):
    message = update.effective_message
    img = nekos.img(site)
    message.reply_document(document=img, parse_mode=ParseMode.MARKDOWN)


@run_async
@typing_action
def neko(update, context):
    nekodoc(update, context, "neko")


@run_async
@typing_action
def erokemo(update, context):
    nekoimage(update, context, "erokemo")


@run_async
@typing_action
def wallpaper(update, context):
    nekodoc(update, context, "wallpaper")


@run_async
@typing_action
def ngif(update, context):
    nekovideo(update, context, "ngif")


@run_async
@typing_action
def tickle(update, context):
    nekoimage(update, context, "tickle")


@run_async
@typing_action
def feed(update, context):
    nekoimage(update, context, "feed")


@run_async
@typing_action
def eroneko(update, context):
    nekoimage(update, context, "eron")


@run_async
@typing_action
def nekonsfw(update, context):
    nekovideo(update, context, "nsfw_neko_gif")


@run_async
@typing_action
def kemonomimi(update, context):
    nekoimage(update, context, "kemonomimi")


@run_async
@typing_action
def poke(update, context):
    nekovideo(update, context, "poke")


@run_async
@typing_action
def avatar(update, context):
    nekoimage(update, context, "avatar")


@run_async
@typing_action
def pwankg(update, context):
    nekovideo(update, context, "pwankg")


@run_async
@typing_action
def waifu(update, context):
    nekoimage(update, context, "waifu")


@run_async
@typing_action
def pat(update, context):
    nekovideo(update, context, "pat")


@run_async
@typing_action
def cuddle(update, context):
    nekovideo(update, context, "cuddle")


@run_async
@typing_action
def foxgirl(update, context):
    nekovideo(update, context, "fox_girls")


@run_async
@typing_action
def hug(update, context):
    nekovideo(update, context, "hug")


@run_async
@typing_action
def smug(update, context):
    nekovideo(update, context, "smug")


@run_async
@typing_action
def goose(update, context):
    nekovideo(update, context, "goose")


@run_async
@typing_action
def baka(update, context):
    nekovideo(update, context, "baka")


@run_async
@typing_action
def woof(update, context):
    nekovideo(update, context, "woof")


__help__ = """
Get images from [Nekos API](nekos.life)
× /neko × /erokemo × /wallpaper × /ngif × /tickle
× /feed × /eron × /nekonsfw × /kemonomimi × /poke
× /avatar × /pwankg × /waifu × /pat × /cuddle
× /foxgirl × /hug × /smug × /goose × /baka × /woof
"""

__mod_name__ = "Nekos"

NEKO_HANDLER = DisableAbleCommandHandler("neko", neko)
EROKEMO_HANDLER = DisableAbleCommandHandler("erokemo", erokemo)
WALLPAPER_HANDLER = DisableAbleCommandHandler("wallpaper", wallpaper)
NGIF_HANDLER = DisableAbleCommandHandler("ngif", ngif)
TICKLE_HANDLER = DisableAbleCommandHandler("tickle", tickle)
FEED_HANDLER = DisableAbleCommandHandler("feed", feed)
ERONEKO_HANDLER = DisableAbleCommandHandler("eroneko", eroneko)
NEKONSFW_HANDLER = DisableAbleCommandHandler("nekonsfw", nekonsfw)
KEMONOMIMI_HANDLER = DisableAbleCommandHandler("kemonomimi", kemonomimi)
POKE_HANDLER = DisableAbleCommandHandler("poke", poke)
AVATAR_HANDLER = DisableAbleCommandHandler("avatar", avatar)
PWANKG_HANDLER = DisableAbleCommandHandler("pwankg", pwankg)
WAIFU_HANDLER = DisableAbleCommandHandler("waifu", waifu)
PAT_HANDLER = DisableAbleCommandHandler("pat", pat)
CUDDLE_HANDLER = DisableAbleCommandHandler("cuddle", cuddle)
FOXGIRL_HANDLER = DisableAbleCommandHandler("foxgirl", foxgirl)
HUG_HANDLER = DisableAbleCommandHandler("hug", hug)
SMUG_HANDLER = DisableAbleCommandHandler("smug", smug)
GOOSE_HANDLER = DisableAbleCommandHandler("goose", goose)
BAKA_HANDLER = DisableAbleCommandHandler("baka", baka)
WOOF_HANDLER = DisableAbleCommandHandler("woof", woof)

dispatcher.add_handler(NEKO_HANDLER)
dispatcher.add_handler(EROKEMO_HANDLER)
dispatcher.add_handler(WALLPAPER_HANDLER)
dispatcher.add_handler(NGIF_HANDLER)
dispatcher.add_handler(TICKLE_HANDLER)
dispatcher.add_handler(FEED_HANDLER)
dispatcher.add_handler(ERONEKO_HANDLER)
dispatcher.add_handler(NEKONSFW_HANDLER)
dispatcher.add_handler(KEMONOMIMI_HANDLER)
dispatcher.add_handler(POKE_HANDLER)
dispatcher.add_handler(AVATAR_HANDLER)
dispatcher.add_handler(PWANKG_HANDLER)
dispatcher.add_handler(WAIFU_HANDLER)
dispatcher.add_handler(PAT_HANDLER)
dispatcher.add_handler(CUDDLE_HANDLER)
dispatcher.add_handler(FOXGIRL_HANDLER)
dispatcher.add_handler(HUG_HANDLER)
dispatcher.add_handler(SMUG_HANDLER)
dispatcher.add_handler(GOOSE_HANDLER)
dispatcher.add_handler(BAKA_HANDLER)
dispatcher.add_handler(WOOF_HANDLER)
