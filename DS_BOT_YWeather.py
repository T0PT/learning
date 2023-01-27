#!/usr/bin/env python3

import discord as ds
import requests
import yandex_weather_api
import time
channel=894979605180592214
x=time.localtime()
token = '3bc03c70-81cb-4f1f-9d0d-ea9a7fa2199f'
token_ds='ODk0OTc4NzQ3MzkwODk0MTYw.YVx36Q.y2XvtaCeEY9xwI8W80bn32R6Eig'
client=ds.Client()
forecast_yandex= yandex_weather_api.get(session=requests, api_key=token, lat=55.10, lon=60.10)
print(forecast_yandex)
print(forecast_yandex['forecast'][0])
print(forecast_yandex['forecast'][0]['parts']['evening'])
print(forecast_yandex['forecast'][0]['parts']['night'])
@client.event
async def on_ready():
    print('hello gays')
    #print(client.get_channel(0))
#forecast_yandex= yandex_weather_api.get(session=requests, api_key=token, lat=55.10, lon=60.10)
@client.event
async def on_message(message):
    #if message.content.startswith('!set this channel'):
     #   channel=message.channel.id
     #   await client.get_channel(id=channel).send('this channel is main now')
     #   print(channel)
    forecast_yandex= yandex_weather_api.get(session=requests, api_key=token, lat=55.10, lon=60.10)
    if message.content.startswith('!погода  '):
        await client.get_channel(id=channel).send('Сейчас за бортом: '+str(forecast_yandex['fact']['temp']))
    if message.content.startswith('!погода днём'):
        await client.get_channel(id=channel).send(
            'Сегодня днём: ' +
            str(forecast_yandex['forecast'][0]['parts']['evening']['temp_avg']))
        await client.get_channel(id=channel).send(
            'Погода: ' +
            str(forecast_yandex['forecast'][0]['parts']['evening']['condition']))
        await client.get_channel(id=channel).send(
            'Давление: ' +
            str(forecast_yandex['forecast'][0]['parts']['evening']['pressure_mm']))
    if message.content.startswith('!погода вечером'):
        await client.get_channel(id=channel).send(
            'Сегодня вечером: ' +
            str(forecast_yandex['forecast'][0]['parts']['night']['temp_avg']))
        await client.get_channel(id=channel).send(
            'Погода: ' +
            str(forecast_yandex['forecast'][0]['parts']['night']['condition']))
        await client.get_channel(id=channel).send(
            'Давление: ' +
            str(forecast_yandex['forecast'][0]['parts']['night']['pressure_mm']))
client.run(token_ds)
