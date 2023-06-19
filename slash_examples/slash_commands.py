import discord

bot = discord.Bot()

@bot.slash_command(name="ping")
async def ping(ctx:discord.ApplicationContext):
    """Ping!"""
    await ctx.respond("Pong!")

@bot.slash_command(name="joined")
async def joined(ctx:discord.ApplicationContext, member:discord.Member=None):
    user = member or ctx.author
    await ctx.respond(f"{user.name} joiend at {discord.utils.format_dt(user.joined_at)}")

bot.run('token')