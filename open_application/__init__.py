import os
import platform


def open_application(inp):
    if platform.system() == 'Darwin':
        d = '/Applications'
        apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
        if 'open' in inp:
            indx = inp.lower().split().index('open')
            app = inp.lower()[indx + 5:]
            os.system('open ' + d + '/%s.app' % app.replace(' ', '\\ '))
        elif 'start' in inp:
            indx = inp.lower().split().index('start')
            app = inp.lower()[indx + 6:]
            os.system('open ' + d + '/%s.app' % app.replace(' ', '\\ '))
        elif 'run' in inp:
            indx = inp.lower().split().index('run')
            app = inp.lower()[indx + 4:]
            os.system('open ' + d + '/%s.app' % app.replace(' ', '\\ '))
    elif platform.system() == 'Windows':
        import subprocess
        indx = inp.lower().split().index('open')
        app = inp.lower()[indx + 5:]
        subprocess.call('C:\\{}.exe'.format(app))
