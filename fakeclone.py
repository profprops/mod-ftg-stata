from .. import loader
from telethon.tl.types import *
from asyncio import sleep

@loader.tds
class WaveCloneMod(loader.Module):
  "Полная статистика чата"
  strings = {"name": "Fake Clone of WaveYT"}
  @loader.owner
  async def waveclonecmd(self, msg):
          await msg.edit("__Клонирование вейва...__")
	  sleep(5)
	  await msg.edit("**Клонирование прошло успешно!**")
