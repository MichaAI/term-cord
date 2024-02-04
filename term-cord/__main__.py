import curses
import atexit
import signal
import getpass
import os
import discord
from discord.ext import commands


line = 0
if os.environ.get('TERM_CORD_TOKEN') is None:
    print("Note: You can set the token in the "
          "TERM_CORD_TOKEN environment variable.")
    token = input("Please enter bot token:")
else:
    token = os.environ.get('TERM_CORD_TOKEN')
bot = commands.Bot(
    command_prefix="*"':;!?@#$_&-+()/',
    # bad prefix because it shouldn't exist at all
    intents=discord.Intents.all(),
)
screen = curses.initscr()


@bot.event
async def on_message(message):
    global line
    y, x = screen.getmaxyx()
    curses.resizeterm(y, x)
    screen.addstr(line % y, 0, f"{message.author}:  {message.content}")
    screen.refresh()
    line += 1


def main():
    bot.run(token)
    handle_exit()


def handle_exit(*args):
    curses.endwin()


if __name__ == "__main__":
    main()

atexit.register(handle_exit)
signal.signal(signal.SIGTERM, handle_exit)
signal.signal(signal.SIGINT, handle_exit)
