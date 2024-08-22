import discord
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import flip_coin_f
from bot_logic import gen_emojis
from settings import settings

prefix = settings["Prefix"]
commands_list = ["cmds", "hello", "bye", "random_password", "random_emoji", "flip_coin"]
commands_desc = {
    "cmds" : "Sends all the available commands.",
    "hello" : "Responds with: Hi.",
    "bye" : "Responds with: Bye.",
    "random_password" : "Generates a random password.",
    "random_emoji" : "Generates a random emoji.",
    "flip_coin" : "Flips a coin."
}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def cmds(ctx):
    send = ""
    for i in commands_list:
        send += f"```css\n[{i}]: {commands_desc[i]}\n```"
    await ctx.send("```yaml\n Prefix: " + prefix + "\n```\n" + send)

@bot.command()
async def hello(ctx):
    await ctx.send(f'<:yes:1273791797797326949> Hello {ctx.author.mention}!')

@bot.command()
async def bye(ctx):
    await ctx.send(f'<:yes:1273791797797326949> Bye {ctx.author.mention}!')

@bot.command()
async def random_password(ctx, length: int = 20):
    await ctx.send(gen_pass(length))

@bot.command()
async def random_emoji(ctx):
    await ctx.send(gen_emojis())

@bot.command()
async def flip_coin(ctx):
    await ctx.send(flip_coin_f())

bot.run(settings["Token"])
