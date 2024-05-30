import asyncio
import aiohttp
import json
import ssl
import certifi
import logging

logger_suffix = "muadao.tgbot"
logger = logging.getLogger("portal_hub")

async def ask_gaianet(node: str, message: str):
    async with aiohttp.ClientSession() as session:
        url = f"https://{node}.gaianet.network/v1/chat/completions"  # 替换为您的实际公共 URL
        payload = {
            "messages": [
                #{"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{message}"}
            ]
        }
        headers = {"Content-Type": "application/json", "accept": "application/json"}

        # 创建 SSL 上下文并加载 certifi 的 CA 证书
        ssl_context = ssl.create_default_context(cafile=certifi.where())

        try:
            async with session.post(url, json=payload, headers=headers, ssl=ssl_context) as response:
                # 打印响应的内容类型
                logger.info(f"{logger_suffix} Content-Type: {response.headers['Content-Type']}")

                text = await response.text()
                text = json.loads(text)
                text = text['choices'][0]['message']['content']
                print(f"Unexpected content type. Response content: {text}")
                return text
        except aiohttp.ClientConnectorError as e:
            logger.info(f"{logger_suffix} Connection error: {e}")
        except aiohttp.ClientResponseError as e:
            logger.info(f"{logger_suffix} Response error: {e}")

async def main():
    res = await ask_gaianet("knowledge2","hi")
# 运行异步主函数
if __name__ == '__main__':
    asyncio.run(main())

# curl -X POST https://law.gaianet.network/v1/chat/completions \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{"messages":[{"role":"system", "content": "You are a helpful assistant."}, {"role":"user", "content": "Where is Paris?"}]}'

