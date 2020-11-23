import discord, random
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
    await ctx.send(f'Your ping is: {round(client.latency * 1000)}ms')

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
async def cb(ctx):
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
            .ping - Check your Latency with Basilisk.
            .8Ball (question) - Will respond with an answer to your question.
            .flip - Coin Flip (Heads/Tails)
            .plang - Random Programming Langauge
            .source - Link to this bots GitHub Page.
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
    await ctx.send(':heart:')

client.run(TOKEN)








