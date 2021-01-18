import datetime
import json

import requests
from telegram import ParseMode

from priscia import dispatcher
from priscia.modules.disable import DisableAbleCommandHandler


def covid(update, context):
    message = update.effective_message
    args = context.args
    query = " ".join(args)
    remove_space = query.split(" ")
    country = "%20".join(remove_space)
    if not country:
        url = "https://disease.sh/v3/covid-19/all?yesterday=false&twoDaysAgo=false&allowNull=true"
        country = "World"
    else:
        url = f"https://disease.sh/v3/covid-19/countries/{country}?yesterday=false&twoDaysAgo=false&strict=true&allowNull=true"
    request = requests.get(url).text
    case = json.loads(request)
    json_date = case["updated"]
    float_date = float(json_date) / 1000.0
    date = datetime.datetime.fromtimestamp(float_date).strftime("%d %b %Y %I:%M:%S %p")
    try:
        flag = case["countryInfo"]["flag"]
    except KeyError:
        pass
    text = f"*COVID-19 Statistics in {country} :*\n📅 Last Updated on {date}\n\n🔼 Confirmed Cases : `{case['cases']}` `+{case['todayCases']}` on today\n🔺 Active Cases : `{case['active']}`\n⚰️ Deaths : `{case['deaths']}` `+{case['todayDeaths']}` on today\n💹 Recovered Cases: `{case['recovered']}` `+{case['todayRecovered']}` on today\n💉 Total Tests : `{case['tests']}`\n👥 Populations : `{case['population']}`\n🌐 Source : worldometers"
    try:
        message.reply_photo(photo=flag, caption=text, parse_mode=ParseMode.MARKDOWN)
    except BaseException:
        message.reply_text(text, parse_mode=ParseMode.MARKDOWN)


__help__ = """
2020 are disaster year :( and now, 2021 are 2020 Season II

 × /covid <country>: Get information about COVID-19 Country Stats
 × /covid : Get information about COVID-19 World Stats
"""

__mod_name__ = "Covid"

COVID_HANDLER = DisableAbleCommandHandler("covid", covid)

dispatcher.add_handler(COVID_HANDLER)
