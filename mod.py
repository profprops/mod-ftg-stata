from .. import loader
from telethon.tl.types import *
@loader.tds
class ChatStatisticMod(loader.Module):
  "Статистика чата"
  strings = {"name": "ChatStatistic"}
  @loader.owner
  async def statacmd(self, m):
	  await m.edit("<b>Считаем...</b>")
	  al = str((await m.client.get_messages(m.to_id, limit=0)).total)
	  ph = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterPhotos())).total)
	  vi = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterVideo())).total)
	  mu = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterMusic())).total)
	  vo = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterVideo())).total)
	  vv = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterRoundVideo())).total)
	  do = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterDocument())).total)
	  urls = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterUrl())).total)
	  gifs = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterGif())).total)
	  geos = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterGeo())).total)
	  cont = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterContacts())).total)
	  await m.edit(
	    ("<b>Всего сoообщений</b> {}\n"+
		"<b>BY MAZA</b>\n"+
	    "<b>Фото:</b> {}\n"+
	    "<b>Видео:</b> {}\n"+
	    "<b>Музыка:</b> {}\n"+
	    "<b>Голосовые:</b> {}\n"+
	    "<b>Круглые видео:</b> {}\n"+
	    "<b>Файлы:</b> {}\n"+
	    "<b>Ссылки:</b> {}\n"+
	    "<b>Гиф:</b> {}\n"+
	    "<b>Корды:</b> {}\n"+
	    "<b>Контакты:</b> {}").format(al, ph, vi, mu, vo, vv, do, urls, gifs, geos, cont))