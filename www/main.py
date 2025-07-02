import sys
import os
import eel

# Add root directory (GHOST/) to sys.path so we can import engine/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine.features import *

eel.init("www")

playAssistantSound()


os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)