import discord, random, requests, time
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
client.remove_command('help')
global outputPorts
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('with your messages'))
    print("Bot is online!")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please pass in all required arguments!")



@client.command()
async def ping(ctx):
    await ctx.send(f'Bot Latency: {round(client.latency * 1000)}ms')

@client.command()
async def patch(ctx):
    patchNotes = discord.Embed(description=("Fixed .ip2\nAdded more quotes to .skid\nMade .help look a lot better\nAdded .slots (See .help for more info)\nAdded this command (.patch)\n"))
    await ctx.send(embed=patchNotes)


@client.command(aliases=['8ball', 'eightball', 'Eightball', 'EightBall'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]

    await ctx.send(f'Question: "{question}"\n\n8Ball: {random.choice(responses)}')

@client.command()
async def delmsg(ctx, amount=2):
    if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send('Sorry, you are not permitted to use this command.')

@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    if (ctx.message.author.permissions_in(ctx.message.channel).kick_members):
        await member.kick(reason=reason)
        await ctx.send(f'Successfully kicked {member}!')
    else:
        await ctx.send('Sorry, you are not permitted to use this command.')


@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    if (ctx.message.author.permissions_in(ctx.message.channel).ban_members):
        await member.ban(reason=reason)
        await ctx.send(f'Successfully banned {member}!')
    else:
        await ctx.send('Sorry, you are not permitted to use this command.')

@client.command()
async def unban(ctx, *, member):
    if (ctx.message.author.permissions_in(ctx.message.channel).ban_members):
	    banned_users = await ctx.guild.bans()
	
	    member_name, member_discriminator = member.split('#')
	    for ban_entry in banned_users:
		    user = ban_entry.user
		
		    if (user.name, user.discriminator) == (member_name, member_discriminator):
 			    await ctx.guild.unban(user)
 			    await ctx.channel.send(f"Unbanned: {user.mention}")
    else:
        await ctx.send('Sorry, you are not permitted to use this command.')

@client.command()
async def source(ctx):
    githublink = "https://github.com/dean0coin/basiliskbot/"
    await ctx.send("You can check out this bots source code at "+githublink)

@client.command()
async def bsaycli(ctx):
    if (ctx.message.author.permissions_in(ctx.message.channel).administrator):
        message = input("Message to send: ")
        await ctx.send(message)
    else:
        await ctx.send('Sorry, you are not permitted to use this command.')

  
@client.command()
async def help(ctx):
    helpMenu = discord.Embed(description=(".ping - Check Basilisks Latency.\n.patch - See Basilisk's new patch notes!\n.8Ball (question) - Will respond with an answer to your question. -- Aliases: .eightball, .Eightball, .EightBall\n.slots - Emulates a slot machine\n.flip - Coin Flip (Heads/Tails).\n.plang - Random Programming Langauge.\n.ip2 (IP) - Performs IP Lookup. -- Aliases: .ipscan, .iplookup, .iplook\n.skid - Outputs random skiddie quote. -- Aliases: .skiddie, .scriptkiddie\n.test - Used to test if bot is online.\n.source - Link to this bots GitHub Page.\n.math - Example of Use: .math 5 + 10\nRock Paper Scissors: .rock/.paper/.scissors - Plays Rock Paper Scissors with you.\n.randnum - Random number between two numbers. Example - .randnum 1 20\n.help - This Menu."))
    await ctx.send(embed=helpMenu)

@client.command()
async def flip(ctx):
    coin = ['Heads', 'Tails']
    await ctx.send(":coin: "+random.choice(coin)+" :coin:")

@client.command()
async def plang(ctx):
    allLangs = ['Ada', 'ALGOL', 'C', 'C++', 'C#', 'CLEO', 'COBOL', 'Cobra', 'D', 'DASL', 'DIBOL', 'Fortran', 'Java', 'JOVIAL', 'Objective-C', 'SMALL', 'Smalltalk', 'Turing',
     'Visual Basic', 'XL', 'AppleScript', 'Awk', 'BeanShell', 'ColdFusion', 'F-Script', 'JASS', 'Maya Embedded Language', 'Mondrian', 'PHP', 'Revolution', 'Tcl', 'VBScript', 
     'Windows PowerShell', 'Curl', 'SGML', 'HTML', 'XML', 'XHTML', 'Agora', 'BETA', 'Cecil', 'Lava', 'MOO', 'Moto', 'Object-Z', 'Obliq', 'Oxygene', 'Prograph', 'REBOL', 'Scala',
     'Self', 'Slate', 'XOTcl', 'IO', 'JavaScript', 'Python', 'R']
    await ctx.send(random.choice(allLangs))
    
@client.command()
async def vortex(ctx):
    invChance = [0, 1]
    invSend = random.choice(invChance)
    if invSend == 0:
        await ctx.send(':heart:')
    elif invSend == 1:
        await ctx.send(':heart:', 'https://discord.gg/dprJ49eXX4', ':heart:')

@client.command()
async def test(ctx):
    await ctx.send("Bot is Online!")

@client.command(aliases=['ipscan', 'iplookup', 'iplook'])
async def ip2(ctx, host):
    try:
        r = requests.get(f"http://ip-api.com/json/{host}?fields=country,regionName,city,isp,mobile,proxy,query")
        geo = r.json()
        query = geo["query"]
        isp = geo["isp"]
        city = geo["city"]
        region = geo["regionName"]
        country = geo["country"]
        proxy = geo["proxy"]
        mobile = geo["mobile"]
        embed = discord.Embed(description=(f"Host: {query}\nISP: {isp}\nCity: {city}\nRegion: {region}\nCountry: {country}\VPN/Proxy: {proxy}\nMobile: {mobile}"))
        embed.set_author(name=(query))
        await ctx.send(embed=embed)
    except:
        ipNo = discord.Embed(description=("That is not a valid IP Address!"))
        await ctx.send(embed=ipNo)
@client.command()
async def bsay(ctx, *, message):
    await ctx.channel.purge(limit=1)
    await ctx.send(message)

@client.command(aliases=['skiddie', 'scriptkiddie'])
async def skid(ctx):
    skidSaysLst = ['can somebody help me with Hydra-Gtk please', 'guys I found this ddos script it DDoSes at like 100KB/s',
    'whats programming?', 'who wants my cracking pack?', 'giving away a free credit card', 'whats a botnet?',
    'im not a kid! wait whats a skid then?', 'just cracked 20 new renegade raiders', 'bro ill legit fry your router',
    'what botnet do I use? Stressthem ofc', 'stop laughing just tell me what a linux is', 
    'ofc i use windows what else is there? mac haha', 'how is an operating system california??', 'i use windows btw',
    'whats an arch and why do you keep telling us you use it?', 'ugh this script stopped working',
    'whats a python?', 'whats a java? can you send me the script', 'who wants this new account checker??', 'yea i know what hacking is! i have the new fortnite crack tool',
    'dont mess with me ill crack your fortnite account', 'i can legit dox u', 'bro ill get ur ip i have wireshark', 'wdym dos and ddos are different thing? no they arent',
    'windows is the best operating system', 'of course i play fortnite']
    skidSays = random.choice(skidSaysLst)
    await ctx.send(skidSays)

#---------------Rock Paper Scissors---------------#
@client.command()
async def rock(ctx):
    rpsC = "Rock"
    rps = ["Rock", "Paper", "Scissors"]
    rpsS = random.choice(rps)
    if rpsS == rpsC:
        await ctx.send(rpsS)
        await ctx.send("Tie!")
    elif rpsS == "Paper":
        await ctx.send(rpsS)
        await ctx.send("lol u suck")
    elif rpsS == "Scissors":
        await ctx.send(rpsS)
        await ctx.send("bro ur haxxing wtf")

@client.command()
async def paper(ctx):
    rpsC = "Paper"
    rps = ["Rock", "Paper", "Scissors"]
    rpsS = random.choice(rps)
    if rpsS == rpsC:
        await ctx.send(rpsS)
        await ctx.send("Tie!")
    elif rpsS == "Scissors":
        await ctx.send(rpsS)
        await ctx.send("lol u suck")
    elif rpsS == "Rock":
        await ctx.send(rpsS)
        await ctx.send("bro ur haxxing wtf")

@client.command()
async def scissors(ctx):
    rpsC = "Scissors"
    rps = ["Rock", "Paper", "Scissors"]
    rpsS = random.choice(rps)
    if rpsS == rpsC:
        await ctx.send(rpsS)
        await ctx.send("Tie!")
    elif rpsS == "Rock":
        await ctx.send(rpsS)
        await ctx.send("lol u suck")
    elif rpsS == "Paper":
        await ctx.send(rpsS)
        await ctx.send("bro ur haxxing wtf")
#---------------Rock Paper Scissors---------------#

@client.command()
async def basilisk(ctx):
    await ctx.send("That's me!")

@client.command()
async def math(ctx, x, s, y):
    x = float(x)
    y = float(y)
    if s == '+':
        mDone = x+y
    elif s == '-':
        mDone = x-y
    elif s == '*':
        mDone = x*y
    elif s == '/':
        mDone = x/y
    else:
        await ctx.send("That isn't a valid operator")

    mDone = str(mDone)
    if len(mDone) > 99:
        await ctx.send("You cannot pass in a math problem where the answer is longer than 100 characters!")
    else:
        await ctx.send(mDone)

@client.command()
async def joke(ctx):
    await ctx.send("This command isn't ready yet!")

@client.command()
async def randnum(ctx, x, y):
    x = int(x)
    y = int(y)
    randInt = random.randint(x, y)
    randInt = str(randInt)
    if len(randInt) > 99:
        await ctx.send("You cannot generate a number longer than 100 characters!")
    else:
        await ctx.send(randInt)


@client.command()
async def slots(ctx):
    slotOptions = [':tangerine:', ':tangerine:', ':tangerine:', ':tangerine:', ':tangerine:', ':strawberry:', ':strawberry:', ':lemon:']


    sChances = discord.Embed(description=("Highest chance of winning: :tangerine:\nLowest Chance: :lemon:\nIn the middle: :strawberry:\n"))
    await ctx.send(embed=sChances)
    #Spin 1
    spin1 = discord.Embed(description=("Spinning first Slot..."))
    await ctx.send(embed=spin1)
    time.sleep(1)
    slotChoice1 = random.choice(slotOptions)
    land1 = discord.Embed(description=(f"Landed on {slotChoice1}"))
    await ctx.send(embed=land1)

    #Spin 2
    spin2 = discord.Embed(description=("Spinning second Slot..."))
    await ctx.send(embed=spin2)
    time.sleep(1)
    slotChoice2 = random.choice(slotOptions)
    land2 = discord.Embed(description=(f"Landed on {slotChoice2}"))
    await ctx.send(embed=land2)

    #Spin 3
    spin3 = discord.Embed(description=("Spinning third Slot..."))
    await ctx.send(embed=spin3)
    time.sleep(1)
    slotChoice3 = random.choice(slotOptions)
    land3 = discord.Embed(description=(f"Landed on {slotChoice3}"))
    await ctx.send(embed=land3)


    if slotChoice1 == ':tangerine:' and slotChoice2 == ':tangerine:' and slotChoice3 == ':tangerine:':
        await ctx.send("tf how'd u win ur hacking")
    elif slotChoice1 == ':strawberry:' and slotChoice2 == ':strawberry:' and slotChoice3 == ':strawberry:':
        await ctx.send("tf how'd u win ur hacking")
    elif slotChoice1 == ':lemon:' and slotChoice2 == ':lemon:' and slotChoice3 == ':lemon:':
        await ctx.send("tf how'd u win ur hacking")
    else:
        await ctx.send("lmao rekt")

	
client.run(TOKEN)








