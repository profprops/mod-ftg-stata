from .. import loader
from telethon.tl.types import *
from asyncio import sleep

@loader.tds
class FullChatStataMod(loader.Module):
  "Полная статистика чата"
  strings = {"name": "Full ChatStata"}
  @loader.owner
  async def fullstatacmd(self, msg):
          await msg.edit("Инициализация...")
          tmsg = str((await msg.client.get_messages(msg.to_id, limit=0)).total)
          tgeo = str((await msg.client.get_messages(msg.to_id, limit=0, filter=InputMessagesFilterGeo())).total)
          tgif = str((await msg.client.get_messages(msg.to_id, limit=0, filter=InputMessagesFilterGif())).total)
          trovid = str((await msg.client.get_messages(msg.to_id, limit=0, filter=InputMessagesFilterRoundVideo())).total)
          turl = str((await msg.client.get_messages(msg.to_id, limit=0, filter=InputMessagesFilterUrl())).total)
          tvo = str((await msg.client.get_messages(msg.to_id, limit=0, filter=InputMessagesFilterVoice())).total)
          tco = str((await msg.client.get_messages(msg.to_id, limit=0, filter=InputMessagesFilterContacts())).total)
          tpho = str((await msg.client.get_messages(msg.to_id, limit=0, filter=InputMessagesFilterPhotos())).total)
          tmu = str((await msg.client.get_messages(msg.to_id, limit=0, filter=InputMessagesFilterMusic())).total)
          tdo = str((await msg.client.get_messages(msg.to_id, limit=0, filter=InputMessagesFilterDocument())).total)
          tvid = str((await msg.client.get_messages(msg.to_id, limit=0, filter=InputMessagesFilterVideo())).total)
          trovo = str((await msg.client.get_messages(msg.to_id, limit=0, filter=InputMessagesFilterRoundVoice())).total)
          await msg.edit("Инициализация завершена")
          sleep(1)
          await msg.edit("Сообщения: " + tmsg + "\nМестоположения: " + tgeo + "\nGIF: " + tgif + "\nКруглые видео: " + trovid + "\nСсылки: " + turl + "\nГолосовые: " + tvo + "\nКонтакты: " + tco + "\nФото: " + tpho + "\nМузыка: " + tmu + "\nДокументы: " + tdo + "\nВидео: " + tvid + "\n?: " + trovo)
