import discord
from discord.ext import commands
import asyncio
import random

async def setup(bot):
	await bot.add_cog(Raid(bot))

class Raid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def raid(self, ctx, heure, code, *, pokemon):
        #messages = await ctx.channel.history(limit=1).flatten()
        #for message in messages:
            #await message.delete(delay=3)

        url = ["https://www.pokepedia.fr/images/b/bb/Artikodin-RFVF.png",
               "https://www.pokepedia.fr/images/8/81/%C3%89lecthor-RFVF.png",
               "https://www.pokepedia.fr/images/6/67/Sulfura-RFVF.png",
               "https://www.pokepedia.fr/images/d/db/Mewtwo-RFVF.png",
               "https://www.pokepedia.fr/images/7/7b/Raikou-HGSS.png",
               "https://www.pokepedia.fr/images/9/90/Entei-HGSS.png",
               "https://www.pokepedia.fr/images/9/9a/Suicune-HGSS.png",
               "https://www.pokepedia.fr/images/c/c0/Lugia-HGSS.png",
               "https://www.pokepedia.fr/images/4/40/Ho-Oh-HGSS.png",
               "https://www.pokepedia.fr/images/6/63/Regirock-RS.png",
               "https://www.pokepedia.fr/images/d/de/Regice-RS.png",
               "https://www.pokepedia.fr/images/f/fb/Registeel-RS.png",
               "https://www.pokepedia.fr/images/7/73/Latias-RS.png",
               "https://www.pokepedia.fr/images/f/fa/Latios-RS.png",
               "https://www.pokepedia.fr/images/e/e4/Kyogre-RS.png",
               "https://www.pokepedia.fr/images/5/5f/Groudon-RS.png",
               "https://www.pokepedia.fr/images/3/36/Rayquaza-ROSA.png",
               "https://www.pokepedia.fr/images/e/e1/Cr%C3%A9helf-DP.png",
               "https://www.pokepedia.fr/images/0/02/Cr%C3%A9follet-DP.png",
               "https://www.pokepedia.fr/images/7/75/Cr%C3%A9fadet-DP.png",
               "https://www.pokepedia.fr/images/e/e4/Dialga-DEPS.png",
               "https://www.pokepedia.fr/images/c/c7/Palkia-DEPS.png",
               "https://www.pokepedia.fr/images/a/af/Giratina-DP.png",
               "https://www.pokepedia.fr/images/b/bf/Heatran-DP.png",
               "https://www.pokepedia.fr/images/c/cb/Regigigas-DP.png",
               "https://www.pokepedia.fr/images/b/bf/Cresselia-DP.png",
               "https://www.pokepedia.fr/images/8/8f/Cobaltium-NB.png",
               "https://www.pokepedia.fr/images/6/66/Terrakium-NB.png",
               "https://www.pokepedia.fr/images/d/d1/Viridium-NB.png",
               "https://www.pokepedia.fr/images/1/1b/Bor%C3%A9as_%28Forme_Avatar%29-NB.png",
               "https://www.pokepedia.fr/images/1/1b/Fulguris_%28Forme_Avatar%29-NB.png",
               "https://www.pokepedia.fr/images/8/87/D%C3%A9m%C3%A9t%C3%A9ros_%28Forme_Avatar%29-NB.png",
               "https://www.pokepedia.fr/images/b/b3/Reshiram-NB.png",
               "https://www.pokepedia.fr/images/c/c7/Zekrom-NB.png",
               "https://www.pokepedia.fr/images/a/a5/Kyurem-NB.png",
               "https://www.pokepedia.fr/images/b/bb/Xerneas_%28Mode_D%C3%A9cha%C3%AEn%C3%A9%29-XY.png",
               "https://www.pokepedia.fr/images/a/a0/Yveltal-XY.png",
               "https://www.pokepedia.fr/images/c/c4/Deoxys_%28Forme_Normale%29-RS.png",
               "https://www.pokepedia.fr/images/5/59/Darkrai-DP.png",
               "https://www.pokepedia.fr/images/4/4b/Genesect-NB2.png",
               "https://www.pokepedia.fr/images/2/27/Artikodin_de_Galar-EB.png",
               "https://www.pokepedia.fr/images/8/83/%C3%89lecthor_de_Galar-EB.png",
               "https://www.pokepedia.fr/images/3/3d/Sulfura_de_Galar-EB.png"]

        def pok():
            if f"{pokemon}".lower() == "artikodin":
                return url[0]
            elif f"{pokemon}".lower() == "electhor":
                return url[1]
            elif f"{pokemon}".lower() == "sulfura":
                return url[2]
            elif f"{pokemon}".lower() == "mewtwo":
                return url[3]
            elif f"{pokemon}".lower() == "raikou":
                return url[4]
            elif f"{pokemon}".lower() == "entei":
                return url[5]
            elif f"{pokemon}".lower() == "suicune":
                return url[6]
            elif f"{pokemon}".lower() == "lugia":
                return url[7]
            elif f"{pokemon}".lower() == "ho-oh":
                return url[8]
            elif f"{pokemon}".lower() == "regirock":
                return url[9]
            elif f"{pokemon}".lower() == "regice":
                return url[10]
            elif f"{pokemon}".lower() == "registeel":
                return url[11]
            elif f"{pokemon}".lower() == "latias":
                return url[12]
            elif f"{pokemon}".lower() == "latios":
                return url[13]
            elif f"{pokemon}".lower() == "kyogre":
                return url[14]
            elif f"{pokemon}".lower() == "groudon":
                return url[15]
            elif f"{pokemon}".lower() == "rayquaza":
                return url[16]
            elif f"{pokemon}".lower() == "crehelf":
                return url[17]
            elif f"{pokemon}".lower() == "crefollet":
                return url[18]
            elif f"{pokemon}".lower() == "crefadet":
                return url[19]
            elif f"{pokemon}".lower() == "dialga":
                return url[20]
            elif f"{pokemon}".lower() == "palkia":
                return url[21]
            elif f"{pokemon}".lower() == "giratina":
                return url[22]
            elif f"{pokemon}".lower() == "heatran":
                return url[23]
            elif f"{pokemon}".lower() == "regigigas":
                return url[24]
            elif f"{pokemon}".lower() == "cresselia":
                return url[25]
            elif f"{pokemon}".lower() == "cobaltium":
                return url[26]
            elif f"{pokemon}".lower() == "terrakium":
                return url[27]
            elif f"{pokemon}".lower() == "viridium":
                return url[28]
            elif f"{pokemon}".lower() == "boreas":
                return url[29]
            elif f"{pokemon}".lower() == "fulguris":
                return url[30]
            elif f"{pokemon}".lower() == "demeteros":
                return url[31]
            elif f"{pokemon}".lower() == "reshiram":
                return url[32]
            elif f"{pokemon}".lower() == "zekrom":
                return url[33]
            elif f"{pokemon}".lower() == "kyurem":
                return url[34]
            elif f"{pokemon}".lower() == "xerneas":
                return url[35]
            elif f"{pokemon}".lower() == "yveltal":
                return url[36]
            elif f"{pokemon}".lower() == "deoxys":
                return url[37]
            elif f"{pokemon}".lower() == "darkrai":
                return url[38]
            elif f"{pokemon}".lower() == "genesect":
                return url[39]
            elif f"{pokemon}".lower() == "artikodin de galar":
                return url[40]
            elif f"{pokemon}".lower() == "electhor de galar":
                return url[41]
            elif f"{pokemon}".lower() == "sulfura de galar":
                return url[42]
            else:
                return ""

        couleur = [0xfc9f03,
                   0x990000,
                   0x3300ee]

        embed = discord.Embed(title=f"*** Raid proposé : {pokemon}***", color=random.choice(couleur))
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar)
        embed.set_thumbnail(url=f"{pok()}")
        embed.add_field(name="**Heure**", value=f"{heure}", inline=True)
        embed.add_field(name="Code amis ", value=f"{code}", inline=True)
        await ctx.send(embed=embed)
        #await ctx.send("Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")


    @commands.command()
    async def rid(self, ctx, *, pokemon):
        heure = ""
        while heure == "":
            await ctx.send("A quel heure commence le raid ? (00h-23 h)")

            def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel

            reponse1 = await self.bot.wait_for("message", check=checkMessage)

            try:
                heure = int(reponse1.content)

            except:
                await ctx.send(":warning: Vous devez rentrer un nombre compris entre 1 et 24 pour les heures!")


        while int(reponse1.content) > 24:
            await ctx.send(":warning: Vous devez rentrer un nombre compris entre 1 et 24 pour les heures! \nA quel heure commence le raid ? (00h-23 h)")

            def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel

            reponse1 = await self.bot.wait_for("message", check=checkMessage)

            try:
                int(reponse1.content) < 25

            except:
                await ctx.send("")


        minute = ""
        while minute == "":
            await ctx.send("A combien de minute ? (0-59 min)")

            def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel

            reponse2 = await self.bot.wait_for("message", check=checkMessage)

            try:
                minute = int(reponse2.content)
            except:
                await ctx.send(":warning: Vous devez rentrer un nombre compris entre 00 et 59 pour les minutes!")

        while int(reponse2.content) > 60:
            await ctx.send(":warning: Vous devez rentrer un nombre compris entre 00 et 59 pour les minutes! \nA combien de minute ? (0-59 min)")

            def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel

            reponse2 = await self.bot.wait_for("message", check=checkMessage)


            try:
               reponse2.content < 60

            except:
                """await ctx.send("")"""
        code = ""
        while code == "":
            await ctx.send("Quel est votre code ami ( xxxxxxxxxxxx )")

            def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel

            reponse3 = await self.bot.wait_for("message", check=checkMessage)

            try:
                code = int(reponse3.content)
            except:
                await ctx.send(":warning: Vous devez rentrer des nombres pour le code ami!")

       
        found_code = False  # Variable pour suivre si la réponse correcte au code ami a été trouvée

        async for message in ctx.channel.history(limit=None):
            if message.author == ctx.message.author and message.content == str(code):
                found_code = True
                continue  # Passe au message suivant sans l'ajouter à la liste
            if found_code and message.content.startswith("!rid"):
                break  # Arrête la boucle lorsque la commande !rid est trouvée
            await message.delete() 
        #await ctx.send("c fait")
        #await asyncio.sleep(10)
        messages = await ctx.channel.purge(limit=2)


        url = ["https://www.pokepedia.fr/images/b/bb/Artikodin-RFVF.png",
               "https://www.pokepedia.fr/images/8/81/%C3%89lecthor-RFVF.png",
               "https://www.pokepedia.fr/images/6/67/Sulfura-RFVF.png",
               "https://www.pokepedia.fr/images/d/db/Mewtwo-RFVF.png",
               "https://www.pokepedia.fr/images/7/7b/Raikou-HGSS.png",
               "https://www.pokepedia.fr/images/9/90/Entei-HGSS.png",
               "https://www.pokepedia.fr/images/9/9a/Suicune-HGSS.png",
               "https://www.pokepedia.fr/images/c/c0/Lugia-HGSS.png",
               "https://www.pokepedia.fr/images/4/40/Ho-Oh-HGSS.png",
               "https://www.pokepedia.fr/images/6/63/Regirock-RS.png",
               "https://www.pokepedia.fr/images/d/de/Regice-RS.png",
               "https://www.pokepedia.fr/images/f/fb/Registeel-RS.png",
               "https://www.pokepedia.fr/images/7/73/Latias-RS.png",
               "https://www.pokepedia.fr/images/f/fa/Latios-RS.png",
               "https://www.pokepedia.fr/images/e/e4/Kyogre-RS.png",
               "https://www.pokepedia.fr/images/5/5f/Groudon-RS.png",
               "https://www.pokepedia.fr/images/3/36/Rayquaza-ROSA.png",
               "https://www.pokepedia.fr/images/e/e1/Cr%C3%A9helf-DP.png",
               "https://www.pokepedia.fr/images/0/02/Cr%C3%A9follet-DP.png",
               "https://www.pokepedia.fr/images/7/75/Cr%C3%A9fadet-DP.png",
               "https://www.pokepedia.fr/images/e/e4/Dialga-DEPS.png",
               "https://www.pokepedia.fr/images/c/c7/Palkia-DEPS.png",
               "https://www.pokepedia.fr/images/a/af/Giratina-DP.png",
               "https://www.pokepedia.fr/images/b/bf/Heatran-DP.png",
               "https://www.pokepedia.fr/images/c/cb/Regigigas-DP.png",
               "https://www.pokepedia.fr/images/b/bf/Cresselia-DP.png",
               "https://www.pokepedia.fr/images/8/8f/Cobaltium-NB.png",
               "https://www.pokepedia.fr/images/6/66/Terrakium-NB.png",
               "https://www.pokepedia.fr/images/d/d1/Viridium-NB.png",
               "https://www.pokepedia.fr/images/1/1b/Bor%C3%A9as_%28Forme_Avatar%29-NB.png",
               "https://www.pokepedia.fr/images/1/1b/Fulguris_%28Forme_Avatar%29-NB.png",
               "https://www.pokepedia.fr/images/8/87/D%C3%A9m%C3%A9t%C3%A9ros_%28Forme_Avatar%29-NB.png",
               "https://www.pokepedia.fr/images/b/b3/Reshiram-NB.png",
               "https://www.pokepedia.fr/images/c/c7/Zekrom-NB.png",
               "https://www.pokepedia.fr/images/a/a5/Kyurem-NB.png",
               "https://www.pokepedia.fr/images/b/bb/Xerneas_%28Mode_D%C3%A9cha%C3%AEn%C3%A9%29-XY.png",
               "https://www.pokepedia.fr/images/a/a0/Yveltal-XY.png",
               "https://www.pokepedia.fr/images/c/c4/Deoxys_%28Forme_Normale%29-RS.png",
               "https://www.pokepedia.fr/images/5/59/Darkrai-DP.png",
               "https://www.pokepedia.fr/images/4/4b/Genesect-NB2.png",
               "https://www.pokepedia.fr/images/2/27/Artikodin_de_Galar-EB.png",
               "https://www.pokepedia.fr/images/8/83/%C3%89lecthor_de_Galar-EB.png",
               "https://www.pokepedia.fr/images/3/3d/Sulfura_de_Galar-EB.png"]

        def pok():
            if f"{pokemon}".lower() == "artikodin":
                return url[0]
            elif f"{pokemon}".lower() == "electhor":
                return url[1]
            elif f"{pokemon}".lower() == "sulfura":
                return url[2]
            elif f"{pokemon}".lower() == "mewtwo":
                return url[3]
            elif f"{pokemon}".lower() == "raikou":
                return url[4]
            elif f"{pokemon}".lower() == "entei":
                return url[5]
            elif f"{pokemon}".lower() == "suicune":
                return url[6]
            elif f"{pokemon}".lower() == "lugia":
                return url[7]
            elif f"{pokemon}".lower() == "ho-oh":
                return url[8]
            elif f"{pokemon}".lower() == "regirock":
                return url[9]
            elif f"{pokemon}".lower() == "regice":
                return url[10]
            elif f"{pokemon}".lower() == "registeel":
                return url[11]
            elif f"{pokemon}".lower() == "latias":
                return url[12]
            elif f"{pokemon}".lower() == "latios":
                return url[13]
            elif f"{pokemon}".lower() == "kyogre":
                return url[14]
            elif f"{pokemon}".lower() == "groudon":
                return url[15]
            elif f"{pokemon}".lower() == "rayquaza":
                return url[16]
            elif f"{pokemon}".lower() == "crehelf":
                return url[17]
            elif f"{pokemon}".lower() == "crefollet":
                return url[18]
            elif f"{pokemon}".lower() == "crefadet":
                return url[19]
            elif f"{pokemon}".lower() == "dialga":
                return url[20]
            elif f"{pokemon}".lower() == "palkia":
                return url[21]
            elif f"{pokemon}".lower() == "giratina":
                return url[22]
            elif f"{pokemon}".lower() == "heatran":
                return url[23]
            elif f"{pokemon}".lower() == "regigigas":
                return url[24]
            elif f"{pokemon}".lower() == "cresselia":
                return url[25]
            elif f"{pokemon}".lower() == "cobaltium":
                return url[26]
            elif f"{pokemon}".lower() == "terrakium":
                return url[27]
            elif f"{pokemon}".lower() == "viridium":
                return url[28]
            elif f"{pokemon}".lower() == "boreas":
                return url[29]
            elif f"{pokemon}".lower() == "fulguris":
                return url[30]
            elif f"{pokemon}".lower() == "demeteros":
                return url[31]
            elif f"{pokemon}".lower() == "reshiram":
                return url[32]
            elif f"{pokemon}".lower() == "zekrom":
                return url[33]
            elif f"{pokemon}".lower() == "kyurem":
                return url[34]
            elif f"{pokemon}".lower() == "xerneas":
                return url[35]
            elif f"{pokemon}".lower() == "yveltal":
                return url[36]
            elif f"{pokemon}".lower() == "deoxys":
                return url[37]
            elif f"{pokemon}".lower() == "darkrai":
                return url[38]
            elif f"{pokemon}".lower() == "genesect":
                return url[39]
            elif f"{pokemon}".lower() == "artikodin de galar":
                return url[40]
            elif f"{pokemon}".lower() == "electhor de galar":
                return url[41]
            elif f"{pokemon}".lower() == "sulfura de galar":
                return url[42]
            else:
                return ""


        embed = discord.Embed(title=f"*** Raid proposé : {pokemon}***", color=0x3300ee)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar)
        embed.set_thumbnail(url=f"{pok()}")
        embed.add_field(name="**Heure**", value=f"{reponse1.content}H{reponse2.content}", inline=True)
        embed.add_field(name="Code amis ", value=f"{reponse3.content}", inline=True)
        embed.add_field(name="Participants ", value=":", inline=False)
        message = await ctx.send(embed=embed)

        await ctx.send(f"Le raid {pokemon} va commencer. Si vous voulez l'annulé cliquer sur ❌")
        await message.add_reaction("✅")
        await message.add_reaction("❌")
        await ctx.send("Si tu veux jouer cliquer sur ✅")
        await ctx.send("Le raid va commencer. Envoyez \"moi\" dans ce channel pour y participer.")

        players = []

        def check(message):
            return message.channel == ctx.message.channel and message.author not in players and message.content.lower() == "moi"

        try:
            while True:
                participation = await self.bot.wait_for("message",timeout=10, check=check)
                print("0")
                players.append(participation.author.mention)
                print("Nouveau participant : ")
                await ctx.send(f"**{participation.author.name}** participe au raid")
                #messages = await ctx.channel.purge(limit=2)
                print("aa")
        except:
            await ctx.send("Le raid va bientôt commencer")
    
        
        def checkEmoji(reaction, user):
            return ctx.message.author == user and message.id == reaction.message.id and (
                    str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

        try:
            reaction, user = await self.bot.wait_for("reaction_add", timeout=0, check=checkEmoji)
            if reaction.emoji == "✅":
                await ctx.send("Ta participation a bien été prise en compte")
            else:
                await ctx.send("Le raid a bien été annulé")
                messages = await ctx.channel.history(limit=4).flatten()
                for message in messages:
                    await message.delete(delay=2)
        except:
            '''await ctx.send("La recette a été anulée vous avez mis trop de temps a réagir.")'''

        newembed = discord.Embed(title=f"*** Raid proposé : {pokemon}***", color=0x990000)
        newembed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar)
        newembed.set_thumbnail(url=f"{pok()}")
        newembed.add_field(name="**Heure**", value=f"{reponse1.content}H{reponse2.content}", inline=True)
        newembed.add_field(name="Code amis ", value=f"{reponse3.content}", inline=True)
        newembed.add_field(name="Participants ", value=", ".join(players), inline=False)
        await message.edit(embed=newembed)

        #print(players)
        #if (players(len)) == 1:
                #return


    @commands.command()
    async def tst(self, ctx, raid, heure, code):
        embed = discord.Embed(title=f"** Raid proposé : {raid}**", color=0x3300ee)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar)
        embed.set_thumbnail(url=ctx.author.display_avatar)
        embed.set_image(url="https://www.pokepedia.fr/images/b/b3/Reshiram-NB.png")
        embed.add_field(name="**Heure**", value=heure, inline=True)
        embed.add_field(name="Code amis ", value=code, inline=True)
        await ctx.send(embed=embed)
