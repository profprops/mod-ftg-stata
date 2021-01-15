from .. import loader
from asyncio import sleep

@loader.tds
class TestMod(loader.Module):
	strings = {"name":"Test"}
	@loader.owner
	async def testcmd(self, message):
		await message.edit("T")
		await sleep(0.1)
		await message.edit("TE")
		await sleep(0.1)
		await message.edit("TES")
		await sleep(0.1)
		await message.edit("TEST")
		await sleep(3)
		await message.edit("BY MAZA")
