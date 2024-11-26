from disnake.ext import commands
from utils.ask_gpt import GPT
from disnake import Message
from os import getenv


class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.admin_ids = list(map(int, getenv("ADMIN_IDS").split(",")))

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.author.bot:
            return

        if message.author.id in self.admin_ids:
            return

        response = await GPT.ask(message.content)

        print(response)

        if response.split(",")[0] == "True":
            await message.delete()
            await message.channel.send(message.author.mention + response.split(",")[1])


def setup(bot: commands.Bot):
    bot.add_cog(Moderation(bot))
