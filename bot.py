import discord
from discord import app_commands
import os
from dotenv import load_dotenv

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await self.tree.sync()

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = MyClient(intents=intents)

@client.tree.command(name="entrar", description="Faz o bot entrar na call")
async def entrar(interaction: discord.Interaction):
    if interaction.user.voice and interaction.user.voice.channel:
        channel = interaction.user.voice.channel
        await channel.connect()
        await interaction.response.send_message(f"Entrei no canal de voz: {channel.name}")
    else:
        await interaction.response.send_message("Você precisa estar em um canal de voz para eu entrar!", ephemeral=True)
@client.tree.command(name="sair", description="Faz o bot sair da call")
async def sair(interaction: discord.Interaction):
    voice_client = discord.utils.get(client.voice_clients, guild=interaction.guild)
    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
        await interaction.response.send_message("Saí do canal de voz!")
    else:
        await interaction.response.send_message("Não estou em nenhum canal de voz neste servidor.", ephemeral=True)

client.run(TOKEN)