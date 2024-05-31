import discord

class PlayView(discord.ui.View):
    def get_content(self):
        image_url = 'https://postimg.cc/jwFbWCYT'

        welcome_message = '''Hey MUA fam!  Welcome aboard! Feel free to @mua42bot with any questions about MUA DAO. 

We're here to build, HODL, and have a blast together. Dive in, get involved, and let's create more Mua~ Mua~ miracles! '''
        return image_url + welcome_message