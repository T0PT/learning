import discord as ds
import apiai, json
token='ODk0OTc4NzQ3MzkwODk0MTYw.YVx36Q.y2XvtaCeEY9xwI8W80bn32R6Eig'
client=ds.Client()
@client.event
async def on_ready():
    print('hello gays, my name is: '+str(client.user.name)+', my id is: '+str(client.user.id))
@client.event
async  def on_message(message):
    request = apiai.ApiAI('ВАШ API ТОКЕН').text_request()  # Токен API к Dialogflow
    request.lang = 'ru'  # На каком языке будет послан запрос
    request.session_id = 'BatlabAIBot'  # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = message.content  # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    await message.channel.send(response)
client.run(token)