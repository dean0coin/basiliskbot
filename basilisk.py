import discord, random, pygeoip
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
    await ctx.send('''
            **Help Menu**
            ```Commands:
            .ping - Check Basilisks Latency.
            .8Ball (question) - Will respond with an answer to your question. -- Aliases: .eightball, .Eightball, .EightBall
            .flip - Coin Flip (Heads/Tails).
            .plang - Random Programming Langauge.
            .ip2 (IP) - Performs IP Lookup. -- Aliases: .ipscan, .iplookup, .iplook
            .skid - Outputs random skiddie quote. -- Aliases: .skiddie, .scriptkiddie
            .test - Used to test if bot is online.
            .source - Link to this bots GitHub Page.
            Rock Paper Scissors: .rock/.paper/.scissors - Plays Rock Paper Scissors with you.
            .help - This Menu.
            ```
    ''')

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
async def ip2(ctx, ip):
    gip = pygeoip.GeoIP('GeoLiteCity.dat')
    res = gip.record_by_addr(ip)
    for key,val in res.items():
	    await ctx.send('%s : %s' % (key,val))

@client.command()
async def bsay(ctx, message=""):
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
    'whats a python?', 'whats a java? can you send me the script']
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
client.run(TOKEN)








