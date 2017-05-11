import re

from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to
from mattermost_bot.bot import Bot

@listen_to('Hey Blue')
def hey_blue(message):
    print '001'
    message.reply('Blue is on')

@respond_to('Give me (.*)')
def give_me(message, something):
        message.reply('Here is %s' % something)

@respond_to('Give me (.*)')
def give_me(message, something):
        message.reply('Here is %s' % something)

@listen_to('*')
def notify(message):
    print '111'


if __name__ == "__main__":
    Bot().run()
