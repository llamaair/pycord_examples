# Pre-disabled buttons example:

import discord

class MyView(discord.ui.View):
    @discord.ui.button(label="Button", style=discord.Button.primary, disabled=True)
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("This button is disabled, so this won't work")

# Disabling buttons on press

class MyView(discord.ui.View):
    @discord.ui.button(label="Button", style=discord.ButtonStyle.success)
    async def button_callback(self, button, interaction):
        button.disabled=True
        button.label="Disabled"
        await interaction.response.edit_message(view=self)