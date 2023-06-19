import discord

bot = discord.Bot()

@bot.command(description="Ping!")
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(description="Start a poll!")
async def poll(ctx, reaction1, reaction2, poll):
    embed = discord.Embed(title=poll)
    msg = await ctx.send(embed=embed)
    msg.add_reaction(reaction1)
    msg.add_reaction(reaction2)

bot.run('token')