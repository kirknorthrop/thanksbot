import re

from slackbot.bot import listen_to, respond_to


@respond_to('thanks,? ([^<>:\'\";]*)', re.I)
@listen_to('thanks,? ([^<>:\'\";]*)', re.I)
def give_thanks(message, something):
    # This algorithm comes from https://github.com/jzplusplus/ThanksAnts
    # Thanks Jay Zuerndorfer.
    # Thuerndorfer.

    vowels = 'aeiouy'

    if something:
        for i, letter in enumerate(something):
            if letter in vowels:
                break

        if i > 0 and i < len(something):
            message.send('Th{}'.format(something[i:]))
