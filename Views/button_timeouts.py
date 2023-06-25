import discord

class MyView(discord.ui.View):
    async def on_timeout(self):
        self.disable_all_items()
        await self.message.edit(content="This button is now disabled!", view=self)
    
    @discord.ui.button()
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("This is an interaction response")

bot = discord.Bot()

@bot.command()
async def button(ctx):
    await ctx.respond("Press this button!", view=MyView(timeout=30))