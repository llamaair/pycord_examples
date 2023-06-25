import discord

class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Short input"))
        self.add_item(discord.ui.InputText(label="Long input", style=discord.InputTextStyle.long))
    
    async def callback(self, interaction:discord.Interaction):
        await interaction.response.send_message(f"Your short input was {self.children[0].value} and your long was {self.children[1].value}")

client = discord.Bot(intents=discord.Intents.all())

class ModalButton(discord.ui.View):
    @discord.ui.button(label="Send modal!", style=discord.ButtonStyle.success)
    async def button_callback(self, button, interaction):
        await interaction.response.send_modal(MyModal(title="Modal via button"))

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")

@client.command(description="Command to send modal")
async def sendmodal(ctx):
    await ctx.respond(view=ModalButton())

client.run("token")