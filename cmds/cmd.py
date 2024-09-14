import discord
from discord.ext import commands
from core.core import Cog_Extension
from oksana.oksana import clear_chat
from datetime import datetime
import asyncio

class cmds(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def avatar(self, ctx, member: discord.User = None):
        if member == None:
            member = ctx.author
        embed = discord.Embed(title=f"{member.name}的頭貼", color=0x00ff00)
        embed.set_image(url=member.avatar)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def clear_chat(self, ctx):
      res = clear_chat(str(ctx.channel.id))
      if res:
        await ctx.send('已清除')
      else:
        await ctx.send('沒有記錄可以清除')

    async def reminder(self, ctx, reminder_message, delay):
        print('等等提醒')
#        await asyncio.sleep(delay)
        for i in range(1, int(delay)+1):
            if i == delay:
              print('提醒！')
              await ctx.send(f"{ctx.author.mention}, 這是你的提醒：{reminder_message}")
              break
            else:
              print('提醒？')
            await asyncio.sleep(1)

    # 指定日期和時間設置提醒
    @commands.command()
    async def remindme(self, ctx, date:str, time: str, *, message: str):
        # 解析使用者輸入的日期時間 (格式: YYYY-MM-DD HH:MM)
        try:
            date_time = f'{date} {time}'
            target_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
            now = datetime.now()

            # 計算當前時間與目標時間之間的差
            delay = (target_time - now).total_seconds()

            # 如果目標時間在過去，則無法設置提醒
            if delay <= 0:
                await ctx.send(f"{ctx.author.mention}, 指定的時間已經過去了，請輸入未來的時間。")
            else:
                self.bot.loop.create_task(self.reminder(ctx, message, delay))

                await ctx.send(f"好的！{ctx.author.mention}，我會在 {date_time} 提醒你。")
        except ValueError:
            await ctx.send(f"請輸入正確的日期和時間格式，例如：2024-09-08 15:30")

async def setup(bot):
    await bot.add_cog(cmds(bot))