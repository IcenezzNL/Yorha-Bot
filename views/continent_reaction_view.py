import discord
from . import helpers as manage


class ContinentReactionView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Europe", style=discord.ButtonStyle.primary, emoji="🇪🇺", custom_id="Europe")
    async def add_europe_role(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = discord.utils.find(
            lambda g: g.id == interaction.user.guild.id, interaction.user.mutual_guilds)
        role = discord.utils.get(guild.roles, id=1005531319574462586)
        await manage.manage_user.manage_user_roles(interaction, role)

    @discord.ui.button(label="North America", style=discord.ButtonStyle.primary, emoji="🇺🇸", custom_id="North America")
    async def add_north_america_role(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = discord.utils.find(
            lambda g: g.id == interaction.user.guild.id, interaction.user.mutual_guilds)
        role = discord.utils.get(guild.roles, id=1005531554073817088)
        await manage.manage_user.manage_user_roles(interaction, role)

    @discord.ui.button(label="South America", style=discord.ButtonStyle.primary, emoji="🌎", custom_id="South America")
    async def add_south_america_role(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = discord.utils.find(
            lambda g: g.id == interaction.user.guild.id, interaction.user.mutual_guilds)
        role = discord.utils.get(guild.roles, id=1005531660890152980)
        await manage.manage_user.manage_user_roles(interaction, role)

    @discord.ui.button(label="South East Asia", style=discord.ButtonStyle.primary, emoji="🗾", custom_id="South East Asia")
    async def add_sea_role(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = discord.utils.find(
            lambda g: g.id == interaction.user.guild.id, interaction.user.mutual_guilds)
        role = discord.utils.get(guild.roles, id=1005531731308322966)
        await manage.manage_user.manage_user_roles(interaction, role)

    @discord.ui.button(label="Asian-Pacific", style=discord.ButtonStyle.primary, emoji="🌏", custom_id="United States")
    async def add_asian_pacific_role(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = discord.utils.find(
            lambda g: g.id == interaction.user.guild.id, interaction.user.mutual_guilds)
        role = discord.utils.get(guild.roles, id=1005531844734890015)
        await manage.manage_user.manage_user_roles(interaction, role)
