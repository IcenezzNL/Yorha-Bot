import discord
from . import helpers as manage


class GameReactionView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Counter:Side Guild", style=discord.ButtonStyle.primary, emoji="<a:hildehyper:978913619704184862>", custom_id="counterside")
    async def add_first_role(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = discord.utils.find(
            lambda g: g.id == interaction.user.guild.id, interaction.user.mutual_guilds)
        role = discord.utils.get(guild.roles, id=1005501928320553030)
        await manage.manage_user.manage_user_roles(interaction, role)

    @discord.ui.button(label="Honkai: Star Rail", style=discord.ButtonStyle.primary, emoji="<:2bdesire:1099287334266089543>", custom_id="starrail")
    async def add_second_role(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = discord.utils.find(
            lambda g: g.id == interaction.user.guild.id, interaction.user.mutual_guilds)
        role = discord.utils.get(guild.roles, id=1099422137237909575)
        await manage.manage_user.manage_user_roles(interaction, role)
