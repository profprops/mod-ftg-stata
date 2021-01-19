from .. import loader, utils
from asyncio import sleep
from telethon.tl.types import *

@loader.tds
class TimerMod(loader.Module):
	"Таймер"
	strings = {"name": "Simple Timer"}
	@loader.owner
	async def timecmd(self, msg):
		""".time (время в секундах) - запускается таймер который будет изменять ваше сообщение каждую секунду."""
		time = int(utils.get_args_raw(msg))
		while time != 0:
			sleep(1)
			time-=1
			await msg.edit(str(time))
		await msg.edit("Таймер окончен")
		 
