import discord
from discord.ext import commands
import asyncio
import random

async def setup(bot):
	await bot.add_cog(Codeami(bot))

class Codeami(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def coucou(self, ctx): 
        await ctx.send("coucou")

    @commands.command()
    async def ha(self, ctx): 
        await ctx.send("bonbonjour")


    codes_amis = {}
    codes_amis1 = {}

    @commands.command()
    async def addcode(self, ctx):
	    if ctx.author.id not in self.codes_amis :
	        await ctx.send("Quel est votre code ami pour Pokémon GO ?")

	        def check1(message):
	            return message.author == ctx.message.author and message.channel == ctx.channel and message.author.id not in self.codes_amis
	        
	        try:
	            reponse1 = await self.bot.wait_for("message", check=check1, timeout=30)
	            self.codes_amis[ctx.author.id] = reponse1.content
	            await ctx.send(f"{ctx.author.mention} Votre code ami pour Pokémon GO {reponse1.content} a bien été enregistré")
	        except asyncio.TimeoutError:
	            await ctx.send("Temps écoulé. Veuillez réessayer.")


	        await ctx.send("Quel est votre code ami pour Nintendo Switch ?")

	        def check2(message):
	            return message.author == ctx.message.author and message.channel == ctx.channel and message.author.id not in self.codes_amis1
	        
	        try:
	            reponse2 = await self.bot.wait_for("message", check=check2, timeout=30)
	            self.codes_amis1[ctx.author.id] = reponse2.content
	            await ctx.send(f"{ctx.author.mention} Votre code ami pour Nintendo Switch {reponse2.content} a bien été enregistré")
	        except asyncio.TimeoutError:
	            await ctx.send("Temps écoulé. Veuillez réessayer.")
	    else:
	        await ctx.send("Vous avez déjà ajouté vos codes")


    @commands.command()
    async def code(self, ctx, member: discord.Member):
	    if member.id in self.codes_amis:
	        embed = discord.Embed(title="***Codes amis ***", color=0xfcdf76)
	        embed.set_author(name=f"{member.display_name}", icon_url=member.display_avatar)
	        embed.add_field(name="Code amis pogo", value=f"{self.codes_amis[member.id]}", inline=True)
	        embed.add_field(name="Code amis switch", value=f"{self.codes_amis1[member.id]}", inline=True)
	        await ctx.send(embed=embed)
	 
	    else:
	        await ctx.send("Le code ami de cette personne n'est pas enregistré.")


    @commands.command()
    async def codepogo(self, ctx):
	    if ctx.author.id in self.codes_amis:
	        await ctx.send("Quel est votre nouveau code ami ?")

	        def check2(message):
	            return message.author == ctx.message.author and ctx.message.channel == message.channel and message.author.id in self.codes_amis
	        
	        try:
	            reponse = await self.bot.wait_for("message", check=check2, timeout=30)
	            self.codes_amis[ctx.author.id] = reponse.content
	            await ctx.send(f"{ctx.author.mention} Votre nouveau code ami {reponse.content} a bien été enregistré")
	        except asyncio.TimeoutError:
	            await ctx.send("Temps écoulé. Veuillez réessayer.")

	    else:
	        await ctx.send("Vous n'avez pas encore ajouté votre code ami !")


    @commands.command()
    async def codeswitch(self, ctx):
	    if ctx.author.id in self.codes_amis1:
	        await ctx.send("Quel est votre nouveau code ami ?")

	        def check2(message):
	            return message.author == ctx.message.author and ctx.message.channel == message.channel and message.author.id in self.codes_amis
	        
	        try:
	            reponse = await self.bot.wait_for("message", check=check2, timeout=30)
	            self.codes_amis1[ctx.author.id] = reponse.content
	            await ctx.send(f"{ctx.author.mention} Votre nouveau code ami {reponse.content} a bien été enregistré")
	        except asyncio.TimeoutError:
	            await ctx.send("Temps écoulé. Veuillez réessayer.")

	    else:
	        await ctx.send("Vous n'avez pas encore ajouté votre code ami !")
