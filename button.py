import discord

# class PlayView(discord.ui.View):
#     @discord.ui.button(label="Twitter",emoji="🐦", style=discord.ButtonStyle)
#     async def twitter_button(self, interaction: discord.Interaction, button: discord.ui.button):
#         await interaction.

class URLButton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(discord.ui.Button(label="🐦 Twitter", url="https://x.com/MUA_MUADAO",row=0))
        self.add_item(discord.ui.Button(label="👥 Discord", url="https://discord.gg/mua-dao",row=0))
        self.add_item(discord.ui.Button(label="📔 Medium", url="https://medium.com/@muadao",row=0))
        self.add_item(discord.ui.Button(label="💬 Gitbook", url="https://docs.muadao.build/mua-dao/",row=1))
        self.add_item(discord.ui.Button(label="🌐 Website", url="https://muadao.build",row=1))