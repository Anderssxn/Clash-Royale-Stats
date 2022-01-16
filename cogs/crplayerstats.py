
from urllib.parse import _NetlocResultMixinBytes
import discord
import urllib.request
import json
import config

from discord.ui import Button, View
from discord.ext import commands



CRAuth= {
    "Authorization": "Bearer %s" %config.CRApiToken
}

api = "https://api.clashroyale.com/v1"

ep_player = "/players/%23"
ep_ucc = '/upcomingchests'

#92P9CL29L Anderssxn
    
class Stats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'"ctplayerstats" ready!')

        
    @commands.command()
    async def stats(self, ctx, playerTag):

        if playerTag.startswith("#"):
             playerTag = playerTag[1:]
        else:
            pass

        request = urllib.request.Request(api+ep_player+playerTag, None, CRAuth)
        response = urllib.request.urlopen(request).read().decode("utf-8")
        data = json.loads(response)

        uccrequest = urllib.request.Request(api+ep_player+playerTag+ep_ucc, None, CRAuth)
        uccresponse = urllib.request.urlopen(uccrequest).read().decode("utf-8")
        uccdata = json.loads(uccresponse)

        ucc = uccdata["items"]
        nextChest = ucc[0].get("name")
        nextChest2 = ucc[2].get("name")
        nextChest3 = ucc[2].get("name")

        nextChests = f"**{nextChest}**, *{nextChest2}, {nextChest3}*"

        clanCheck = "clan" in data
        if clanCheck == True:
            clanname = data["clan"].get("name")
            clantag = data["clan"].get("tag")
        else:
            clanname = "Not in a clan"
            clantag = ""
        
        username = data["name"]
        userLevel = data["expLevel"]
        arena = data["arena"].get("name")
        wins = data["wins"]
        losses = data["losses"]
        totalMatches = wins + losses
        favouriteCard = data["currentFavouriteCard"].get("name")
        bestTrophies = data["bestTrophies"]
        trophies = data["trophies"]
        
        currentDeck = data["currentDeck"]


        CD1 = {
            "name": currentDeck[0].get("name"),
            "id": currentDeck[0].get("id"),
            "level": currentDeck[0].get("level"),
            "image": currentDeck[0].get("iconUrls").get("medium"),
        }

        CD2 = {
            "name": currentDeck[1].get("name"),
            "id": currentDeck[1].get("id"),
            "level": currentDeck[1].get("level"),
            "image": currentDeck[1].get("iconUrls").get("medium"),
        }

        CD3 = {
            "name": currentDeck[2].get("name"),
            "id": currentDeck[2].get("id"),
            "level": currentDeck[2].get("level"),
            "image": currentDeck[2].get("iconUrls").get("medium"),
        }

        CD4 = {
            "name": currentDeck[3].get("name"),
            "id": currentDeck[3].get("id"),
            "level": currentDeck[3].get("level"),
            "image": currentDeck[3].get("iconUrls").get("medium"),
        }
        CD5 = {
            "name": currentDeck[4].get("name"),
            "id": currentDeck[4].get("id"),
            "level": currentDeck[4].get("level"),
            "image": currentDeck[4].get("iconUrls").get("medium"),
        }
        CD6 = {
            "name": currentDeck[5].get("name"),
            "id": currentDeck[5].get("id"),
            "level": currentDeck[5].get("level"),
            "image": currentDeck[5].get("iconUrls").get("medium"),
        }
        CD7 = {
            "name": currentDeck[6].get("name"),
            "id": currentDeck[6].get("id"),
            "level": currentDeck[6].get("level"),
            "image": currentDeck[6].get("iconUrls").get("medium"),
        }
        CD8 = {
            "name": currentDeck[7].get("name"),
            "id": currentDeck[7].get("id"),
            "level": currentDeck[7].get("level"),
            "image": currentDeck[7].get("iconUrls").get("medium"),
        }

        decklink = f"https://link.clashroyale.com/deck/en?deck={CD1['id']};{CD2['id']};{CD3['id']};{CD4['id']};{CD5['id']};{CD6['id']};{CD7['id']};{CD8['id']}"
    



        embed = discord.Embed(
            title = "Clash Royale Stats",
            description = '*"This app is under development!"*',
            color= 0x006eff,
        )

        embed.add_field(name=f" {userLevel} ⭐ |   {username} *#{playerTag}* ", value=f"**CLAN**: {clanname} {clantag}", inline=False)
        embed.add_field(name=f"{arena}", value=f"{trophies}  🏆", inline=True)
        embed.add_field(name="BEST TROPHIES", value=f"*{bestTrophies}*  🏆", inline=True)
        embed.add_field(name=" WINS ✅", value=f"{wins}", inline=True)
        embed.add_field(name="LOSSES ❌", value=f"{losses}", inline=True)
        embed.add_field(name="MATCHES PLAYED", value=f"{totalMatches}", inline=True)
        embed.add_field(name="Next Chests", value=f"{nextChests}", inline=False)
        embed.set_footer(text="Made by Anderssxn 2022")
        await ctx.send(embed=embed)

        embed = discord.Embed(
            title = "Clash Royale Stats",
            description= f"{username} #{playerTag} | Current Deck",
            color= 0xffbb00,
        )

        embed.add_field(name=f"{CD1['name']}", value=f"*Level {CD1['level']}*", inline=True)
        embed.add_field(name=f"{CD2['name']}", value=f"*Level {CD2['level']}*", inline=True)
        embed.add_field(name=f"{CD3['name']}", value=f"*Level {CD3['level']}*", inline=True)
        embed.add_field(name=f"{CD4['name']}", value=f"*Level {CD4['level']}*", inline=True)
        embed.add_field(name=f"{CD5['name']}", value=f"*Level {CD5['level']}*", inline=True)
        embed.add_field(name=f"{CD6['name']}", value=f"*Level {CD6['level']}*", inline=True)
        embed.add_field(name=f"{CD7['name']}", value=f"*Level {CD7['level']}*", inline=True)
        embed.add_field(name=f"{CD8['name']}", value=f"*Level {CD8['level']}*", inline=True)

        embed.add_field(name="Favourite Card", value=f"{favouriteCard}", inline=False)
        embed.set_footer(text=f"Made by Anderssxn 2022 | {config.version}")
        
        btn = discord.ui.Button(label="Copy Deck", url= f"{decklink}")
        view = View()
        view.add_item(btn)
        await ctx.send(embed=embed ,view = view)

        
        
    
def setup(client):

    client.add_cog(Stats(client))

