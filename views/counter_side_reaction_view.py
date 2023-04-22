import discord
from . import helpers as manage


class CounterSideReactionView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Raid Support", style=discord.ButtonStyle.primary, emoji="<:quartz:978911785874767923>", custom_id="raid_support")
    async def add_raid_support_role(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = discord.utils.find(
            lambda g: g.id == interaction.user.guild.id, interaction.user.mutual_guilds)
        role = discord.utils.get(guild.roles, id=980415886945042442)
        await manage.manage_user.manage_user_roles(interaction, role)

    @discord.ui.button(label="Daily Reset", style=discord.ButtonStyle.primary, emoji="♻️", custom_id="daily_reset")
    async def add_daily_reset_role(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = discord.utils.find(
            lambda g: g.id == interaction.user.guild.id, interaction.user.mutual_guilds)
        role = discord.utils.get(guild.roles, id=980542306660798466)
        await manage.manage_user.manage_user_roles(interaction, role)
