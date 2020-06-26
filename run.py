import discord
import asyncio
import json


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



# client를 구동시킵니다.
client.run(token)
