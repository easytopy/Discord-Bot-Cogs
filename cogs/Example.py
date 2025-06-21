from discord.ext import commands
from discord import app_commands
import discord

class ButtonExample(discord.ui.View):
    def __init__(self, ctx):
        super().__init__(timeout=150)
        self.ctx = ctx
    
    @discord.ui.button(label="예시버튼", style=discord.ButtonStyle.gray)
    async def example_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.userid == interaction.user.id:
            print(1)
        else:
            pass
    
    async def on_timeout(self) -> None:
        try:
            await self.message.edit(content="타임 아웃",view=None)
        except:
            pass
class ModalExample(discord.ui.Modal, title="모달 제목"):
    input_example = discord.ui.TextInput(label="입력하세요.", style=discord.TextStyle.short)
    async def on_submit(self, interaction: discord.Interaction):
        print(1)

class SelectOptionExample(discord.ui.View):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx

        self.select = discord.ui.Select(
            placeholder="예 혹은 아니요를 선택하세요",
            options=[
                discord.SelectOption(label="1", description="설명", value="1"),
                discord.SelectOption(label="2", description="설명",value="2")
            ])
        self.add_item(self.select)
        self.select.callback = self.callback_selectoption

    async def callback_selectoption(self, interaction: discord.Interaction):
        if self.userid == interaction.user.id:
            print(1)
        else:
            pass

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