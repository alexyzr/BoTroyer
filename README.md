# BoTroyer
Bot do Discord que utiliza um canal de texto para postar novos postagens de um perfil do Instagram.

## índice

- [Configuração do bot](#configuração)
- [Comandos](#comandos)
- [Autor](#autor)

## Configuração

Utilizando algum programa que te possibilite editar o código, e procure o arquivo `bot.py`. Em seguida, modifique as seguintes variáveis:
```
# Configurações do bot
TOKEN = 'YOUR_INSTAGRAM_ID'
INSTAGRAM_USER_ID = YOUR_INSTAGRAM_USER_ID
DISCORD_CHANNEL_ID = YOUR_DISCORD_CHANNEL_ID
ERROR_CHANNEL_ID = YOUR_CHANNEL_ID 
CHECK_INTERVAL_SECONDS = 3600  # Intervalo de verificação em segundos (1 hora)
```
No `TOKEN`, procure o token no site oficial do [Discord Developer](https://discord.com/developers/applications) após fazer sua Aplicação para a criação de um novo bot.

Para as `DISCORD_CHANNEL_ID` e `ERROR_CHANNEL_ID`, você encontra clicando com o botão direito nos canais desejados, e procurar a opção `Copiar ID do canal`. 

E para o `INSTAGRAM_USER_ID`, será necessário o uso de um site, como por exemplo o site do [CodeOfaNinja](https://www.codeofaninja.com/tools/find-instagram-user-id/).

O `CHECK_INTERVAL_SECONDS`também pode ser modificado para a sua necessidade.


## Comandos

No momento, o bot não tem nenhum comando configurado. Quando ele fica online, ele automaticamente vai verificar o Instagram configurado no `bot.py` e postar no canal de voz o link do post, junto com a mensagem que pode ser configurada.


## Autor

- GitHub - [@alexyzr](https://github.com/alexyzr)
