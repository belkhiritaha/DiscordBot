# DiscordBot
fun discord bot with live debugging commands

## LoL/AmongUs crossover
discord adaptation to one of my repos, figured that discord was a way better tool to deliver roles to players, vote etc..
Commands include:
- reset: Resets all variables, roles, and clears arrays
- status: Prints the status of lobby (number of players currently in the lobby)
- addme: Adds a player to the lobby
- rolepls: Sends a DM to the player that includes his role
- gamestart: Starts timer for missions
- gamewon: Announces that game is done and starts voting phase
- .... more functions are coming as this part is functionnal, but not completely done yet

## Debugging tools
When writing code for the 1st part, I found debugging the code a bit frustrating as you need to restart the bot each time you make a change to the code, so I implemented a way to execute commands and see their output through Discord's chat
Commands include:
- print _python variable_: prints (to discord chat) the current value of any variable within the environnement: 

Exemple: - print players >>> ["Sorry lm BIind","NotToxicBipolar","iSultan","Sondo45","Lost Astronaut"]
- do for _int_ _python command_: basically a for loop where the loops variable is "i"

Exemple: - do for 1 count = 0; do for 10 count+=1; print count >>>> 10

_Also note that anything that is printed, or processed by the "do for" loop is automatically added to a list called "buffer", hence comes the following commands_

- buffer: prints the buffer as it is
- clear buffer: clears the buffer (duh)
