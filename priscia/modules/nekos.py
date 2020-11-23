import nekos
from telegram import ParseMode
from telegram.ext import run_async

from priscia import dispatcher
from priscia.modules.disable import DisableAbleCommandHandler
from priscia.modules.helper_funcs.alternate import typing_action


def nekoimage(update, context, site: str):
    message = update.effective_message
    img = nekos.img(site)
    message.reply_photo(photo=img, caption=site, parse_mode=ParseMode.MARKDOWN)


def nekovideo(update, context, site: str):
    message = update.effective_message
    img = nekos.img(site)
    message.reply_video(video=img, caption=site, parse_mode=ParseMode.MARKDOWN)


def nekodoc(update, context, site: str):
    message = update.effective_message
    img = nekos.img(site)
    message.reply_document(
        document=img, filename=site.jpg, parse_mode=ParseMode.MARKDOWN
    )


@run_async
@typing_action
def pussy(update, context):
    nekoimage(update, context, "pussy_jpg")


@run_async
@typing_action
def hentaig(update, context):
    nekovideo(update, context, "hentaig")


@run_async
@typing_action
def neko(update, context):
    nekodoc(update, context, "neko")


@run_async
@typing_action
def feet(update, context):
    nekoimage(update, context, "feet")


@run_async
@typing_action
def yuri(update, context):
    nekoimage(update, context, "yuri")


@run_async
@typing_action
def trap(update, context):
    nekoimage(update, context, "trap")


@run_async
@typing_action
def futunari(update, context):
    nekoimage(update, context, "futunari")


@run_async
@typing_action
def hololewd(update, context):
    nekoimage(update, context, "hololewd")


@run_async
@typing_action
def lewdkemo(update, context):
    nekoimage(update, context, "lewdkemo")


@run_async
@typing_action
def solog(update, context):
    nekovideo(update, context, "solog")


@run_async
@typing_action
def feetg(update, context):
    nekovideo(update, context, "feetg")


@run_async
@typing_action
def cumgif(update, context):
    nekovideo(update, context, "cum")


@run_async
@typing_action
def erokemo(update, context):
    nekoimage(update, context, "erokemo")


@run_async
@typing_action
def lesbian(update, context):
    nekoimage(update, context, "les")


@run_async
@typing_action
def wallpaper(update, context):
    nekodoc(update, context, "wallpaper")


@run_async
@typing_action
def lewdk(update, context):
    nekoimage(update, context, "lewdk")


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
def lewd(update, context):
    nekoimage(update, context, "lewd")


@run_async
@typing_action
def feed(update, context):
    nekoimage(update, context, "feed")


@run_async
@typing_action
def eroyuri(update, context):
    nekoimage(update, context, "eroyuri")


@run_async
@typing_action
def eron(update, context):
    nekoimage(update, context, "eron")


@run_async
@typing_action
def cum(update, context):
    nekoimage(update, context, "cum_jpg")


@run_async
@typing_action
def bjgif(update, context):
    nekovideo(update, context, "bj")


@run_async
@typing_action
def bj(update, context):
    nekoimage(update, context, "blowjob")


@run_async
@typing_action
def nekonsfw(update, context):
    nekovideo(update, context, "neko_nsfw_gif")


@run_async
@typing_action
def solo(update, context):
    nekoimage(update, context, "solo")


@run_async
@typing_action
def kemonomimi(update, context):
    nekoimage(update, context, "kemonomimi")


@run_async
@typing_action
def pokegif(update, context):
    nekovideo(update, context, "poke")


@run_async
@typing_action
def analgif(update, context):
    nekovideo(update, context, "anal")


@run_async
@typing_action
def hentai(update, context):
    nekoimage(update, context, "hentai")


@run_async
@typing_action
def erofeet(update, context):
    nekoimage(update, context, "erofeet")


@run_async
@typing_action
def holo(update, context):
    nekoimage(update, context, "holo")


@run_async
@typing_action
def pussygif(update, context):
    nekovideo(update, context, "pussy")


@run_async
@typing_action
def tits(update, context):
    nekoimage(update, context, "tits")


@run_async
@typing_action
def holoero(update, context):
    nekoimage(update, context, "holoero")


@run_async
@typing_action
def classic(update, context):
    nekovideo(update, context, "classic")


@run_async
@typing_action
def kuni(update, context):
    nekovideo(update, context, "kuni")


__help__ = """
Get images from [Nekos API](nekos.life)
× /pussy   × /hentaig   × /neko   × /feet   × /yuri
× /trap   × futunari   × /hololewd   × /lewdkemo
× /solog   × feetg   × /cumgif   × /erokemo   × /lesbian
× /wallpaper   × lewdk   × /ngif   × /tickle   × /lewd
× /feed   × /eroyuri   × /eron   × /cum   × /bjgif
× /bj   × /nekonsfw   × /solo   × /kemonomimi   × pokegif
× /analgif   × /hentai   × /erofeet   × /holo   × /pussygif
× /tits   × /holoero   × /classic   × /kuni
"""

__modname__ = "Nekos"

