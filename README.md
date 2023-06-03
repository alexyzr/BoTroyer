# BoTroyer
Bot do Discord que utiliza um canal de texto para postar novos postagens de um perfil do Instagram.

## índice

- [Configuração do bot](#configuração)
- [Pré-requesitos](#requerimentos)
- [Comandos](#comandos)
- [Contribuição](#contribuição)
- [Aviso Legal](#aviso-legal)
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

O `CHECK_INTERVAL_SECONDS`também pode ser modificado para a sua necessidade, mudando o tempo entre os intervalos em segundos.

Após a configuração, você pode executar o bot executando o seguinte comando no terminal:

```
python main.py
```

O bot ficará online e começará a verificar as postagens do Instagram de acordo com o intervalo especificado. Ele enviará notificações no canal do Discord especificado sempre que uma nova postagem for feita.


## Requerimentos

Para o código rodar corretamente, é necessário que as seguintes dependências estejam baixadas:

• discord.py: É uma biblioteca de integração do Discord para Python.

• requests: É uma biblioteca para fazer requisições HTTP em Python.

• Python 3.7 ou superior

Você pode instalar essas dependências utilizando o pip, executando os seguintes comandos no terminal:

```
pip install -r requirements.txt
```


## Comandos

No momento, o bot não tem nenhum comando configurado. Quando ele fica online, ele automaticamente vai verificar o Instagram configurado no `bot.py` e postar no canal de voz o link do post, junto com a mensagem que pode ser configurada.


## Contribuição
Contribuições são bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou novos recursos, fique à vontade para abrir uma issue ou enviar um pull request.


## Aviso Legal
Este projeto é fornecido como está, sem qualquer garantia. Use por sua própria conta e risco. O desenvolvedor não se responsabiliza por quaisquer danos causados pelo uso deste código.


## Autor

- GitHub - [@alexyzr](https://github.com/alexyzr)
