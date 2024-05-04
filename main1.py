import discord
from discord.ext import commands
import asyncio
import random
#import cog_1

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", description="Test du nouveau bot", intents=intents)


@bot.event
async def on_ready():
    print("Ready !")


#bot.add_cog(cog_1.CogOwner(bot))


@bot.command()
async def load(ctx, name=None):
    if name:
        bot.load_extension(name)


@bot.command()
async def unload(ctx, name=None):
    if name:
        bot.unload_extension(name)


@bot.command()
async def reload(ctx, name=None):
    if name:
        try:
            bot.reload_extension(name)
        except:
            bot.load_extension(name)


@bot.command()
async def infochaine(ctx):
    await ctx.send("https://www.youtube.com/channel/UCx3I1q4JNLGrBNxqSsb4Z4A")


@bot.command()
async def ruhtra(ctx):
    await ctx.send("Ruhtra est le meilleur youtubeur ")


@bot.command()
async def combatabonnes(ctx):
    await ctx.send("https://www.youtube.com/watch?v=flOzvMGNUo8&list=PLvauXDNLkOlFZ20Zpj3Z_thIWrliD7vYV")


@bot.command()
async def ppp(ctx):
    await ctx.send("https://www.youtube.com/watch?v=D9q48loIfNc&list=PLvauXDNLkOlGdDawOQKe7wfmNSvtSnj1N")


@bot.command()
async def infoserver(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"Le serveur ***{serverName}*** contient **{numberOfPerson}** personnes. \n La description du serveur ***{serverDescription}***. \n Ce serveur possède **{numberOfTextChannels}** salons textuel ainsi que **{numberOfVoiceChannels}** salon vocaux."
    await ctx.send(message)


@bot.command()
async def bonjour(ctx):
    server = ctx.guild
    serverName = server.name
    await ctx.send(
        f"Bonjour jeune *padawan* ! Savais tu que tu te trouvais dans le serveur *{serverName}*, c'est d'ailleurs un super serveur puisque **JE** suis dedans.")


@bot.command()
async def say(ctx, *text):
    await ctx.send(" ".join(text))


@bot.command()
async def dire(ctx, number, *text):
    for i in range(int(number)):
        await ctx.send(" ".join(text))


@bot.command()
async def chinese(ctx, *text):
    chineseChar = "丹书ㄈ力已下呂廾工丿片乚爪ㄇ口尸厶尺ㄎ丁凵人山父了乙"
    chineseText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = chineseChar[index]
                chineseText.append(transformed)
            else:
                chineseText.append(char)
        chineseText.append(" ")
    await ctx.send("".join(chineseText))


""""@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Cette commande n'exite pas")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Il manque un argument.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Vous n'avez pas les permissons pour utiliser cette commande.")"""


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, nombre: int):
    messages = await ctx.channel.history(limit=nombre + 1).flatten()
    for message in messages:
        await message.delete()
    await ctx.send(f"J'ai supprimer {nombre} messages")
    mes = await ctx.channel.history(limit=1).flatten()
    for message in mes:
        await message.delete(delay=4)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason=reason)
    await ctx.send(f"{user} à été kick.")


funFact = ["L'eau mouille",
           "Le feu brûle",
           "Lorsque vous volez, vous ne touchez pas le sol"]


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.User, *, reason="Aucune raison n'a été donné"):
    # await ctx.guild.ban(user, reason = reason)
    embed = discord.Embed(title="**Banissement**", description="un modérateur a frappé !",
                          url="https://www.youtube.com/channel/UCx3I1q4JNLGrBNxqSsb4Z4A", color=0xde9d38)
    embed.set_author(name=ctx.author.name, icon_url=ctx.message.author.display_avatar)
    embed.set_thumbnail(url="https://discordemoji.com/assets/emoji/BanneHammer.png")
    embed.add_field(name="Membre banni", value=user.name, inline=True)
    embed.add_field(name="Raison", value=reason, inline=True)
    embed.add_field(name="Modérateur", value=ctx.author.name, inline=False)
    embed.set_footer(text=random.choice(funFact))
    await ctx.send(embed=embed)


