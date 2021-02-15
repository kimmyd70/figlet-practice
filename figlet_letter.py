import pyfiglet
from pyfiglet import Figlet

custom_fig = Figlet(font='banner3')
print()
print()
print()
print(custom_fig.renderText('CLUE'))

sword = """                           
                          ( ((
                           ) ))
  .::.                    / /(
 ' .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
( ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
 ` `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
  `::'                    \ \(
                           ) ))
                          (_((
"""
print(sword)

# https://levelup.gitconnected.com/python-ascii-art-generator-60ba9eb559d7

ascii_banner = pyfiglet.figlet_format("Clue")
print()
print()
print()
print(ascii_banner)

keyboard = """
          _________________________________________________
         /                                                /|
        / _/_/_/_/_/ _/_/_/_/_/ _/_/_/_/ _/___/ _/_/_/_/ //
       /                                                //|
      / _/_/_/_/_/_/_/_/_/_/_/_/_/__/  _/_/_/ _/_/_/_/ //||
     / __/_/_/_/_/_/_/_/_/_/_/_/_/  / _/_/_/ _/_/_/_/ //_|/    ,---------
    /_/__/_/_/_/_/_/_/_/_/_/_/_/___/   _/   _/_/_/_/ //       /__/__/__/ /|
   / __/_/_/_/_/_/_/_/_/_/_/_/__/   _/_/_/ _/_/_/ / //       /          / |
  /   __/_________________/               ___/_/_/ //       /          /  .
 /                                                //       /          / .'
(________________________________________________(/       (__________(.'
 Dirk Feeken """
 
print(keyboard)
