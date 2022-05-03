WQS--from discord.ext import commands
from boto.s3.connection import S3Connection
import requests
import json

TOKEN = S3Connection(os.environ['TOKEN'], os.environ['weather-craig'])
WEATHER_API =  S3Connection(os.environ['API_KEY'], os.environ['weather-craig'])


# Initialize Bot and Denote The Command Prefix
bot = commands.Bot(command_prefix="$")

# Runs when Bot Succesfully Connects
@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong!")

@bot.command()
async def weather(ctx, place = "London"):
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API} &q={place}&aqi=no".json()

        location = response['location']['name'] + ", "+ response['location']['region']
        temp = response['current']['temp_f']
        percip = response['current']['condition']['text']
        temp = str(temp)	
        weather = "The weather in " + location + " is " + temp + " deg F and " + percip

        await ctx.send(weather)

@bot.command()
async def forecast(ctx, place = "London"):
    response = requests.get("http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API}&q={place}&days=3&aqi=no&alerts=no".json()

    location = "Forecast for " + response['location']['name'] + ", "+ response['location']['region']
    threeDays = ""
    for x in range(3):
        day = response['forecast']['forecastday'][x]['date']
        mintemp = response['forecast']['forecastday'][x]['day']['mintemp_f']
        mintemp = str(mintemp)
        maxtemp = response['forecast']['forecastday'][x]['day']['maxtemp_f']
        maxtemp = str(maxtemp)
        threeDays += (f'\n Date: {day:15}| min temp: {mintemp:10} max temp: ' + maxtemp)
    
    finalString  = location + "\n" + threeDays 
    await ctx.send(finalString)
bot.run(TOKEN)
