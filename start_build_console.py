from os.path import dirname, abspath, join
from os import listdir

import sys

base_dir = dirname(abspath(sys.modules[__name__].__file__))
source_dir = join(base_dir, "source")

for lib_name in listdir(source_dir):
	sys.path.append(join(source_dir, lib_name))

from python_developer_console import PythonDeveloperConsole
from babsi.model import Podcast

podcast = Podcast(base_dir)

console = PythonDeveloperConsole()

console.locals['thewickedmu'] = podcast
console.locals['twm'] = podcast

console.interact('Welcome to "The Wicked Mu!"')
