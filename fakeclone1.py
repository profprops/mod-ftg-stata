from .. import loader
from telethon.tl.types import *
from asyncio import sleep

@loader.tds
class WaveCloneMod(loader.Module):
  "Fake Clone of WaveYT"
  strings = {"name": "Clone @gdewave"}
  @loader.owner
  async def clonewavecmd(self, msg):
          await msg.edit("__Клонируем вейва...__\nby @mason767yt")
          sleep(5)
          await msg.edit("**Клонирование прошло успешно!**")
