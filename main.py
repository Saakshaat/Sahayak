'''
    @Author Saakshaat Singh
    Contact: saakshaatsin@umass.edu
'''

import random
from talk import talk

bye = ['See= you later, alligator', 'Goodbye', 'Yeah, I have to go too', 'Until Next Time']
hello = ['Hello there!', 'Howdy!', 'Welcome', 'Good to see you', 'Hi', 'Hello']
how_are_you = ['I\'ll live', 'Do you really care?', 'Like you, but better.', 'Somewhere between better and best',
               'If I were any better, I\'d be you.', 'I can\'t complain! It\'s against the Company Policy.',
               'Better now that I\'m talking to you.']
roll_a_dice = [1, 2, 3, 4, 5, 6]
fortune_cookie = ['The fortune you seek is in another cookie.',
                  'A closed mouth gathers no feet.', 'If you look back, you\'ll soon be going that way.',
                  'You will live long enough to open many fortune cookies', 'He who laughs last is laughing at you.',
                  'We don\'t know the future, but here\'s a cookie.', 'The road to riches is paved with homework.',
                  'Fortune not found? Abort, Retry, Ignore',
                  'Help! I am being held prisoner in a fortune cookie factory.',
                  'All fortunes are wrong except this one.', 'All fortunes are wrong except this one.',
                  'You love Chinese food.', 'You are not illiterate.', 'Don\'t let statistics do a number on you.',
                  'Change is inevitable, except for vending machines.', 'If a turtle doesn\'t have a shell, is it'
                                                                        ' naked or homeless?',
                  'Ask your mom instead of a cookie.', 'This cookie contains 117 calories in kilobytes.']
thank_you_replies = ['It is my pleasure.', 'You\'re welcome *blushes*', 'No problemo', 'I\'m here for you', 'Sure!']

flirt = ['I have a boyfriend. I\'m sorry.', 'I\'m a bot and you\'re a creep.',
         'You\'re kinda hot but nah',
         'I am a bot. You\'re a human. Society forbids this.', 'You\'re a 3 and I\'m a 110100100.', 'Wink Wink',
         'No, but we can be friends']


def intro():
    talk('I can do the following and much more')
    print("""
        * Just talk to you >_<n
        * Search stuff on the web :D
        * Look for stuff on Youtube
        * Send Emails .-.
        * Open Applications on your system :)
        * Roll a dice *probability noises*
        * Open a Fortune Cookie :p
        * Be a good friend
    """)


def init():
    talk(random.choice(hello))
    intro()
    while True:
        from get_command import get_command
        from assistant import assistant
        assistant(get_command())


if __name__ == "__main__":
    try:
        init()
    except KeyboardInterrupt:
        talk('Oh, alright then. {}'.format(random.choice(bye)))
        quit()
