import os
from discord.ext import commands

bot = commands.Bot(command_prefix="")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.listen()
async def on_message(message):
    print(f"Message from in as {message.author.name}({message.content})")
    if message.author.name == "AreYouReady" or message.author.name == "GrigorySkovoroda":
        await message.channel.send(f"@{message.author.name} :sosiblue:")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

if __name__ == "__main__":
    bot.run(TOKEN)
