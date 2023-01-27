import discord
import discord as ds
token='ODk0OTc4NzQ3MzkwODk0MTYw.YVx36Q.y2XvtaCeEY9xwI8W80bn32R6Eig'
intents = ds.Intents.all()
perm = ds.Permissions.all()
intents.members=True
perm.ban_members=True
perm.kick_members=True
client=ds.Client(intents=intents, permissions=perm)
role_message_id=902573047473655888
emoji_to_role={
    discord.PartialEmoji(name='🥱'):902571454497951845,
    discord.PartialEmoji(name='😎'):902571547624083466
}
channel=''
answers={'!прив':'Дароу', # dialog=1
        '!как дела':'Та вот один кожаный пришёл, говорить хочет',
        '!поиграем':'Го, только я хз во что'}
howareyou={'!как дела':'Та норм, а ты как, мой кожаный друг?', # dialog=2
           '!ок':'ок',
           '!так себе':'живи, брат',
           '!плохо':'соболезную бро',
           '!норм':'ок, не выключай меня бро',
           '!по кайфу':'класс, и у меня',
           '!отлично':'красава',
           }
@client.event
async def on_ready():
    print('hello gays, my name is: '+str(client.user.name)+', my id is: '+str(client.user.id))
@client.event
async def on_raw_reaction_add(payload=discord.RawReactionActionEvent): #...ADD ROLE...
    global role_message_id,emoji_to_role
    guild=client.get_guild(payload.guild_id)
    if payload.message_id == role_message_id and guild != None:
        try:
            role_id=emoji_to_role[payload.emoji]
        except KeyError:
            print('not such role as: '+str(payload.emoji))
            return
        if guild.get_role(role_id) != None:
            await payload.member.add_roles(guild.get_role(role_id))

@client.event
async def on_raw_reaction_remove(payload=discord.RawReactionActionEvent): #...REMOVE ROLE...
    global role_message_id,emoji_to_role
    guild = client.get_guild(payload.guild_id)
    if payload.message_id == role_message_id and guild != None:
        try:
            role_id=emoji_to_role[payload.emoji]
        except KeyError:
            print('not such role as: '+str(payload.emoji))
            return
        if guild.get_role(role_id) != None:
            member=guild.get_member(payload.user_id)
            await member.remove_roles(guild.get_role(role_id))

@client.event
async  def on_message(message):

    global channel
    def checkfunc(x):
        return x.channel==channel

    channel=message.channel
    print(message.content)
    if str.lower(message.content).startswith('!ban'):
        words=message.content.split(' ')
        for mem in client.get_all_members():
            print(str(mem))
            print(str(words[1]))
            if str(mem)==str(words[1]):
                await channel.send('лови бан, лох')
                await mem.ban(reason='ban, потому что потому', delete_message_days=1)
    if str.lower(message.content).startswith('!kick'):
        words=message.content.split(' ')
        for mem in client.get_all_members():
            print(str(mem))
            print(str(words[1]))
            if str(mem)==str(words[1]):
                await channel.send('лови kik, лох')
                await mem.kick(reason='kik, потому что потому')
    elif message.content[0]=='!':
        for key in answers.keys():
            if message.content.lower().startswith(key):
                if key=='!как дела':
                    await channel.send(howareyou[key])
                    ans= await client.wait_for('answer', check=checkfunc)
                    for answr in howareyou:
                        if ans.lower().startswith(answr):
                            await channel.send(howareyou[answr])
                elif message.content.lower() in answers:
                    await channel.send(answers[key])
                else:
                    await channel.send('опять бред не панимаю твой')

client.run(token)