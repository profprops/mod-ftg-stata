from .. import loader
from asyncio import sleep

@loader.tds
class TestMod(loader.Module):
	strings = {"name":"Test"}
	@loader.owner
	async def testcmd(self, message):
		await message.edit("M")
		await sleep(1)
		await message.edit("Mo")
		await sleep(1)
		await message.edit("Mod")
		await sleep(1)
		await message.edit("Modu")
		await sleep(1)
		await message.edit("Modul")
		await sleep(1)
		await message.edit("Module")
		await sleep(1)
		await message.edit("Module ")
		await sleep(1)
		await message.edit("Module b")
		await sleep(1)
		await message.edit("Module by")
		await sleep(1)
		await message.edit("Module by ")
		await sleep(1)
		await message.edit("Module by M")
		await sleep(1)
		await message.edit("Module by MA")
		await sleep(1)
		await message.edit("Module by MAZ")
		await sleep(1)
		await message.edit("Module by MAZA")
	