import discord
import asyncio
import json
import time
"""
discord.__version__ == 1.3.3

"""
client = discord.Client()
token = ""  # 절대 이곳에 토큰을 적지 말고 다른 파일에서 읽어오는 형식으로 진행하기

# 봇이 구동되었을 때
@client.event
async def on_ready():
    print("Logged in as ")
    print(client.user.name)
    print(client.user.id)
    print("=============")

    await client.change_presence(activity=discord.Game("ON", type=1))


# 메세지가 입력되었을 때
@client.event
async def on_message(message):
    if message.author.bot:
        return None  # 봇이 보낸 메세지는 무시합니다.

    file_path = "./Question"
    name = client.user.name
    script = message.content
    group = dict()

    group['name'] = name
    group['script'] = script

    with open(file_path, 'w') as f:
        json.dump(group, f, ensure_ascii=False)


# client를 구동시킵니다.
client.run(token)
