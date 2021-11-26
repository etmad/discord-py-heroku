import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):
    async def on_message(self, message):
        print(f"MSG FROM as {message.author.name})")
        if message.author.name == "AreYouReady":
            print("CXC")

    async def on_ready():
        print(f"Logged in as {self.user.name}({self.user.id})")

if __name__ == "__main__":
    client = MyClient()
    MyClient.run(TOKEN)
