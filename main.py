import os
#from keep_alive import keep_alive
from discord.ext import commands

from config import *

bot = commands.Bot(
	command_prefix=bot_identifier,  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = bot_owner_id

@bot.event
async def on_ready():  # When the bot is ready
	print("Successful Connection.")
	print("NAME =", bot.user, "ID =", bot.user.id)  # Prints the bot's username and identifier

def connectCogs(database):
	for index in bot.cogs:
		cog = bot.cogs[index]
		if cog.ai:
			cog._openAIHookup(OPENAI_API_KEY)

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

	connectCogs(None)
	#keep_alive()  # Starts a webserver to be pinged.
	#token = os.environ.get("DISCORD_BOT_SECRET")
	bot.run(bot_token)  # Starts the bot
