import os
import re
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

		preSetup = """
		Goober is a silly chatbot that tries to carry a fun conversation with humans:

Goober: Hello! How can I help you?
Human: {0}
Goober:
		"""

		print(ctx.author.name, "says:", " ".join(args))
		joinedPrompt = " ".join(args)
		await ctx.trigger_typing()

		finalPrompt = preSetup.format(joinedPrompt)

		response = openai.Completion.create(
			engine="text-davinci-002",
			prompt=finalPrompt,
			temperature=0.5,
			max_tokens=60,
			top_p=0.3,
			frequency_penalty=0.5,
			presence_penalty=0.0,
			#stop=["\n", " Human:", " AI:"]
		)

		output = None
		outputs = response['choices']
		
		for i in outputs:
			if output == None:
				output = i['text']

		print("Curie responds:", output)

		if(re.sub(r"[\n\t\s]*", "", output) == ""):
			await ctx.send('...')

		await ctx.send(output)


def setup(bot):
	bot.add_cog(CuriePlugin(bot))
