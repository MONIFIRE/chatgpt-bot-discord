import discord
from langdetect import detect
from connect_openai import chatgpt_response
from discord.ext import commands
from discord_slash import SlashCommand


bot = commands.Bot(command_prefix='/')
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='friends talk', url='https://www.twitch.tv/OTAKO'))
print('We have logged in as {0.user}'.format(bot))

@slash.slash(name="OTAKO", description="ข้อความ")
async def ChatGPT(ctx, messages):
    language = detect(messages)
    if language != 'ja':
         await ctx.send("**โปรดใช้ภาษาญี่ปุ่นในการสนทนา :D**")
    else:
         response = f"{chatgpt_response(messages)}"
         await ctx.send(f"**{response}**")
        

        

if __name__ == '__main__':

    TOKEN = bot.run('MTAzNjAwNjAwMDY2ODQ2MzExNA.Gwr525.Ehr9czPT7wS7o9CFROmWJm2hwdA76wDiRiqqXQ')
