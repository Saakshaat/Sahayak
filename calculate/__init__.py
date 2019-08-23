import wolframalpha


def calculate(inp):
    from assistant import assistant
    from talk import talk
    from get_command import get_command
    try:
        app_id = 'W4PGT4-6EL82797RH'
        client = wolframalpha.Client(app_id)
        indx = inp.lower().split().index('calculate')
        query = inp.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        talk("The answer is " + answer)
    except:
        talk('There was some issue. Try again?')
        assistant(get_command())
