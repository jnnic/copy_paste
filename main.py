from telegram.ext import Updater, CommandHandler
import requests
import random


API_KEY = "35bd7717-39ad-41cc-8cd1-8c2a4a43e631"

updater = Updater(token='5938233596:AAEy86-rgbOMHa9Swyh-ui0cewbP1wwkyh8', use_context=True)

dispatcher = updater.dispatcher

def start(update, context): # Sends a welcome message
    context.bot.send_message(chat_id=update.message.chat_id, text="Hi! I'm a basic Telegram bot. You can use me to do some simple tasks.")

def echo(update, context): # Echoes the message sent by the user
    text = update.message.text
    context.bot.send_message(chat_id=update.message.chat_id, text=text)

def BitcoinPrice(update, context): # Get the Bitcoin price
        # Construct the URL for the API request
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    # Set the HTTP parameters for the request
    params = {
        "symbol": "BTC",
        "convert": "USD"
    }

    # Set the HTTP headers for the request
    headers = {
        "X-CMC_PRO_API_KEY": API_KEY
    }

    # Send the request to the API and get the response
    response = requests.get(url, params=params, headers=headers)

    data = response.json()
    price = data["data"]["BTC"]["quote"]["USD"]["price"]
    price_str = (f"Bitcoin price: ${price:.2f}")

    context.bot.send_message(chat_id=update.message.chat_id, text=price_str)
    

def EtheriumPrice(update, context): # Get the Etherium price
    # Construct the URL for the API request
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

    # Set the HTTP parameters for the request
    params = {
        "symbol": "ETH",
        "convert": "USD"
    }

    # Set the HTTP headers for the request
    headers = {
        "X-CMC_PRO_API_KEY": API_KEY
    }

    # Send the request to the API and get the response
    response = requests.get(url, params=params, headers=headers)

    data = response.json()
    price = data["data"]["ETH"]["quote"]["USD"]["price"]
    price_str = (f"Etherium price: ${price:.2f}")

    context.bot.send_message(chat_id=update.message.chat_id, text=price_str)


def joke(update, context): # Generates a random joke
    response = requests.get('https://sv443.net/jokeapi/v2/joke/Programming')
    response1 = requests.get('https://sv443.net/jokeapi/v2/joke/Programming')
    response2 = requests.get('https://sv443.net/jokeapi/v2/joke/Programming')
    joke_data = response.json()
    joke_data1 = response1.json()
    joke_data2 = response2.json()
    try:
        the_joke = joke_data["joke"]
        context.bot.send_message(chat_id=update.message.chat_id, text=the_joke)
    except:
        try:
            the_joke1 = joke_data1["joke"]
            context.bot.send_message(chat_id=update.message.chat_id, text=the_joke1)

        except:
            try:
                the_joke2 = joke_data2["joke"]
                context.bot.send_message(chat_id=update.message.chat_id, text=the_joke2)

            except:
                text1="No joke for you! (This is an Error message)"
                context.bot.send_message(chat_id=update.message.chat_id, text=text1)

def passwort(update, context): # Generates a random password using the list of characters
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    password = ''.join(random.choices(chars, k=10))
    context.bot.send_message(chat_id=update.message.chat_id, text=password)





start_handler = CommandHandler('start', start)
echo_handler = CommandHandler('echo', echo)
bitcoin_handler = CommandHandler('bitcoin', BitcoinPrice)
joke_handler = CommandHandler('joke', joke)
password_handler = CommandHandler('passwort', passwort)
etherium_handler = CommandHandler('etherium', EtheriumPrice)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(bitcoin_handler)
dispatcher.add_handler(joke_handler)
dispatcher.add_handler(password_handler)
dispatcher.add_handler(etherium_handler)

updater.start_polling()