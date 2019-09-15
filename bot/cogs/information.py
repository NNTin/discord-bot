import aiohttp
from datetime import datetime as dt
from http.client import responses

import discord
from discord.ext import commands
from discord import Embed, Color

from bot.paginator import Paginator

from typing import Optional
from bot.constants import Lang, NEWLINES_LIMIT, CHARACTERS_LIMIT, Emoji, JUDGE0_ICON, START_TIME


class Information(commands.Cog):
    """
    Represents instance of a Cog for retrieving judge0 API information.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        uptime = int((dt.utcnow() - START_TIME).total_seconds())
        d, h = divmod(uptime, 86400)
        h, m = divmod(h, 3600)
        m, s = divmod(m, 60)
        
        owner = (await self.bot.application_info()).owner
        embed = Embed(
                      title='Judge0Bot',
                      url='https://discordbots.org/bot/620609604295852033',
                      timestamp=dt.utcnow(),
                      description="Discord bot for running code in the chat through the Judge0 API.")

        embed.set_author(name=f'{ctx.author} request',
                    icon_url=ctx.author.avatar_url)
        embed.add_field(name='Bot',
                        value=(f'Uptime: {d}d {h}h {m}m {s}s\n'
                               f'Servers connected: {len(self.bot.guilds)}\n'
                               f'Unique users: {len(self.bot.users)}'),
        )   
        embed.add_field(name='Links',
                        value=(f'[Bot invite](https://discordapp.com/oauth2/authorize?client_id=620609604295852033&scope=bot&permissions=0)\n'
                               f'[Bot repo](https://github.com/judge0/discord-bot)\n'
                               f'[Support server](https://discord.gg/fbty4Rk)'),
        )
        embed.add_field(name='Judge0',
                        value=(f'[Website](https://judge0.com/)\n'
                               f'[Github](https://github.com/judge0)\n'
                               f'[Creator](https://hermanz.dosilovic.com/)'
                               )
        )
        embed.add_field(name='Project',
                        value=(f'[Library](https://github.com/Rapptz/discord.py/)\n'
                               f'[Hosting](https://www.digitalocean.com/)\n'
                               f'[Developer](https://github.com/skilldeliver)')
        )
        embed.set_thumbnail(url=JUDGE0_ICON)
        embed.set_footer(text=f'Main Bot Developer - {owner}', icon_url=owner.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def workers(self, ctx):
        """Returns health check information about the workers."""
        base_url = "https://api.judge0.com/workers"

        async with aiohttp.ClientSession() as cs:
            async with cs.get(base_url) as r:
                if r.status not in [200, 201, 500]:
                    await ctx.send(f"{r.status} {responses[r.status]}")
                    return

                data = (await r.json())[0]
        embed = Embed(timestamp=dt.utcnow(), title='Workers Health Check')

        embed.set_author(name=f'{ctx.author} request',
                         icon_url=ctx.author.avatar_url)
        
        embed.add_field(name=f"{Emoji.available} Available", value=data['available'])
        embed.add_field(name=f"{Emoji.idle} IDLE", value=data['idle'])
        embed.add_field(name=f"{Emoji.total} Total", value=data['total'])
        embed.add_field(name=f"{Emoji.working} Working", value=data['working'])
        embed.add_field(name=f"{Emoji.paused} Paused", value=data['paused'])
        embed.add_field(name=f"{Emoji.failed} Failed", value=data['failed'])

        await ctx.send(embed=embed)

    @commands.command(aliases=['sys'])
    async def system(self, ctx):
        """Returns info about system on which Judge0 API is running."""
        base_url = "https://api.judge0.com/system_info"

        async with aiohttp.ClientSession() as cs:
            async with cs.get(base_url) as r:
                if r.status not in [200, 201]:
                    await ctx.send(f"{r.status} {responses[r.status]}")
                    return
                data = (await r.json())


        alist = [list(data)[x:x+5] for x in range(0, len(data),5)]
        pages = list()

        for item in alist:
            embed = Embed(timestamp=dt.utcnow(),
                          title='System Info')
            embed.set_author(name=f'{ctx.author} request',
                            icon_url=ctx.author.avatar_url)
            
            for k in item:
                embed.add_field(name=k, value=data[k], inline=False)
            pages.append(embed)
    
        paginator = Paginator(self.bot, ctx, pages, 30)
        await paginator.run()

    @commands.command()
    async def languages(self, ctx):
        """Returns a list of all languages supported by the Judge0 API."""
        base_url = "https://api.judge0.com/languages"
    
        async with aiohttp.ClientSession() as cs:
            async with cs.get(base_url) as r:
                if r.status not in [200, 201]:
                    await ctx.send(f"{r.status} {responses[r.status]}")
                    return
                data = (await r.json())

        alist = [data[x:x+10] for x in range(0, len(data),10)]
        pages = list()

        for item in alist:
            description = '\n'.join(f'**{i["id"]}.** {i["name"]}' for i in item)
            embed = Embed(timestamp=dt.utcnow(),
                        title='Languages List',
                        description=description)
            embed.set_author(name=f'{ctx.author} request',
                            icon_url=ctx.author.avatar_url)
            pages.append(embed)

        paginator = Paginator(self.bot, ctx, pages, 30)
        await paginator.run()

def setup(bot):
    bot.add_cog(Information(bot))