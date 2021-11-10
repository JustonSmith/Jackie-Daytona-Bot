import discord
import requests
import json
import random

from apikeys import *

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "bummed", "irritated", "mad", "pissed", "distressed", "troubled", "heartbroken", "hopeless", "melancholy", "gloomy", "glum", "woeful", "disappointed", "bleak",   ]

starter_encouragements = ["If it aint broke, dont fix it.", "Nothing ventured, nothing gained", "Haste makes waste.", "One swallow doesnt make a summer.", "Practice makes perfect", "A rolling stone gathers no moss.", "Jack of all trades, master of none.", "Descretion is the better part of valor.", "A watched pot never boils.", "Dont look a gift horse in the mouth.", "People who live in glass houses shouldnt throw stones.", "Necessity is the mother of invention.", "A stitch in time saves nine", "Dont cross that bridge until you come to it.", "Every dog has its day.", "The squeaky wheel gets the grease.", "Dont bite the hand that feeds you.", "Too many cooks spoil the broth.", "Dont put all your eggs in one basket", "You can lead a horse to water but you cant make it drink", "A bird in hand is better than two in the bush.", "A chain is only as strong as its weakest link", "Two is company, three is a crowd.", "Fools rush in where angels fear to tread."]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = 'I say, you seem a little down in the chops. You know, ' + json_data[0]['a'] + ' once said, ' + json_data[0] ['q']+'.' + ' Heres one on Jackie. Cheers! To being back in high snuff!' 
    return(quote)

@client.event
async def on_ready():
    print('*****')
    print ('We have logged in as {0.user}'.format(client))
    print('*****')

@client.event
async def on_message(message):

    msg = message.content

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Good day! Im Jackie Daytona! Regular human bartender!' )

    if message.content.startswith('$wheresjackie'):
        await message.channel.send('Here I am old chap! Jackie Daytona! Regular human bartender! Hows about a round for the whole lot?! On Jackie!')

    if message.content.startswith('$pour'):
        await message.channel.send('One regular human alcohol! Coming right up!')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))


client.run(TOKEN)

