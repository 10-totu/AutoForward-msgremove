# Authour: TOTU/@to.tu (Discord)
# Purpose: forwards + removes messages excluding a specific member.


import discord
from discord.ext import commands

#--Enable perms (lowkey got this off of reddit)--
intent = discord.Intents.default()
intent.message_content = True

bot = commands.Bot(command_prefix="!", intents=intent)

#--Place your numeral channel IDs here!!!
ORIGINAL_CHANNEL = 1527340262005932153  # The channel of which messages will be deleted
FORWARDED_CHANNEL = 1527341010840195213  # The channel you want to forward to

@bot.event
async def when_ready():
    print(f"Running as {bot.user}!")

@bot.event
async def on_message(message):
    #--this prevents looping---
    if message.author == bot.user:
        return

    #--check if any new messages are sent in the original channel--
    if message.channel.id == ORIGINAL_CHANNEL:
        
        #--check if the sender is the specified exclusionary user.--
        sender_tag = str(message.author)
        if sender_tag == "YAGPDB.xyz#8760": #--Change to whatever bot you want. make sure they have the old style of usernames or else remove the line above.--
            return  #--doesnt forward because its the specified bot lol--
        
        #--let the bot retreive the channel which the message will be forwarded to--
        forwarded_channel = bot.get_channel(FORWARDED_CHANNEL)
        if forwarded_channel:
            # Check if there is text to send
            if message.content:
                await forwarded_channel.send(f"**{message.author}:** {message.content}")
            
            #--forward images & videos alongside the message--
            for attachment in message.attachments:
                await forwarded_channel.send(attachment.url)
                #--Deletes the original message
                await message.delete()
                
    await bot.process_commands(message)

#--bot token
bot.run("im_not_gonna_share_that_cuz_dangerous")