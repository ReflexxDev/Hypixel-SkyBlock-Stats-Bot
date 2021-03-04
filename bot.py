import requests
import discord
from discord.ext import commands
import time
from bs4 import BeautifulSoup


client = commands.Bot(command_prefix="?")
user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"}  # enter user agent here


async def on_ready():
    print("Loaded")


@client.command()
async def monitor(ctx, url, price):
    r = requests.session()
    page = r.get(url, headers=user_agent)
    soup = BeautifulSoup(page.content, "html.parser")

    product = {
        "Title": soup.find("h1", {"class": "name"}).text,
        "Last Sale": soup.find("div", {"class": "sale-value"}).text.replace("£", ""),
        }

    await ctx.send("***Monitoring Price For:***" + " " + product["Title"])

    embed = discord.Embed(
        title="Price Increase Has Met Criteria",
        color=discord.Colour.blue()
    )

    while True:
        r.get(url, headers=user_agent)

        if int(product["Last Sale"]) >= int(price):
            embed.add_field(name="***Name:***", value=product["Title"], inline=False)
            embed.add_field(name="***Last Sale:***", value="£" + product["Last Sale"], inline=False)
            embed.add_field(name="***Url:***" + " ", value=url, inline=True)
            await ctx.send(embed=embed)
            break
        else:
            print("Monitoring Price")
            time.sleep(3)


client.run("MzY3MDY5ODM4NzQyNTE5ODA4.WdvybQ.OAPTwwoBSXGtGDVKwFU3_454S8M")  # enter bot token here

