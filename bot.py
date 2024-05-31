import io
import discord
import aiohttp
from discord.ext import commands

from cpi import ask_gaianet
from button import PlayView



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
@commands.has_permissions(administrator=True)
async def synccommands(ctx):
    await bot.tree.sync()
    await ctx.send('sync commands finnish')

@bot.hybrid_command()
async def start(ctx):
    image_url = "https://postimg.cc/jwFbWCYT"

    welcome_message = '''Hey MUA fam!  Welcome aboard! Feel free to @mua42bot with any questions about MUA DAO. 

We're here to build, HODL, and have a blast together. Dive in, get involved, and let's create more Mua~ Mua~ miracles! '''
    # await ctx.send(file=image_url)
    # async with aiohttp.ClientSession() as session: # creates session
    #     async with session.get(image_url) as resp: # gets image from url
    #         img = await resp.read() # reads image from response
    #         with io.BytesIO(img) as file: # converts to file-like object
    #             await ctx.send(file=discord.File(file, "testimage.png"))
    #file = discord.File("/Users/gaopenghao/Downloads/rust项目/discord_bot_muadao/muadao.jpg", filename="output.png")
    new_embed = discord.Embed()
    new_embed.set_image(url = image_url)
    await ctx.send(embed = new_embed)
    await ctx.send(welcome_message, view = PlayView())

@bot.command()
async def query(ctx, message): # message这部分也需要改进
    res = await ask_gaianet("muadao", message)
    print(message)
    url_suffix= f'''\nEnter the MUA7648 Phase I event now 
and enjoy up to $500,000 worth of $MUA and $MNT airdrops: https://7648.muaverse.build/'''
    res = res + url_suffix
    await ctx.send(res)

# @bot.event
# async def on_message(message):
#         # we do not want the bot to reply to itself

#     print(message.content)
#     # print(bot.user.id)
#     id = bot.user.id
#     if message.content.startswith(f'<@{id}>'):
#         await message.reply('Hello!', mention_author=True)



bot.run(token)