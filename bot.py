import io
import discord
import aiohttp
from discord.ext import commands

from cpi import ask_gaianet
from button import URLButton



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.command()
# @commands.has_permissions(administrator=True)
# async def synccommands(ctx):
#     await bot.tree.sync()
#     await ctx.send('sync commands finnish')

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
    
    #嵌入 图片
    # new_embed = discord.Embed()
    # new_embed.set_image(url = image_url)
    # await ctx.send(embed = new_embed)

    # 以文件形式发送可以显示
    # 创建Embed对象
    embed = discord.Embed(
        # title="消息标题",  # 可以根据需要调整标题
        description=welcome_message,  # 这里是你的文字描述
        color=discord.Color.blue()  # 可以选择一个适合的颜色
    )
    file=discord.File("muadao.jpg", filename="muadao.jpg")
        # 添加图片，将会显示在文字上方
    embed.set_image(url="attachment://muadao.jpg")
        # 发送嵌入式消息
    await ctx.send(file=file,embed=embed, view = URLButton())
    # await ctx.send(file=discord.File("muadao.jpg")) 
    # await ctx.send(content=welcome_message, view = PlayView())

# @bot.command()
# async def query(ctx, message): # message这部分也需要改进
#     res = await ask_gaianet("muadao", message)
#     print(message)
#     url_suffix= f'''\nEnter the MUA7648 Phase I event now 
# and enjoy up to $500,000 worth of $MUA and $MNT airdrops: https://7648.muaverse.build/'''
#     res = res + url_suffix
#     await ctx.send(res)

def parse_message(message):
    parts = message.split(maxsplit=2)
    
    bot_username = parts[0]
    command = None
    query = None
    
    if len(parts) > 1:
        if parts[1].startswith('/'):
            command = parts[1][1:]
            if len(parts) > 2:
                query = parts[2]
        else:
            if len(parts) > 2:
                query = parts[1] + ' ' + parts[2]
            else:
                query = parts[1]
    
    print(query)
    return bot_username, command, query

@bot.event
async def on_message(message):
    if message.content == "!synccommands":
        await bot.tree.sync()
        await message.reply('sync commands finnish')

    id = bot.user.id
    if message.content.startswith(f'<@{id}>'):
        bot_username, command, query = parse_message(message.content)
        res = await ask_gaianet("muadao", query)
        url_suffix= f'''\nEnter the MUA7648 Phase I event now 
and enjoy up to $500,000 worth of $MUA and $MNT airdrops: https://7648.muaverse.build/'''
        res = res + url_suffix
        await message.reply(res, mention_author=True)



bot.run(token)