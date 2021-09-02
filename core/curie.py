import os
import openai
import discord
from discord.ext import commands

class CuriePlugin(commands.Cog, name='Talk to OpenAI Curie'):
	'''Commands to talk to Open AI Curie'''

	def __init__(self, bot):
		self.bot = bot
		self.ai = True

	def _openAIHookup(self, key):
		openai.api_key = key

	async def cog_check(self, ctx):
		'''
		The default check for this cog whenever a command is used. Returns True if the command is allowed.
		'''
		return ctx.author.id == self.bot.author_id

	@commands.command(name="ct")
	async def talkToCurie(self, ctx, *args):
		'''
		EXPIREMENTAL
		'''

		preSetup = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: {0}\nAI:"

		print(args)
		joinedPrompt = " ".join(args)

		finalPrompt = preSetup.format(joinedPrompt)

		response = openai.Completion.create(
			engine="curie",
			prompt=finalPrompt,
			temperature=0.9,
			max_tokens=150,
			top_p=1,
			frequency_penalty=0.0,
			presence_penalty=0.6,
			stop=["\n", " Human:", " AI:"]
		)
		print(response)
		output = None
		outputs = response['choices']
		for i in outputs:
			if output == None:
				output = i['text']

		await ctx.send(output)


def setup(bot):
	bot.add_cog(CuriePlugin(bot))
