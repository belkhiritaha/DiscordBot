import asyncio
from asyncio import queues
from discord.ext import tasks, commands
import discord
import time
import random
import datetime
import cassiopeia as cass
from cassiopeia import Summoner

missions = [["voler le cannon ou smite sa grand mere (si jungler)", "faire ze3ma t'as perdu internet pendant 1min", "accuser quelqu'un qui tryhard pour le tilt", "mettre oui au prochain vote ff", "flash devant un allié pour la dahka", "ne pas farm la prochaine wave"],["faire un kill le plus vite possible", "faire top degat fin de la game", "aider sa team pour le prochain objectif", "mettre non au prochain vote ff", "faire top cs", "time les summs des adversaires"]]
players = []
players_full = []
imposters = [random.randint(0,4),random.randint(0,4)]
game_running = [False]
time_list = []
ok = [1]
buffer = []


cass.set_riot_api_key("RGAPI-2d972ef5-33b0-43bc-84d7-95a23fea9c02")

summoner = Summoner(name="Sorry lm BIind", region="EUW")
print("match id: ", summoner.match_history[0].timeline.frames[5].events[2])
#print([event for event in summoner.match_history[0].timeline.frames[1].events[0].type])

def resetGame():
    imposters[0] = random.randint(0,4)
    imposters[1] = random.randint(0,4)

    players.clear()


def addPlayer(player):
    if len(players) < 5:
        if player not in players:
            players.append(player.name)
            players_full.append(player)
            return 1
        else:
            return 2
    else:
        return 0


def getRole(player):
    if len(players) < 5:
        return 69
    else:
        if players.index(player) in imposters:
            return 1
        return 0

def execResult(message):
    a = [0]
    exec("a[0] = " + message.content[6:])
    return a[0]

def doResult(message):
    k = 0
    while message.content[7:][k] != ' ':
        k = k + 1
    
    range_loop = int(message.content[7:][:k])
    for i in range(range_loop):
        exec(message.content[7:][k+1:])
        
    return message.content[7:][k+1:]


client = discord.Client()


async def send(message):
    await client.send_message(client.get_channel("937763766286815265"), message)


@client.event
async def on_ready():
    print("bot ready")


@client.event
async def on_message(message):
    
    if message.content[:6] == "do for":
        result = doResult(message)
        await message.channel.send(result)

    if message.content[:5] == "print":
        result = execResult(message)
        await message.channel.send(result)

    if message.content.lower() == "ping":
        await message.channel.send(message.content)

    if message.content.lower() == "sultan":
        await message.channel.send("le noob")

    if message.content.lower() == "blind":
        await message.channel.send("le big boss")

    if message.content.lower() == "reset":
        resetGame()

    if message.content.lower() == "status":
        status = "Lobby is empty"
        if players != []:
            status = "Players in the lobby: \n"
            for player in players:
                status = "  -" + status + player + "\n"
        await message.channel.send(status)

    if message.content.lower() == "addme":
        print(message.author)
        if addPlayer(message.author) == 1:
            await message.channel.send(message.author.name + " joined the game.")
            await message.author.send("You have joined the game. Type rolepls to get your role")
        else:
            if addPlayer(message.author.name) == 2:
                await message.channel.send("You are already in the lobby")    
            else:
                await message.channel.send("Lobby is already full")

    if message.content.lower() == "rolepls":
        role = getRole(message.author.name)
        if role == 69:
            await message.channel.send("Can't give out roles now. Lobby isn't full yet")
        if role == 1:
            await message.author.send("You are an imposter! go ruin (discretement) la game")
        if role == 0:
            await message.author.send("You are a crewmate! go tryhard")
    
    if message.content.lower() == "gamestart":
        game_running[0] = True
        if time_list == []:
            time_list.append(time.time())
        while game_running[0]:
            if ok[0] == 1:
                await sendMission(players_full, missions)

    if message.content.lower() == "gamewon":
        game_running[0] = False
        


async def sendMission(players_full, missions):
    if time.time() - time_list[0] > 10:
        ok[0] = 0
        player = players_full[random.randint(0,4)]
        if player in imposters:
            role = 1
        else:
            role = 0
        
        mission = missions[role][random.randint(0, len(missions[role]) - 1)]
        await player.send("You have recieved a mission ! You must complete it as soon as you can \n" + "here's your mission: " + mission)
        channel = client.get_channel(937946461642047509)
        await channel.send("A mission has been given to a random player 👀 watch out")
        await asyncio.sleep(15)
        ok[0] = 1

client.run("OTM3NzYwNjQwODc2MDE5NzUz.Yfgbpw.1BzDwnSAgz1hNSD-fWbCzTSRGFk")

