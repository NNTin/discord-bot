
<p align="center">
  <img src="https://i.imgur.com/vKqLL6V.png" width="1024">
</p>

<h1 align="center">
Judge0Bot
</h1>
<h4 align="center">Code execution in the chat</h4>



<div align="center">
<a href="https://github.com/Rapptz/discord.py/">
      <img src="https://img.shields.io/badge/discord-py-blue.svg" alt="discord.py">
</a>
<a>
    <img src="https://img.shields.io/github/v/tag/judge0/discord-bot" alt="Version">
</a>
<a href="https://github.com/ambv/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style: Black">
</a>
<a href="https://discord.gg/6dvxeA8">
      <img src="https://discordapp.com/api/guilds/620615182116323328/embed.png" alt="Judge0 server">
</a>
</div>

<p align="center">
  <a href="#overview">Overview</a>
  •
  <a href="#get-to-the-bot">Get to the bot</a>
  •
  <a href="#usage">Usage</a>
  •
  <a href="#development">Development</a>
</p>

# Overview
**Judge0Bot** is a Discord bot for interacting with the [Judge0 API](https://api.judge0.com/).
It executes source code of near 20 programming languages directly in the Discord channel chat.

# Get to the bot
The bot is hosted and this means that you can use its commands from a Discord server.
Three of the ways of interacting with our bot in the Discord platform:

1. **Invite the bot in your server**.
    You can invite the bot in servers which you manage with this [invite link.](https://discordapp.com/oauth2/authorize?client_id=620609604295852033&scope=bot&permissions=388160)
1. **Use the bot from our support server**.
    You can use the bot from our Judge0 support server. Join the server [here.]()
1. **Use the bot from programming servers.**
    The bot is included in large IT related communties.
    [discord.py](https://discord.gg/r3sSKJJ), [ITBG](http://discord.gg/dRrdYQf)
    
# Usage
The bot is quite easy and straightforward for use. There is integrated
help command in the bot. Send `;help` in the chat and the bot will send helpful
information for usage.

#### Executing code
The code execution is done through sending a language command and passing the source code.
You can view all language commands after sending `;languages` in the chat.
Every language command have three use cases (Python example):

<br>

`;python print("Executing source code")`
<p align="left">
  <img src="https://i.imgur.com/Enafvtn.png" width="256">
</p>

This command will execute the passed source code and it will return an output embed which includes information like time and memory usage and output which includes standart output, standart error, compiler message and sandbox message if any.

<br>

`;python`
<p align="left">
  <img src="https://i.imgur.com/4zW9yd1.png" width="256">
</p>


If a language command is send without source code it will return an useful guide how to pass the source code. There are three methods: passing source code in plain format, passing soure code in code block or passing source code in highlighted code block.

<br>

`;python -v`
<p align="left">
  <img src="https://i.imgur.com/881hbFc.png" width="256">
</p>


If argument `-v` is passed instead of source code it will return the version of the language.

# Development
It is highly preferable if you don't run an instance of this bot unless you want to contribute.

The installation and running steps are as follows:

1. **Make sure to get git and Python 3.6 or higher**

This is required to clone the repository and actually run the bot.

2. **Clone the repository**

`git clone https://github.com/judge0/discord-bot.git`

3. **Enter the directory**

`cd discord-bot`

4. **Install Pipenv**

`python -m pip install pipenv`

5. **Install dependencies**

`pipenv install --dev`

6. **Run the bot**

Bot token passed like command-line argument:

`pipenv run start <token>`

Bot token set as enviorment variable **BOT_TOKEN**:

`pipenv run start`

# Deployment
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
