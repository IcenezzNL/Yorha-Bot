import discord


async def manage_user_roles(interaction: discord.Interaction, role: discord.Role):
    for x in interaction.user.roles:
        if x.id == role.id:
            await interaction.user.remove_roles(role)
            message = f"Successfully removed the role: {role.name} from you."
            embed = discord.Embed(
                title="Succesfully added role", description=message, color=0x00ff00).set_thumbnail(
                url="https://i.imgur.com/4fosu5L.png")
            await interaction.response.send_message(embed=embed, ephemeral=True, delete_after=5)
            return

    await interaction.user.add_roles(role)
    message = f"Successfully added the role: {role.name} to you."
    embed = discord.Embed(
        title="Succesfully added role", description=message, color=0x00ff00).set_thumbnail(
        url="https://i.imgur.com/4fosu5L.png")
    await interaction.response.send_message(embed=embed, ephemeral=True, delete_after=5)
