import re

from slackbot.bot import listen_to, respond_to

import settings

@respond_to('.*thanks,? ([^<>:\'\";]*)', re.I)
@listen_to('.*thanks,? ([^<>:\'\";]*)', re.I)
def give_thanks(message, something):
    # This algorithm comes from https://github.com/jzplusplus/ThanksAnts
    # Thanks Jay Zuerndorfer.
    # Thuerndorfer.

    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'qu']

    if something:
        for i, letter in enumerate(something):
            # if letter in vowels and i > 0:
            if letter in vowels:
                break

        # if i > 0 and i < len(something):
        if i < len(something):
            message.send('Th{}'.format(something[i:]))


@respond_to('.*bless you,? ([^<>:\'\";]*)', re.I)
@listen_to('.*bless you,? ([^<>:\'\";]*)', re.I)
def give_bless(message, something):
    # This algorithm comes from https://github.com/jzplusplus/ThanksAnts
    # Thanks Jay Zuerndorfer.
    # Thuerndorfer.

    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'qu']

    if something:
        for i, letter in enumerate(something):
            # if letter in vowels and i > 0:
            if letter in vowels:
                break

        # if i > 0 and i < len(something):
        if i < len(something):
            message.send('Bl{}'.format(something[i:]))


@listen_to('(?:\s|^)(f)(.*)', re.I)
@respond_to('(?:\s|^)(f)(.*)', re.I)
def phantomify(message, letterf, something):
    if message.body['user'] == settings.PHANTOMIFY_USER_ID and something:
        ph = 'Ph' if letterf.isupper() else 'ph'
        message.send('I think you mean {}{}'.format(ph, something))


@respond_to('.*(/r/[A-Za-z0-9]*).*', re.I)
@listen_to('.*(/r/[A-Za-z0-9]*).*', re.I)
def reddit(message, something):

    if something:
        message.send('http://reddit.com{}'.format(something))
