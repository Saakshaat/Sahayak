import os
import platform


def open_application(inp):
    if platform.system() == 'Darwin':
        print('This is a mac')
        d = '/Applications'
        apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
        indx = inp.lower().split().index('open')
        app = inp.lower()[indx + 5:]
        os.system('open ' + d + '/%s.app' % app.replace(' ', '\\ '))

    elif platform.system() == 'Windows':
        import subprocess
        indx = inp.lower().split().index('open')
        app = inp.lower()[indx + 5:]
        subprocess.call('C:\\{}.exe'.format(app))