PUSSY_HANDLER = DisableAbleCommandHandler("pussy", pussy)
HENTAIG_HANDLER = DisableAbleCommandHandler("hentaig", hentaig)
NEKO_HANDLER = DisableAbleCommandHandler("neko", neko)
FEET_HANDLER = DisableAbleCommandHandler("feet", feet)
YURI_HANDLER = DisableAbleCommandHandler("yuri", yuri)
TRAP_HANDLER = DisableAbleCommandHandler("trap", trap)
FUTUNARI_HANDLER = DisableAbleCommandHandler("futunari", futunari)
HOLOLEWD_HANDLER = DisableAbleCommandHandler("hololewd", hololewd)
LEWDKEMO_HANDLER = DisableAbleCommandHandler("lewdkemo", lewdkemo)
SOLOG_HANDLER = DisableAbleCommandHandler("solog", solog)
FEETG_HANDLER = DisableAbleCommandHandler("feetg", feetg)
CUMGIF_HANDLER = DisableAbleCommandHandler("cumgif", cumgif)
EROKEMO_HANDLER = DisableAbleCommandHandler("erokemo", erokemo)
LESBIAN_HANDLER = DisableAbleCommandHandler("lesbian", lesbian)
WALLPAPER_HANDLER = DisableAbleCommandHandler("wallpaper", wallpaper)
LEWDK_HANDLER = DisableAbleCommandHandler("lewdk", lewdk)
NGIF_HANDLER = DisableAbleCommandHandler("ngif", ngif)
TICKLE_HANDLER = DisableAbleCommandHandler("tickle", tickle)
LEWD_HANDLER = DisableAbleCommandHandler("lewd", lewd)
FEED_HANDLER = DisableAbleCommandHandler("feed", feed)
EROYURI_HANDLER = DisableAbleCommandHandler("eroyuri", eroyuri)
ERON_HANDLER = DisableAbleCommandHandler("eron", eron)
CUM_HANDLER = DisableAbleCommandHandler("cum", cum)
BJGIF_HANDLER = DisableAbleCommandHandler("bjgif", bjgif)
BJ_HANDLER = DisableAbleCommandHandler("bj", bj)
NEKONSFW_HANDLER = DisableAbleCommandHandler("nekonsfw", nekonsfw)
SOLO_HANDLER = DisableAbleCommandHandler("solo", solo)
KEMONOMIMI_HANDLER = DisableAbleCommandHandler("kemonomimi", kemonomimi)
POKEGIF_HANDLER = DisableAbleCommandHandler("pokegif", pokegif)
ANALGIF_HANDLER = DisableAbleCommandHandler("analgif", analgif)
HENTAI_HANDLER = DisableAbleCommandHandler("hentai", hentai)
EROFEET_HANDLER = DisableAbleCommandHandler("erofeet", erofeet)
HOLO_HANDLER = DisableAbleCommandHandler("holo", holo)
PUSSYGIF_HANDLER = DisableAbleCommandHandler("pussygif", pussygif)
TITS_HANDLER = DisableAbleCommandHandler("tits", tits)
HOLOERO_HANDLER = DisableAbleCommandHandler("holoero", holoero)
CLASSIC_HANDLER = DisableAbleCommandHandler("classic", classic)
KUNI_HANDLER = DisableAbleCommandHandler("kuni", kuni)

dispatcher.addhandler(PUSSY_HANDLER)
dispatcher.addhandler(HENTAIG_HANDLER)
dispatcher.addhandler(NEKO_HANDLER)
dispatcher.addhandler(FEET_HANDLER)
dispatcher.addhandler(YURI_HANDLER)
dispatcher.addhandler(TRAP_HANDLER)
dispatcher.addhandler(FUTUNARI_HANDLER)
dispatcher.addhandler(HOLOLEWD_HANDLER)
dispatcher.addhandler(LEWDKEMO_HANDLER)
dispatcher.addhandler(SOLOG_HANDLER)
dispatcher.addhandler(FEETG_HANDLER)
dispatcher.addhandler(CUMGIF_HANDLER)
dispatcher.addhandler(EROKEMO_HANDLER)
dispatcher.addhandler(LESBIAN_HANDLER)
dispatcher.addhandler(WALLPAPER_HANDLER)
dispatcher.addhandler(LEWDK_HANDLER)
dispatcher.addhandler(NGIF_HANDLER)
dispatcher.addhandler(TICKLE_HANDLER)
dispatcher.addhandler(LEWD_HANDLER)
dispatcher.addhandler(FEED_HANDLER)
dispatcher.addhandler(EROYURI_HANDLER)
dispatcher.addhandler(ERON_HANDLER)
dispatcher.addhandler(CUM_HANDLER)
dispatcher.addhandler(BJGIF_HANDLER)
dispatcher.addhandler(BJ_HANDLER)
dispatcher.addhandler(NEKONSFW_HANDLER)
dispatcher.addhandler(SOLO_HANDLER)
dispatcher.addhandler(KEMONOMIMI_HANDLER)
dispatcher.addhandler(POKEGIF_HANDLER)
dispatcher.addhandler(ANALGIF_HANDLER)
dispatcher.addhandler(HENTAI_HANDLER)
dispatcher.addhandler(EROFEET_HANDLER)
dispatcher.addhandler(HOLO_HANDLER)
dispatcher.addhandler(PUSSYGIF_HANDLER)
dispatcher.addhandler(TITS_HANDLER)
dispatcher.addhandler(HOLOERO_HANDLER)
dispatcher.addhandler(CLASSIC_HANDLER)
dispatcher.addhandler(KUNI_HANDLER)
