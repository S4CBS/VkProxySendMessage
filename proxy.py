import os
import subprocess

# Устанавливаем переменные окружения для прокси
os.environ['http_proxy'] = 'http://user:password@ip:port'
os.environ['HTTP_PROXY'] = 'http://user:password@ip:port'
os.environ['https_proxy'] = 'http://user:password@ip:port'
os.environ['HTTPS_PROXY'] = 'http://user:password@ip:port'

# subprocess.run(['python.exe','main.py'], shell=True)
subprocess.run(['main.exe'], shell=True)
