import discord
import os
import views.game_reaction_view as game_reaction_view
import views.continent_reaction_view as continent_reaction_view
import views.counter_side_reaction_view as counterside_reaction_view
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")


class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        prefix = "!"

        super().__init__(command_prefix=prefix, intents=intents)

    async def setup_hook(self) -> None:
        self.add_view(game_reaction_view.GameReactionView())
        self.add_view(continent_reaction_view.ContinentReactionView())

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


bot = PersistentViewBot()


@bot.command()
async def react(ctx: commands.Context):
    if ctx.channel.id == 980416422171799563:
        view = game_reaction_view.GameReactionView()
        react_embed = discord.Embed(title="Welcome, YoRHa units!",
                                    description="You can choose here from a variety of roles that applies to you on your duty as unit inside of the YoRHa guild.\nClick either of the buttons to obtain the role, or click it again to remove it if you're off-duty.",
                                    color=0x000000).set_thumbnail(url="https://i.imgur.com/4fosu5L.png")
        await ctx.send(embed=react_embed, view=view)


@bot.command()
async def continent(ctx: commands.Context):
    if ctx.channel.id == 980416422171799563:
        view = continent_reaction_view.ContinentReactionView()
        react_embed = discord.Embed(title="Where do you strive from, fellow unit?",
                                    description="Please select the region you originated from before attending the Headquarters. \nClick either of the buttons to obtain the role, or click it again to remove it.",
                                    color=0x000000).set_thumbnail(url="https://i.imgur.com/4fosu5L.png")
        await ctx.send(embed=react_embed, view=view)


@bot.command()
async def counterside(ctx: commands.Context):
    if ctx.channel.id == 1005506934973136936:
        view = counterside_reaction_view.CounterSideReactionView()
        react_embed = discord.Embed(title="What applies to you inside of Counter:Side, unit?",
                                    description="Please select the role that you want to help you in your adventure within Counter:Side \nClick either of the buttons to obtain the role, or click it again to remove it.",
                                    color=0x000000).set_thumbnail(url="https://i.imgur.com/4fosu5L.png")
        await ctx.send(embed=react_embed, view=view)

bot.run(token)
