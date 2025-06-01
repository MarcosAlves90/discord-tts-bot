
# Bot de Voz para Discord

Um bot simples que entra em canais de voz e fala mensagens usando conversão de texto para fala.

## Funcionalidades

O bot oferece os seguintes comandos:

- `/entrar` - Faz o bot entrar no canal de voz em que você está
- `/sair` - Desconecta o bot do canal de voz atual
- `/falar [texto]` - Converte o texto fornecido em fala e reproduz no canal de voz

## Requisitos

- Python 3.11
- FFmpeg
- Token de Bot do Discord
- Bibliotecas: discord.py, python-dotenv, gtts

## Instalação

### Usando Docker (Recomendado)

1. Clone este repositório
2. Crie um arquivo `.env` na raiz do projeto com seu token:

   ```env
   DISCORD_TOKEN="seu_token_aqui"
   ```

3. Construa e execute a imagem Docker:

   ```powershell
   docker build -t discord-voice-bot .
   docker run -d discord-voice-bot
   ```

### Instalação manual

1. Clone este repositório
2. Instale as dependências:

   ```powershell
   pip install discord.py python-dotenv gtts pynacl
   ```

3. Instale o FFmpeg no seu sistema
4. Crie um arquivo `.env` na raiz do projeto com seu token
5. Execute o bot:

   ```powershell
   python bot.py
   ```

## Como usar

1. Adicione o bot ao seu servidor Discord
2. Entre em um canal de voz
3. Use o comando `/entrar` para trazer o bot para o canal
4. Use `/falar [sua mensagem]` para fazer o bot falar
5. Use `/sair` quando terminar

## Observações

- O bot reproduz as mensagens prefixadas com o nome de quem solicitou
- O arquivo `.env` com seu token não deve ser compartilhado ou commitado
