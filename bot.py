import discord
from discord import app_commands
import os
from dotenv import load_dotenv
from gtts import gTTS
import tempfile
import asyncio

import keepalive
keepalive.start_keepalive()

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

@client.tree.command(name="entrar", description="Me chama para o seu canal de voz que eu entro para conversar!")
async def entrar(interaction: discord.Interaction):
    if interaction.user.voice and interaction.user.voice.channel:
        channel = interaction.user.voice.channel
        await channel.connect()
        await interaction.response.send_message(f"Prontinho! Acabei de entrar no canal de voz: {channel.name}. Pode falar comigo à vontade!")
    else:
        await interaction.response.send_message("Ei! Você precisa estar em um canal de voz para eu poder entrar e conversar com você!", ephemeral=True)
@client.tree.command(name="sair", description="Se quiser que eu saia do canal de voz, é só pedir!")
async def sair(interaction: discord.Interaction):
    voice_client = discord.utils.get(client.voice_clients, guild=interaction.guild)
    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
        await interaction.response.send_message("Ok, estou saindo do canal de voz! Se precisar de mim de novo, é só chamar!")
    else:
        await interaction.response.send_message("Eu nem entrei em nenhum canal de voz ainda! Me chama primeiro para conversar.", ephemeral=True)
@client.tree.command(name="falar", description="Me peça para falar algo no canal de voz e eu falo para todo mundo ouvir!")
@app_commands.describe(texto="O que você quer que eu diga em voz alta para todos?")
async def falar(interaction: discord.Interaction, texto: str):
    voice_client = discord.utils.get(client.voice_clients, guild=interaction.guild)
    if not (voice_client and voice_client.is_connected()):
        await interaction.response.send_message("Eu preciso estar em um canal de voz para falar! Me chama primeiro usando o comando /entrar.", ephemeral=True)
        return
    usuario = interaction.user.display_name
    frase = f"{usuario} pediu para eu dizer: {texto}"
    await interaction.response.send_message(f"Pode deixar, vou falar: {texto}", ephemeral=True)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts = gTTS(text=frase, lang='pt')
        tts.save(fp.name)
        audio_path = fp.name
    audio_source = discord.FFmpegPCMAudio(audio_path)
    if not voice_client.is_playing():
        voice_client.play(audio_source)
        while voice_client.is_playing():
            await asyncio.sleep(0.5)
    try:
        os.remove(audio_path)
    except Exception:
        pass

client.run(TOKEN)