import datetime
import json

import requests
from telegram import ParseMode

from priscia import dispatcher
from priscia.modules.disable import DisableAbleCommandHandler


def dot(number, thousand_separator="."):
    def reverse(string):
        string = "".join(reversed(string))
        return string

    s = reverse(str(number))
    count = 0
    result = ""
    for char in s:
        count = count + 1
        if count % 3 == 0:
            if len(s) == count:
                result = char + result
            else:
                result = thousand_separator + char + result
        else:
            result = char + result
    return result


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
    try:
        json_date = case["updated"]
    except KeyError:
        message.reply_text("Make sure you have input correct country")
        return
    float_date = float(json_date) / 1000.0
    date = datetime.datetime.fromtimestamp(float_date).strftime("%d %b %Y %I:%M:%S %p")
    try:
        flag = case["countryInfo"]["flag"]
    except KeyError:
        flag = []
    if flag:
        text = f"*COVID-19 Statistics in* [{query}]({flag})\n"
    else:
        text = f"*COVID-19 Statistics in {country} :*\n"
    text += f"Last Updated on `{date} GMT`\n\n🔼 Confirmed Cases : `{dot(case['cases'])}` | `+{dot(case['todayCases'])}`\n🔺 Active Cases : `{dot(case['active'])}`\n⚰️ Deaths : `{dot(case['deaths'])}` | `+{dot(case['todayDeaths'])}`\n💹 Recovered Cases: `{dot(case['recovered'])}` | `+{dot(case['todayRecovered'])}`\n💉 Total Tests : `{dot(case['tests'])}`\n👥 Populations : `{dot(case['population'])}`\n🌐 Source : worldometers"
    try:
        message.reply_text(text, parse_mode=ParseMode.MARKDOWN)
    except Exception:
        message.reply_text("Try again in few times, maybe API are go down")


__help__ = """
2020 are disaster year :( and now, 2021 are 2020 Season II

 × /covid <country>: Get information about COVID-19 Country Stats
 × /covid : Get information about COVID-19 World Stats
"""

__mod_name__ = "Covid"

COVID_HANDLER = DisableAbleCommandHandler("covid", covid)

dispatcher.add_handler(COVID_HANDLER)
