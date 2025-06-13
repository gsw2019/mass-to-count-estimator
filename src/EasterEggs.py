"""
A function that implements "Easter Egg" into the GUI. Inside joke for friend.

Author: Garret Wilson
Last Updated: 11/15/24
"""


import PySimpleGUI as sg


def popup_secret_word_input():
    """
    this function will create a popup with a message in-front of the main input window if the secret
    word is entered into any of the input fields (inventory data, inventory memory, output folder)

    :return: None
    """
    secret_text = r"""
 ________      ___  ___     ________       ________        ___      ________          ________         ___    ___     ________      _________    _________     ___
|\   __  \    |\  \|\  \   |\   ____\     |\   ____\      |\  \    |\   ___  \       |\   ____\       |\  \  /  /|   |\   __  \    |\___   ___\ |\___   ___\  |\  \
\ \  \|\ /_   \ \  \\\  \   \ \  \___|_    \ \  \___|_    \ \  \   \ \  \\ \  \       \ \  \___|      \ \  \/  / /   \ \  \|\  \   \|___ \  \_| \|___ \  \_|  \ \  \
 \ \   __  \   \ \  \\\  \   \ \_____  \    \ \_____  \    \ \  \   \ \  \\ \  \       \ \  \  ___     \ \    / /     \ \   __  \       \ \  \       \ \  \    \ \  \
  \ \  \|\  \   \ \  \\\  \   \|____|\  \    \|____|\  \    \ \  \   \ \  \\ \  \       \ \  \|\  \     \/  /  /       \ \  \ \  \       \ \  \       \ \  \    \ \__\
   \ \_______\   \ \_______\    ____\_\  \     ____\_\  \    \ \__\   \ \__\\ \__\       \ \_______\  __/  / /          \ \__\ \__\       \ \__\       \ \__\    \|__|
    \|_______|    \|_______|   |\_________\   |\_________\    \|__|    \|__| \|__|        \|_______|  |\___/ /           \|__|\|__|        \|__|        \|__|       ___
                               \|_________|   \|_________|                                            \|___|/                                                      |\__\
                                                                                                                                                                   \|__|    
"""
    sg.popup(secret_text, title="Secret Message", font=("Courier New", 12), line_width=170)
