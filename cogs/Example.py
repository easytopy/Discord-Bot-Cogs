from discord.ext import commands
from discord import app_commands
import discord
class Example(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog 준비 완료")
        await self.bot.tree.sync()

    @app_commands.command(name="test", description="테스트 명령어입니다.")
    async def create_post(self, interaction: discord.Interaction):
       
        await interaction.response.send_message("test", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Example(bot))