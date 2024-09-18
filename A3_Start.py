import os
import csv
import discord
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()
TOKEN = 'token'
GUILD = 'burtons server'

# we need complexes intents this, we need to be able to access events.
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

# the name of my csv file 
CSV_FILE = 'members.csv'

def initCsv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Member ID', 'Member Name', 'Join Date'])

def add_member_to_csv(member):
    with open(CSV_FILE, mode='a', newline='') as file:  # Adding a new member to the CSV 
        writer = csv.writer(file)
        writer.writerow([member.id, member.name, datetime.now().isoformat()])

def remove_member_from_csv(member):          # Removing a member from the CSV with their ID'S
    rows = []
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row[0] != str(member.id)]

    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

@client.event
async def on_ready():           # Initializing the CSV file and add existing members when the bot is ready
    initCsv()
    guild = discord.utils.get(client.guilds, name=GUILD)
    if guild:
        for member in guild.members:
            on_ready(member)
        print(f"{client.user} is online on {guild.name}!")
        
        general = discord.utils.get(guild.channels, name="general")
        if general:
            await general.send(f"{client.user} is online on {guild.name}!")
    else:
        print(f"Guild '{GUILD}' not found")

@client.event
async def on_member_join(member):  # that is where new members are getting welcome messages and additing in to the CSV
    on_member_join(member)
    guild = discord.utils.get(client.guilds, name=GUILD)  
    if guild:
        general = discord.utils.get(guild.channels, name="general")  # Send a channel message in general channel
        if general:
            await general.send(f"Hello {member.name}, welcome to {guild.name}!,here is hell!!!! https://tenor.com/view/burn-in-hell-elmo-fire-flame-gif-8764555")
        
        await member.create_dm()
        await member.dm_channel.send(
            f"Hello {member.name}, welcome to {guild.name}!, this is turtle sliding in your dms :sunglasses: rizzturtle"
        )
    else:
        print(f"Guild '{GUILD}' not found")

@client.event
async def on_member_remove(member):  # the function will be realize when member leaves
    on_member_remove(member)
    guild = discord.utils.get(client.guilds, name=GUILD)
    if guild:
        general = discord.utils.get(guild.channels, name="general")
        if general:                                            # good bye message 
            await general.send(f"Goodbye {member.name}, we will not miss you, since you left us!!, https://tenor.com/view/gold-star-succession-gif-27712928")
    else:
        print(f"Guild '{GUILD}' not found")

# Run the bot
client.run(TOKEN)
