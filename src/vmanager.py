#!/usr/bin/env python3

import sys
import os
import venv
import subprocess
from pathlib import Path

version = sys.version.split()[0]
major_minor = '.'.join(version.split('.')[:2])

argv = sys.argv
if not os.path.exists('/usr/local/bin/vmanager'):
    os.mkdir('/usr/local/bin/vmanager')
    os.mkdir('/usr/local/bin/vmanager/environments')

if argv[1] == 'help':
    print("""
help -- Shows this
new -- creates a new virtual environment (ex: vman new --name venv-name)
remove -- removes a virtual environment (ex: vman remove venv-name)
run -- runs a python file with a virtual environment (ex: vman run venv-name python-file.py)
install -- installs a package into a the selected virtual environment (ex: vman install package-name venv-name)
info -- gets the installed packages from a virtual environment (ex: vman info venv-name)
""")

if argv[1] == 'new':
    try:
        if argv[2] == '--name':
            if os.path.exists(f'/usr/local/bin/vmanager/environments/{argv[3]}'):
                print('This virtual environment already exists!')
            else:
                venv.create(Path(f'/usr/local/bin/vmanager/environments/{argv[3]}'))
    except:
        print('No name has been set! Use --name to give the virtual environment a name.')

elif argv[1] == 'remove':
    if input('Continue? Y/n: ') == 'Y':
        os.system(f'rm -r /usr/local/bin/vmanager/environments/{argv[2]}')
        print('Successfully removed the virtual environment')
    else:
        print('Cancelled')

elif argv[1] == 'run':
    subprocess.run(f'source /usr/local/bin/vmanager/environments/{argv[2]}/bin/activate && python3 {argv[3]}', shell=True,
                   executable='/bin/bash')

elif argv[1] == 'install':
    os.system(f'python3 -m pip install {argv[2]} --upgrade --target /usr/local/bin/vmanager/environments/{argv[3]}/lib/python{major_minor}/site-packages/')
    print(f"Successfully installed {argv[2]}")

elif argv[1] == 'info':
    subprocess.run(f'source /usr/local/bin/vmanager/environments/{argv[2]}/bin/activate && pip list --local', shell=True,
                   executable='/bin/bash')
