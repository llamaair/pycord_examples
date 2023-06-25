import discord

class MyView(discord.ui.View):
    @discord.ui.Select(
        placeholder="Choose a color!",
        min_values = 1,
        max_values = 1,
        options=[
            discord.SelectOption(
                label="Red",
                description="Click this if you like the color Red"
            ),
            discord.SelectOption(
                label="Blue",
                description="Click this if you like the color Blue"
            ),
            discord.SelectOption(
                label="Purple",
                description="Click this if you like the color purple"
            )
        ]
    )
    async def select_callback(self, select, interaction):
        await interaction.response.send_message(f"You picked the color {select.values[0]}!")

bot = discord.Bot()

@bot.command()
async def color(ctx):
    await ctx.respond("Pick a color!", view=MyView())

bot.run("token")