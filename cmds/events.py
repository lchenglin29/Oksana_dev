import discord
from discord.ext import commands
from core.core import Cog_Extension
from oksana.oksana import calling_Oksana
from oksana.koala import calling_Koala
from oksana.internet import extract_urls,get_html


class event(Cog_Extension):
  @commands.Cog.listener()
  async def on_message(self,message):
    if message.author == self.bot.user:
      return
    if self.bot.user.mention in message.content or isinstance(message.channel,discord.DMChannel):
      if message.content == "d!clear_chat":
          return
      user_message = message.content.replace(f'<@{self.bot.user.id}>','Oksana')
      urls = extract_urls(user_message)
      html = {}
      for url in urls:
        try:
          html[url] = get_html(url)
        except Exception as e:
          print(e)
      if len(html) > 0:
        for ht in html:
          user_message += f"\n{ht}:\n{html[ht]}"
      await message.channel.typing()
      try:
        await message.reply(calling_Oksana(f"{message.author.name}：{user_message}",message.channel.id,message=message))
      except Exception as e:
        await message.reply("-# this message has been filtered\n-# 這則訊息已被過濾")
        print(e)
    if message.content.startswith("k@a"):
      await message.channel.typing()
      msg = calling_Koala(f"{message.author.name}：{message.content[3:]}",message.channel.id)
      if msg.count("\n") < 10:
        msgs = msg.split("\n")
        for m in msgs:
          try:
            await message.channel.send(m)
          except:
            continue
      else:
        try:
          await message.channel.send(msg)
        except:
          await message.channel.send("-# Hmmm.Something went wrong.")
      pass
  @commands.Cog.listener()
  async def on_member_join(self,member:discord.Member):
    channel = self.bot.get_channel(1202596441088987156)
    if member.guild.id == 1202596440535343154:
      pass
#      await channel.send(f'{member.mention}，歡迎來到{member.guild.name}！\n你可以看 <#1202599065318326272> 了解O-bot的玩法\n若要開始遊戲，請到 <#1203004488340742214> 使用指令！')

async def setup(bot):
    await bot.add_cog(event(bot))
 