@bot.command()
async def commandes(ctx):
    embed = discord.Embed(title="***Voici toute les commandes disponible:***", color=0x1bf9ff)
    embed.set_thumbnail(url="https://emoji.gg/assets/emoji/2744-checklist.png")
    embed.add_field(name="__**Affichage-Commandes d'affichage**__",
                    value='**infochaine** : Afficher la chaine de Ruhtra \n **ppp** : Afficher la playlist :"Un pokémon presque parfait" \n **combatabonnes** : Afficher la playlist : "Le combat des abonnés"',
                    inline=False)
    embed.add_field(name="!coucou", value="Faire dire coucu au bot", inline=True)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason=reason)
            await ctx.send(f"{user} à été unban.")
            return
    await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des personnes bannis.")


async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name="Muted",
                                            permissions=discord.Permissions(
                                                send_messages=False,
                                                speak=False),
                                            reason="Creation du role Muted pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages=False, speak=False)
    return mutedRole


async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role

    await createMutedRole(ctx)


@bot.command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"{member.mention} a été mute !")


@bot.command()
@commands.has_permissions(ban_members=True)
async def unmute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason=reason)
    await ctx.send(f"{member.mention} a été unmute")


@bot.command()
async def cuisine(ctx):
    await ctx.send("Envoyez le plat que vous voulez cuisiner")

    def checkMessage(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    try:
        recette = await bot.wait_for("message", timeout=10, check=checkMessage)
    except:
        return
    message = await ctx.send(
        f"La préparation de {recette.content} va commencer. Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
    await message.add_reaction("✅")
    await message.add_reaction("❌")

    def checkEmoji(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (
                str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

    try:
        reaction, user = await bot.wait_for("reaction_add", timeout=10, check=checkEmoji)
        if reaction.emoji == "✅":
            await ctx.send("La recette a démarré")
        else:
            await ctx.send("La recette a bien été annulée")
    except:
        await ctx.send("La recette a été anulée vous avez mis trop de temps a réagir.")


@bot.command()
async def roulette(ctx):
    await ctx.send("La roulette commencera dans 10 secondes. Envoyez \"moi\" dans ce channel pour y participer.")

    players = []

    def check(message):
        return message.channel == ctx.message.channel and message.author not in players and message.content.lower() == "moi"

    try:
        while True:
            participation = await bot.wait_for("message", timeout=10, check=check)
            players.append(participation.author)
            print("Nouveau participant : ")
            await ctx.send(f"**{participation.author.name}** participe au tirage ! Le tirage commence dans 10 secondes")
    except:
        print("Demarrage du tirage")

    gagner = ["nouveau rôle", "ban", "kick", "mute", "gage"]

    await ctx.send("Le tirage va commencer dans 3...")
    await asyncio.sleep(1)
    await ctx.send("2")
    await asyncio.sleep(1)
    await ctx.send("1")
    await asyncio.sleep(1)
    loser = random.choice(players)
    price = random.choice(gagner)
    await ctx.send(f"La personne qui a gagnée un {price} est... ")
    await asyncio.sleep(1)
    await ctx.send("**" + loser.name + "**" + " !")


def isOwner(ctx):
    return ctx.message.author.id == 511977822009688064


@bot.command()
@commands.check(isOwner)
async def private(ctx):
    await ctx.send("Cette commande peut seulement être éffectué par le propriétaire du bot.")


@bot.event
async def on_raw_reaction_add(playload):
    ourMessageID = 871868395820290068

    if ourMessageID == playload.message_id:
        member = playload.member
        guild = member.guild

        emoji = playload.emoji.name
        if emoji == "1️⃣":
            role = discord.utils.get(guild.roles, name="snapchat")
        elif emoji == "2️⃣":
            role = discord.utils.get(guild.roles, name="youtube")
        elif emoji == "3️⃣":
            role = discord.utils.get(guild.roles, name="facebook")
        elif emoji == "4️⃣":
            role = discord.utils.get(guild.roles, name="twitch")
            print("salut ca va")
        await member.add_roles(role)


@bot.event
async def on_raw_reaction_remove(playload):
    ourMessageID = 871868395820290068

    if ourMessageID == playload.message_id:
        guild = await(bot.fetch_guild(playload.guild_id))
        emoji = playload.emoji.name
        if emoji == "1️⃣":
            role = discord.utils.get(guild.roles, name="snapchat")
        elif emoji == "2️⃣":
            role = discord.utils.get(guild.roles, name="youtube")
        elif emoji == "3️⃣":
            role = discord.utils.get(guild.roles, name="facebook")
        elif emoji == "4️⃣":
            role = discord.utils.get(guild.roles, name="twitch")
        member = await guild.fetch_member(playload.user_id)
        if member is not None:
            await member.remove_roles(role)
        else:
            print("member not found")


@bot.command()
async def ya(ctx):
    embed = discord.Embed(title="Rôles",
                          description=":one: snapchat \n 2️⃣ youtube \n :three: facebook \n :four: twitch",
                          color=0xff0000)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("1️⃣")
    await msg.add_reaction("2️⃣")
    await msg.add_reaction("3️⃣")
    await msg.add_reaction("4️⃣")

    await ctx.message.add_reaction("✅")


@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(837242210684633112)
    await channel.send(f"Acceuillons a bras ouvert{member.mention} ! Bienvenue dans ce magnifique serveur ;) .")


@bot.event
async def on_member_remove(member):
    channel = member.guild.get_channel(837242210684633112)
    await channel.send(f"Terrible désillusion nous apprenons le départ de : {member.mention}.")



@bot.command()
async def raid(ctx, heure, code, *, pokemon):
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


codes_amis = {}
codes_amis1 = {}

@bot.command()
async def addcode(ctx):
    if ctx.author.id not in codes_amis :
        await ctx.send("Quel est votre code ami pour Pokémon GO ?")

        def check1(message):
            return message.author == ctx.message.author and message.channel == ctx.channel and message.author.id not in codes_amis
        
        try:
            reponse1 = await bot.wait_for("message", check=check1, timeout=30)
            codes_amis[ctx.author.id] = reponse1.content
            await ctx.send(f"{ctx.author.mention} Votre code ami pour Pokémon GO {reponse1.content} a bien été enregistré")
        except asyncio.TimeoutError:
            await ctx.send("Temps écoulé. Veuillez réessayer.")


        await ctx.send("Quel est votre code ami pour Nintendo Switch ?")

        def check2(message):
            return message.author == ctx.message.author and message.channel == ctx.channel and message.author.id not in codes_amis1
        
        try:
            reponse2 = await bot.wait_for("message", check=check2, timeout=30)
            codes_amis1[ctx.author.id] = reponse2.content
            await ctx.send(f"{ctx.author.mention} Votre code ami pour Nintendo Switch {reponse2.content} a bien été enregistré")
        except asyncio.TimeoutError:
            await ctx.send("Temps écoulé. Veuillez réessayer.")
    else:
        await ctx.send("Vous avez déjà ajouté vos codes")


@bot.command()
async def code(ctx, member: discord.Member):
    if member.id in codes_amis:
        embed = discord.Embed(title="***Codes amis ***", color=0xfcdf76)
        embed.set_author(name=f"{member.display_name}", icon_url=member.display_avatar)
        embed.add_field(name="Code amis pogo", value=f"{codes_amis[member.id]}", inline=True)
        embed.add_field(name="Code amis switch", value=f"{codes_amis1[member.id]}", inline=True)
        await ctx.send(embed=embed)
 
    else:
        await ctx.send("Le code ami de cette personne n'est pas enregistré.")


@bot.command()
async def codepogo(ctx):
    if ctx.author.id in codes_amis:
        await ctx.send("Quel est votre nouveau code ami ?")

        def check2(message):
            return message.author == ctx.message.author and ctx.message.channel == message.channel and message.author.id in codes_amis
        
        try:
            reponse = await bot.wait_for("message", check=check2, timeout=30)
            codes_amis[ctx.author.id] = reponse.content
            await ctx.send(f"{ctx.author.mention} Votre nouveau code ami {reponse.content} a bien été enregistré")
        except asyncio.TimeoutError:
            await ctx.send("Temps écoulé. Veuillez réessayer.")

    else:
        await ctx.send("Vous n'avez pas encore ajouté votre code ami !")


@bot.command()
async def codeswitch(ctx):
    if ctx.author.id in codes_amis1:
        await ctx.send("Quel est votre nouveau code ami ?")

        def check2(message):
            return message.author == ctx.message.author and ctx.message.channel == message.channel and message.author.id in codes_amis
        
        try:
            reponse = await bot.wait_for("message", check=check2, timeout=30)
            codes_amis1[ctx.author.id] = reponse.content
            await ctx.send(f"{ctx.author.mention} Votre nouveau code ami {reponse.content} a bien été enregistré")
        except asyncio.TimeoutError:
            await ctx.send("Temps écoulé. Veuillez réessayer.")

    else:
        await ctx.send("Vous n'avez pas encore ajouté votre code ami !")



@bot.command()
async def rid(ctx, *, pokemon):
    heure = ""
    while heure == "":
        await ctx.send("A quel heure commence le raid ? (00h-23 h)")

        def checkMessage(message):
            return message.author == ctx.message.author and ctx.message.channel == message.channel

        reponse1 = await bot.wait_for("message", check=checkMessage)

        try:
            heure = int(reponse1.content)

        except:
            await ctx.send(":warning: Vous devez rentrer un nombre compris entre 1 et 24 pour les heures!")


    while int(reponse1.content) > 24:
        await ctx.send(":warning: Vous devez rentrer un nombre compris entre 1 et 24 pour les heures! \nA quel heure commence le raid ? (00h-23 h)")

        def checkMessage(message):
            return message.author == ctx.message.author and ctx.message.channel == message.channel

        reponse1 = await bot.wait_for("message", check=checkMessage)

        try:
            int(reponse1.content) < 25

        except:
            await ctx.send("")


    minute = ""
    while minute == "":
        await ctx.send("A combien de minute ? (0-59 min)")

        def checkMessage(message):
            return message.author == ctx.message.author and ctx.message.channel == message.channel

        reponse2 = await bot.wait_for("message", check=checkMessage)

        try:
            minute = int(reponse2.content)
        except:
            await ctx.send(":warning: Vous devez rentrer un nombre compris entre 00 et 59 pour les minutes!")

    while int(reponse2.content) > 60:
        await ctx.send(":warning: Vous devez rentrer un nombre compris entre 00 et 59 pour les minutes! \nA combien de minute ? (0-59 min)")

        def checkMessage(message):
            return message.author == ctx.message.author and ctx.message.channel == message.channel

        reponse2 = await bot.wait_for("message", check=checkMessage)


        try:
           reponse2.content < 60

        except:
            """await ctx.send("")"""
    code = ""
    while code == "":
        await ctx.send("Quel est votre code ami ( xxxxxxxxxxxx )")

        def checkMessage(message):
            return message.author == ctx.message.author and ctx.message.channel == message.channel

        reponse3 = await bot.wait_for("message", check=checkMessage)

        try:
            code = int(reponse3.content)
        except:
            await ctx.send(":warning: Vous devez rentrer des nombres pour le code ami!")

   #messages = await ctx.channel.history(limit=0).flatten()
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
    await ctx.send("Si tu veux particier cliquer sur ✅")
    await ctx.send("Le raid va commencer. Envoyez \"moi\" dans ce channel pour y participer.")

    players = []


    def check(message):
        return message.channel == ctx.message.channel and message.author not in players and message.content.lower() == "moi"

    try:
        while True:
            participation = await bot.wait_for("message",timeout=10, check=check)
            players.append(participation.author.mention)
            print("Nouveau participant : ")
            await ctx.send(f"**{participation.author.name}** participe au raid")
            print(players)
                
    except:
        print("Demarrage du tirage")


        def checkEmoji(reaction, user):
            return ctx.message.author == user and message.id == reaction.message.id and (
                    str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=0, check=checkEmoji)
            if reaction.emoji == "✅":
                await ctx.send("Ta participation a bien été prise en compte")
            else:
                await ctx.send("Le raid a bien été annulé")
                messages = await ctx.channel.history(limit=4).flatten()
                for message in messages:
                    await message.delete(delay=2)
        except:
            '''await ctx.send("La recette a été anulée vous avez mis trop de temps a réagir.")'''

    newembed = discord.Embed(title=f"*** Raid proposé : {pokemon}***", color=0x3300ee)
    newembed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar)
    newembed.set_thumbnail(url=f"{pok()}")
    newembed.add_field(name="**Heure**", value=f"{reponse1.content}H{reponse2.content}", inline=True)
    newembed.add_field(name="Code amis ", value=f"{reponse3.content}", inline=True)
    newembed.add_field(name="Participants ", value=f"{players}", inline=False)
    await message.edit(embed=newembed)

    #print(players)
    #if (players(len)) == 1:
            #return


@bot.command()
async def tst(ctx, raid, heure, code):
    embed = discord.Embed(title=f"** Raid proposé : {raid}**", color=0x3300ee)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar)
    embed.set_thumbnail(url=ctx.author.display_avatar)
    embed.set_image(url="https://www.pokepedia.fr/images/b/b3/Reshiram-NB.png")
    embed.add_field(name="**Heure**", value=heure, inline=True)
    embed.add_field(name="Code amis ", value=code, inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def kiss(mess,mention):
    #messages = await mess.channel.history(limit=1).flatten()
    #for message in messages:
        #await message.delete(delay=0)

    lien = ["https://68.media.tumblr.com/c45d95ee33273be7beb731f6b522623d/tumblr_n34am4scGz1qdmrquo2_500.gif",
               "https://aniyuki.com/wp-content/uploads/2021/07/aniyuki-anime-gif-kiss-34.gif"]

    await mess.channel.send(mention)
    embed = discord.Embed(title=f"Vous recevez un bisous de ***{mess.author.name}*** :sparkling_heart:",color=0x990000)
    embed.set_author(name=mess.author.name, icon_url = mess.author.display_avatar)
    embed.set_image(url=random.choice(lien))
    await mess.send(embed=embed)


@bot.command()
async def nrv(mess,mention):
   # messages = await mess.channel.history(limit=1).flatten()
    #for message in messages:
        #await message.delete(delay=0)

    await mess.channel.send(mention)
    embed = discord.Embed(title=f"Vous avez énervé ***{mess.author.name}*** :rage:")
    embed.set_author(name=mess.author.name, icon_url=mess.author.display_avatar)
    embed.set_image(url="https://i.pinimg.com/originals/64/52/02/645202ed4daa782a29507d82546a9829.gif")
    await mess.send(embed=embed)


badwords = ["Fly", "fly", "vole", "avion", "fl y", "f l y", "a v i o n"]

@bot.event
async def on_message(message):

    for i in badwords:
      if i in message.content.lower():
          await message.delete()
          await message.channel.send(message.author.mention)
          embed = discord.Embed(title="Avertissement", description=" *** Raison : *** Utilisation de mots interdit !",
                                color=0x3300ee)
          embed.set_author(name=message.author.name, icon_url=message.author.display_avatar)
          embed.set_thumbnail(url = "https://cdn.discordapp.com/emojis/1233814300842262558.webp?size=96&quality=lossless")
          await message.channel.send(embed=embed)

    if "bonjour" in message.content:
        await message.add_reaction("👍")
    if "salutation" in message.content:
        await message.add_reaction("👍")
    if "shiny" in message.content:
        await message.add_reaction("✅")
    #if message.author.name == f"r0mric":
        #await message.add_reaction("❤️")
    await bot.process_commands(message)


bot.run("MTIzMzUzNjM2MTc0NzcxNDE3MA.GxnMTn.iS8xGwbkiXo2pbpdg8lbyife0zUGxncW0XHRIM")