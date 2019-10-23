# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:03:00 2018

@author: pat bowden
"""
import discord
import asyncio
import random
import csv

'''
def storecsv(a,b):
    with open('quotes.csv','a') as infile:
        writer = csv.writer(infile, delimiter=' ')
        writer.writerow[(a,b)]
'''

def readthoughts():
    
	with open('thoughts.txt', 'r') as infile:
		test = [line.strip() for line in infile]
		print(len(test))
'''
		for i in infile.readlines():
			o = [i.strip()]

			print(o)
'''



def randtime ():
    return (random.randint(1,24) * 3600)



commands=['!test','!sleep','!jvoice','!quote','!thought']
vchannel = 'CHANNEL ID' #insert channel id where you want the bot to post 
client=discord.Client()
tokenbot='BOTS TOKEN' #bots API token
mytoken = 'YOUR API TOKEN' #your API TOKEN

async def my_background_task():
    await client.wait_until_ready()
    channel = discord.Object(id='CHANNEL ID') #insert Channel id
    with open('meirl.txt','r')as infile:
        test = [line.strip() for line in infile]
    message = random.choice(test)
    while not client.is_closed:
        await client.send_message(channel, message)
        print(message)
        await asyncio.sleep(10)

async def randomthought():
    await client.wait_until_ready()    
    channel = discord.Object(id='CHANNEL ID') #insert Channel id
    with open('thoughts.txt','r')as infile:
        test = [line.strip() for line in infile]
    while not client.is_closed:
        await client.send_message(channel, random.choice(test))
        t=randtime()
        print(t)
        await asyncio.sleep(t)

@client.event
async def on_message(message):
    
    if message.content.startswith(commands[0]):

        await client.send_message(message.channel, 'Hello {0}'.format(message.author.mention))
        #await client.send_message(message.channel, message.content.split(commands[0])[1])

    elif message.content.startswith(commands[1]):
        await client.send_message(message.channel, 'sleeping for {0} seconds'.format(message.content.split(commands[1])[1]))
        #time = int(message.content.split(command2)[1]))
        #await asyncio.sleep(int(message.content.split(command2)[1])))
        await asyncio.sleep(int(message.content.split(commands[1])[1]))
        await client.send_message(message.channel, 'im back {0}'.format(message.author.mention))

    elif message.content.startswith(commands[3]):
        await client.send_message(message.channel, ' oo thats a good one storing quote for later thanks {0}'.format(message.author.mention))
        value = message.content.split(commands[3])[0]
        quote = message.content.split(commands[3])[1]
        print(quote)
        storecsv(value,quote)
    elif message.content.startswith(commands[4]):
        temp=readthoughts()
        await client.send_message(message.channel, ' oo thats a good one storing quote for later thanks {0}'.format(readthoughts()))
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#client.loop.create_task(randomthought())       
client.run(tokenbot)