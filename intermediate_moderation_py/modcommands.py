import discord
import datetime
from discord.ext import commands
from discord.utils import get

class ModCommandsCog(commands.Cog, name="Moderation Commands"):
    def __init__(self, bot):
        self.bot = bot
        self.log_chnl = 'bot-logs'
        self.muted_role = 'Muted'

    #Kick
    @commands.command()
    @commands.has_role('Moderator')
    async def kick(self, ctx, user: discord.User, *args):
        if len(args) >= 1:
            reason = ' '.join(args)
        else:
            reason = 'No reason provided'

        await ctx.message.guild.kick(user, reason=reason)

        embed = discord.Embed(title='User Kicked', color=0xff6666)
        embed.add_field(name='Username', value=f'{user.name}\n{user.id}', inline=False)
        embed.add_field(name='Reason', value=reason, inline=False)
        embed.add_field(name='Kicked by', value=f'{ctx.message.author.name}\n({ctx.message.author.id})', inline=False)
        embed.set_footer(text=datetime.datetime.now().replace(microsecond=0).isoformat())
        
        log_chnl = get(ctx.message.guild.channels, name=self.log_chnl, type=discord.ChannelType.text)
        await log_chnl.send(embed=embed)

    #Ban
    @commands.command()
    @commands.has_role('Moderator')
    async def ban(self, ctx, user: discord.User, *args):
        if len(args) >= 1:
            reason = ' '.join(args)
        else:
            reason = 'No reason provided'

        await ctx.message.guild.ban(user, reason=reason)

        embed = discord.Embed(title='User Banned', color=0xff6666)
        embed.add_field(name='Username', value=f'{user.name}\n({user.id})', inline=False)
        embed.add_field(name='Reason', value=reason, inline=False)
        embed.add_field(name='Banned by', value=f'{ctx.message.author.name}\n({ctx.message.author.id})', inline=False)
        embed.set_footer(text=datetime.datetime.now().replace(microsecond=0).isoformat())
        
        log_chnl = get(ctx.message.guild.channels, name=self.log_chnl, type=discord.ChannelType.text)
        await log_chnl.send(embed=embed)
    
    #Unban
    @commands.command()
    @commands.has_role('Moderator')
    async def unban(self, ctx, user: discord.User, *args):
        if len(args) >= 1:
            reason = ' '.join(args)
        else:
            reason = 'No reason provided'

        await ctx.message.guild.unban(user, reason=reason)

        embed = discord.Embed(title='User Unbanned', color=0x00ff00)
        embed.add_field(name='Username', value=f'{user.name}\n({user.id})', inline=False)
        embed.add_field(name='Reason', value=reason, inline=False)
        embed.add_field(name='Unbanned by', value=f'{ctx.message.author.name}\n({ctx.message.author.id})', inline=False)
        embed.set_footer(text=datetime.datetime.now().replace(microsecond=0).isoformat())
        
        log_chnl = get(ctx.message.guild.channels, name=self.log_chnl, type=discord.ChannelType.text)
        await log_chnl.send(embed=embed)
    
    #Mute
    @commands.command()
    @commands.has_role('Moderator')
    async def mute(self, ctx, user: discord.Member, *args):
        if len(args) >= 1:
            reason = ' '.join(args)
        else:
            reason = 'No reason'
        
        muted_role = get(ctx.message.guild.roles, name=self.muted_role)
        await user.add_roles(muted_role, reason=reason)

        embed = discord.Embed(title='User Muted', color=0x808080)
        embed.add_field(name='Username', value=f'{user.name}\n({user.id})', inline=False)
        embed.add_field(name='Reason', value=reason, inline=False)
        embed.add_field(name='Muted by', value=f'{ctx.message.author.name}\n({ctx.message.author.id})', inline=False)
        embed.set_footer(text=datetime.datetime.now().replace(microsecond=0).isoformat())
        
        log_chnl = get(ctx.message.guild.channels, name=self.log_chnl, type=discord.ChannelType.text)
        await log_chnl.send(embed=embed)

    #Unmute
    @commands.command()
    @commands.has_role('Moderator')
    async def unmute(self, ctx, user: discord.Member, *args):
        if len(args) >= 1:
            reason = ' '.join(args)
        else:
            reason = 'No reason'
        
        muted_role = get(ctx.message.guild.roles, name=self.muted_role)
        await user.remove_roles(muted_role, reason=reason)

        embed = discord.Embed(title='User Unmuted', color=0x00ff00)
        embed.add_field(name='Username', value=f'{user.name}\n({user.id})', inline=False)
        embed.add_field(name='Reason', value=reason, inline=False)
        embed.add_field(name='Unmuted by', value=f'{ctx.message.author.name}\n({ctx.message.author.id})', inline=False)
        embed.set_footer(text=datetime.datetime.now().replace(microsecond=0).isoformat())
        
        log_chnl = get(ctx.message.guild.channels, name=self.log_chnl, type=discord.ChannelType.text)
        await log_chnl.send(embed=embed)

    #Purge
    @commands.command()
    @commands.has_role('Moderator')
    async def purge(self, ctx, num):
        await ctx.message.channel.purge(limit=int(num))


def setup(bot):
    bot.add_cog(ModCommandsCog(bot))