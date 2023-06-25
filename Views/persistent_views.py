import discord

client = discord.Client()

class MyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="I am a button", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("Button was pressed")

@client.event
async def on_ready():
    client.add_view(MyView())

@client.command()
async def button(ctx):
    await ctx.respond("Press the button!", view=MyView())

client.run("token")