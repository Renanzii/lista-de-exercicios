import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)


@client.event
async def on_ready():
    print(f"{client.user} está online!")

@client.event
async def on_message(message):
    if message.author != client.user:
      await message.channel.send ("hello word!")
      
    if message.content  == "teste":
      await message.channel.send ("testando")



    
    

client.run("MTE0MDc3OTg5MTIyMzE3MTE4Mg.GFAhnk.8RzvqkmNPkr4uRVqats2AnkcEkbzxQTvIBLUXI")