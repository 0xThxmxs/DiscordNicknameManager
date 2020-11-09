import json

from discord.ext import commands

with open("config.json", "r") as dump:
	config = json.load(dump)

bot = commands.Bot(command_prefix=config["prefix"], self_bot=True)
bot.remove_command("help")


@bot.event
async def on_connect():
	print("oue boss")
	for guild in bot.guilds:
		for member in guild.members:
			if member.name == bot.user.name:
				if member.nick and member.nick != bot.user.name:
					print("[+] Nickname reseted from {} ({}) !".format(guild, member.nick))
					await member.edit(nick="")


bot.run(config["token"], bot=False)
