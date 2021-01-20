from .. import loader
from telethon.tl.types import *

@loader.tds
class FrogMod(loader.Module):
	"""Отправляет лягушку"""
	strings = {"name": "Frog"}
	@loader.owner
	async def frogcmd(self, msg):
		await msg.edit("......... ..... _ e - e _
............_ ( - . _ . - ) _
.......- ( ....  . - - - ' .....) - .
.__ \ ....\ .\ .\ ___ / ./ ./ ..../ __
..' - . _ . ' / M \ ..../ M \ .._ , - `")
