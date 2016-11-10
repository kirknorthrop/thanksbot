var Botkit = require('botkit');
var config = require('./config');

var controller = Botkit.slackbot({
    debug: false,
    log: false
});

// connect the bot to a stream of messages
controller.spawn({
    token: config.slackBotToken,
}).startRTM();

// give the bot something to listen for.
controller.hears('thanks,? ([^<>:\'\";]*)', ['direct_message', 'direct_mention', 'mention', 'ambient'], function(bot, message) {
    // This code comes from https://github.com/jzplusplus/ThanksAnts with minor changes.
    // Thanks Jay Zuerndorfer.
    // Thuerndorfer.

    vowels = "aeiouy";
    var i;

    for(i = 0; i < message.match[1].length; i++)
    {
        if(vowels.indexOf(message.match[1][i]) != -1) {
            break;
        }
    }

    if(i > 0 && i < message.match[1].length) {
        bot.reply(message, 'Th' + message.match[1].substring(i));
    }
});
