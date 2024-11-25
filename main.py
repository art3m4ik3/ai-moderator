from disnake.ext import commands
from dotenv import load_dotenv
from os import getenv, listdir
import disnake

load_dotenv()


class Client(commands.AutoShardedInteractionBot):
    def __init__(self):
        super().__init__(intents=disnake.Intents.all())

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}")

        for filename in listdir("cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"cogs.{filename[:-3]}")
                print(f"Loaded extension {filename[:-3]}")


if __name__ == "__main__":
    client = Client()
    client.run(getenv("TOKEN"))
