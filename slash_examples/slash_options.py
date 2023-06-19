import discord
from discord import option

bot = discord.Bot()

@bot.slash_command()
@option("name", description="Enter your name")
@option("gender", description="Choose your gender", choices=["Male", "Female", "Other"])
@option("age", description="Enter your age", min_value=13, max_value=99, default=18, required=False)
async def hi(ctx:discord.ApplicationContext, name:str, gender:str, age:int):
    await ctx.respond(f"Hey there {name}. Your gender is {gender} and you are {age} years old :slight_smile:", ephemeral=True)

@bot.slash_command(name="attach_file")
@option("attachment", discord.Attachment, description="A file to attach to the message")
async def file(ctx:discord.ApplicationContext, attachment:discord.Attachment):
    """How to attach a file with a slash command"""
    file = await attachment.to_file()
    await ctx.respond("Here's your file!", file=file)

bot.run('token')