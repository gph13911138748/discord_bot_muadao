import discord
from discord.ext import commands
import ssl
import certifi
import asyncio
import aiohttp

token = "MTI0NTYxNTQ2NTcyODk2NjY2Ng.GGnSpq.-w2G7t3ICIDh4WfY0BOoCjLwSmqhmN4HmOJS2o"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='@muadao-testbot', intents=intents)

# 配置 SSL 上下文
ssl_context = ssl.create_default_context(cafile=certifi.where())

# 自定义 HTTP 连接器
connector = aiohttp.TCPConnector(ssl=ssl_context)

# 在启动 bot 之前设置 aiohttp 的连接器
async def start_bot():
    async with aiohttp.ClientSession(connector=connector) as session:
        bot.http._HTTPClient__session = session
        await bot.start(token, reconnect=True)

# 创建一个新的事件循环
def main():
    new_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)
    try:
        new_loop.run_until_complete(start_bot())
    finally:
        new_loop.run_until_complete(bot.close())
        new_loop.close()

if __name__ == "__main__":
    main()


