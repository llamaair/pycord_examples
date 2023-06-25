import discord

bot = discord.Bot()

class MyView(discord.ui.View):
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎")
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!")

@bot.command()
async def button(ctx):
    await ctx.respond("This is a button!", view=MyView())

bot.run("token")