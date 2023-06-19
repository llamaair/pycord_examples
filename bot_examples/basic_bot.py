import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def poll(ctx, reaction1, reaction2, *, poll):
    embed = discord.Embed(title=poll)
    msg = await ctx.send(embed=embed)
    msg.add_reaction(reaction1)
    msg.add_reaction(reaction2)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Unknown command")

bot.run('token')