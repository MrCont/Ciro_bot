import mp3
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import random
from gtts import gTTS
token = input("Insert bot token")
def dillo_in_napoletano(_str):
    return gTTS(_str,lang="it")
bot = commands.Bot(command_prefix=">")

with open("proverbi_sfaccimm.txt","r",encoding="utf-8") as f:
    lines = f.readlines() 
    lines = list(lines)
    
@bot.event
async def on_ready():
    print ("Ready")

@bot.command(pass_context=True)
async def join(ctx):
    if  (ctx.author.voice):
        channel=ctx.message.author.voice.channel
        global voice
        voice = await channel.connect()
    else:
        await ctx.send("not in a voice channel")

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command()
async def proverbio(ctx):
    msg=dillo_in_napoletano("O' proverbio dice:"+random.choice(lines)[4:])
    msg.save("msg.mp3")
    print("playing msg")
    source = FFmpegPCMAudio(executable="ffmpeg.exe", source="msg.mp3")
    voice.play(source)
    
bot.run(token)

