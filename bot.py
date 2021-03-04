import requests
import discord
from discord.ext import commands


client = commands.Bot(command_prefix="?")


@client.event
async def on_ready():
    print("loaded")


@client.command()
async def balance(ctx, name, pname):
    r = requests.session()
    api = r.get("https://sky.shiiyu.moe/api/v2/coins/" + name + "/" + pname).json()
    embed = discord.Embed(
        title="Balance for " + name + " " + "on profile " + pname,
        color=discord.Colour.blue()
    )
    embed.set_thumbnail(url="https://mc-heads.net/avatar/" + name)
    embed.add_field(name="**Purse**", value="$" + str(api["purse"]))
    embed.add_field(name="**Bank**", value="$" + str(api["bank"]))
    await ctx.send(embed=embed)


@client.command()
async def slayers(ctx, name, pname):
    api = requests.get("https://sky.shiiyu.moe/api/v2/slayers/" + name + "/" + pname).json()
    embed = discord.Embed(
        title="Slayer Information for " + name,
        description="**Total slayer EXP:** " + str(api["slayer_xp"]),
        color=discord.Colour.red()
    )
    embed.set_thumbnail(url="https://mc-heads.net/avatar/" + name)
    embed.add_field(name="**Revenent Horror**", value="Level " + str(api["slayers"]["zombie"]["level"]["currentLevel"]))
    embed.add_field(name="**Tarantula Broodfather**", value="Level " + str(api["slayers"]["spider"]["level"]["currentLevel"]))
    embed.add_field(name="**Sven Packmaster**", value="Level " + str(api["slayers"]["wolf"]["level"]["currentLevel"]))
    await ctx.send(embed=embed)


@client.command()
async def dungeons(ctx, name, pname):
    api = requests.get("https://sky.shiiyu.moe/api/v2/dungeons/" + name + "/" + pname).json()
    embed = discord.Embed(
        title="Dungeon Stats For " + name + " " "On Profile " + pname,
        description="**Total Dungeon EXP:** " + (str(round(api["dungeons"]["catacombs"]["level"]["xp"], 3))),
        color=discord.Colour.blurple()
    )
    embed.set_thumbnail(url="https://mc-heads.net/avatar/" + name)
    embed.add_field(name="**Catacombs Level**", value=str(api["dungeons"]["catacombs"]["level"]["level"]))
    embed.add_field(name="**EXP Until Next Level**", value=str(api["dungeons"]["catacombs"]["level"]["xpForNext"]))
    embed.add_field(name="**Highest Floor**", value=str(api["dungeons"]["catacombs"]["highest_floor"]).replace("_", " ").replace("f", "F"))
    embed.add_field(name="**Healer**", value="Level: " + str(api["dungeons"]["classes"]["healer"]["experience"]["level"]))
    embed.add_field(name="**Mage**", value="Level: " + str(api["dungeons"]["classes"]["mage"]["experience"]["level"]))
    embed.add_field(name="**Tank**", value="Level: " + str(api["dungeons"]["classes"]["tank"]["experience"]["level"]))
    embed.add_field(name="**Berserk**", value="Level: " + str(api["dungeons"]["classes"]["berserk"]["experience"]["level"]))
    embed.add_field(name="**Archer**", value="Level: " + str(api["dungeons"]["classes"]["archer"]["experience"]["level"]))
    await ctx.send(embed=embed)


Token = client.run("MzY3MDY5ODM4NzQyNTE5ODA4.WdvybQ.OAPTwwoBSXGtGDVKwFU3_454S8M")
