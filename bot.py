import discord
from discord.ext import commands, tasks
import requests

# Configurações do bot
TOKEN = 'YOUR_INSTAGRAM_ID'
INSTAGRAM_USER_ID = YOUR_INSTAGRAM_USER_ID
DISCORD_CHANNEL_ID = YOUR_DISCORD_CHANNEL_ID
ERROR_CHANNEL_ID = YOUR_CHANNEL_ID 
CHECK_INTERVAL_SECONDS = 3600  # Intervalo de verificação em segundos (1 hora)

# Criação do bot com intents
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True
bot = commands.Bot(command_prefix='+', intents=intents)


@bot.event
async def on_ready():
    print('Bot do Discord online!')
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    if channel:
        await channel.send('Bot online! Agora vou verificar as postagens do Instagram.')
    else:
        print(f'Não foi possível encontrar o canal com ID {DISCORD_CHANNEL_ID}')


@bot.event
async def on_error(event, *args, **kwargs):
    error = args[0]
    print('Ocorreu um erro no bot do Discord:', error)
    error_channel = bot.get_channel(ERROR_CHANNEL_ID)
    if error_channel:
        await error_channel.send(f'Ocorreu um erro no bot do Discord: `{error}`')
    else:
        print(f'Não foi possível encontrar o canal de erro com ID {ERROR_CHANNEL_ID}')


async def check_instagram_post():
    try:
        response = requests.get(f'https://www.instagram.com/{INSTAGRAM_USER_ID}/?__a=1')
        response.raise_for_status()
        data = response.json()
        latest_post = data['graphql']['user']['edge_owner_to_timeline_media']['edges'][0]['node']

        # Verifica se já foi enviada uma mensagem sobre esse post
        if latest_post['id'] != check_instagram_post.latest_post_id:
            check_instagram_post.latest_post_id = latest_post['id']
            post_url = f"https://www.instagram.com/p/{latest_post['shortcode']}"
            message = f'Nova postagem no Instagram! Confira em: {post_url}! @Notificações Instagram'

            channel = bot.get_channel(DISCORD_CHANNEL_ID)
            if channel:
                await channel.send(message)
            else:
                print(f'Não foi possível encontrar o canal com ID {DISCORD_CHANNEL_ID}')
    except Exception as error:
        print('Erro ao verificar a postagem do Instagram:', error)
        error_channel = bot.get_channel(ERROR_CHANNEL_ID)
        if error_channel:
            await error_channel.send(f'Erro ao verificar a postagem do Instagram: `{error}`')
        else:
            print(f'Não foi possível encontrar o canal de erro com ID {ERROR_CHANNEL_ID}')


check_instagram_post.latest_post_id = ''


@tasks.loop(seconds=CHECK_INTERVAL_SECONDS)
async def periodic_check():
    await check_instagram_post()


@bot.event
async def on_ready():
    print(f'Bot do Discord online!')
    periodic_check.start()


# Inicia o bot
bot.run(TOKEN)
