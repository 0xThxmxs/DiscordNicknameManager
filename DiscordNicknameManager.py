import json

from discord.ext import commands

with open("config.json", "r") as dump:
	config = json.load(dump)

bot = commands.Bot(command_prefix=config["prefix"], self_bot=True)
bot.remove_command("help")


@bot.command(pass_context=True)
async def reset(ctx):
	for guild in bot.guilds:
		for member in guild.members:
			if member.name == bot.user.name:
				if member.nick and member.nick != bot.user.name:
					await member.edit(nick="")
					print("[+] Nicknames reseted from everywhere !")


bot.run(config["token"], bot=False)
