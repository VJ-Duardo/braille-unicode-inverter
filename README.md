﻿# braille-unicode-inverter

This script can transform unicode-art made up of braille characters. It can invert and rotate any given unicode-art string.

## Invert
For example this:

<p>⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠉⠉⠉⠋⠉⠉⠙⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿ <br> 
⣿⣿⣿⣿⠿⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠻⣿⣿⣿⣿⣿ <br> 
⣿⣿⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢻⣿⣿⣿ <br> 
⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⢀⣔⢤⣄⡀⠄⡄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⣿ <br> 
⠏⠄⠄⠄⠄⠄⠄⠄⢀⣀⣨⣵⣿⣿⣿⣿⣧⣦⣤⣀⣿⣷⡐⠄⠄⠄⠄⠄⢿⣿ <br> 
⠄⠄⠄⠄⠄⠄⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠄⠄⠄⢚⣿ <br> 
⣆⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣿⡿⠛⠛⠛⠛⣿⢿⣿⣿⣿⡿⢟⣻⣄⣤⣮⡝⣿ <br> 
⣿⠆⠄⠄⠄⠄⠄⠄⠄⠄⠉⠘⣿⡗⡕⣋⢉⣩⣽⣬⣭⣶⣿⣿⣿⣿⣝⣻⣷⣿ <br> 
⣿⣦⡀⠄⠄⠠⢀⠄⠄⠁⠄⠄⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿ <br> 
⣿⣿⣿⡆⠄⠄⠰⣶⡗⠄⠄⠄⣿⣿⣿⣿⣦⣌⠙⠿⣿⣿⣿⣿⣿⣿⣿⡛⠱⢿ <br> 
⣿⣿⣿⣿⡀⠄⠄⠿⣿⠄⠄⠄⠨⡿⠿⠿⣿⣟⣿⣯⣹⣿⣿⣿⣿⣿⣿⣿⣦⡀ <br> 
⣿⣿⣿⣿⣷⠄⠄⠄⢷⣦⠄⠄⠐⢶⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇ <br> 
⣿⣿⣿⣿⣿⣧⡄⠄⠄⠉⠄⠄⠄⢉⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄ <br> 
⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠈⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄ <br> 
⣿⠿⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠿⢿⣿⣿⣿⣿⣿⠿⠋⠄⠄⠄⠄</p> 

can be converted to this:

<p>⠄⠄⠄⠄⠄⠄⠄⢀⣠⣤⣶⣶⣶⣶⣴⣶⣶⣦⣤⣤⣄⣀⡀⠄⠄⠄⠄⠄⠄⠄ ⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣶⣶⣴⣶⣶⣦⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀ <br> 
⠄⠄⠄⠄⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⠄⠄⠄⠄⠄ ⠀⠀⠀⠀⣀⣴⣾⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣷⣶⣄⠀⠀⠀⠀⠀ <br> 
⠄⠄⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡄⠄⠄⠄ ⠀⠀⢠⣾⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣦⡄⠀⠀⠀ <br> 
⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⡿⠫⡛⠻⢿⣿⢻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠄⠄ ⠀⣰⣻⣻⣻⣻⣻⣻⣻⣻⡿⠫⡛⠻⢿⣻⢻⢿⣻⣻⣻⣻⣻⣻⣻⣻⣻⡄⠀⠀ <br> 
⣰⣿⣿⣿⣿⣿⣿⣿⡿⠿⠗⠊⠄⠄⠄⠄⠘⠙⠛⠿⠄⠈⢯⣿⣿⣿⣿⣿⡀⠄ ⣰⣻⣻⣻⣻⣻⣻⣻⡿⠿⠗⠊⠀⠀⠀⠀⠘⠙⠛⠿⠀⠈⢯⣻⣻⣻⣻⣻⡀⠀ <br> 
⣿⣿⣿⣿⣿⣿⣯⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢿⣿⣿⣿⡥⠄ ⣻⣻⣻⣻⣻⣻⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣻⣻⣻⡥⠀ <br> 
⠹⣿⣿⣿⣿⣿⣿⡄⠄⠄⠄⠄⢀⣤⣤⣤⣤⠄⡀⠄⠄⠄⢀⡠⠄⠻⠛⠑⢢⠄ ⠹⣻⣻⣻⣻⣻⣻⡄⠀⠀⠀⠀⢀⣤⣤⣤⣤⠀⡀⠀⠀⠀⢀⡠⠄⠻⠛⠑⢢⠀ <br> 
⠄⣹⣿⣿⣿⣿⣿⣿⣿⣿⣶⣧⠄⢨⢪⠴⡶⠖⠂⠓⠒⠉⠄⠄⠄⠄⠢⠄⠈⠄ ⠀⣹⣻⣻⣻⣻⣻⣻⣻⣻⣶⣧⠀⢨⢪⠴⡶⠖⠂⠓⠒⠉⠀⠀⠀⠀⠢⠄⠈⠀ <br> 
⠄⠙⢿⣿⣿⣟⡿⣿⣿⣾⣿⣿⠄⠄⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⠄ ⠀⠙⢿⣻⣻⣟⡿⣻⣻⣾⣻⣻⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀ <br> 
⠄⠄⠄⢹⣿⣿⣏⠉⢨⣿⣿⣿⠄⠄⠄⠄⠙⠳⣦⣀⠄⠄⠄⠄⠄⠄⠄⢤⣎⡀ ⠀⠀⠀⢹⣻⣻⣏⠉⢨⣻⣻⣻⠀⠀⠀⠀⠙⠳⣦⣀⠀⠀⠀⠀⠀⠀⠀⢤⣎⡀ <br> 
⠄⠄⠄⠄⢿⣿⣿⣀⠄⣿⣿⣿⣗⢀⣀⣀⠄⠠⠄⠐⠆⠄⠄⠄⠄⠄⠄⠄⠙⢿ ⠀⠀⠀⠀⢿⣻⣻⣀⠀⣻⣻⣻⣗⢀⣀⣀⠀⠠⠀⠐⠆⠀⠀⠀⠀⠀⠀⠀⠙⢿ <br> 
⠄⠄⠄⠄⠈⣿⣿⣿⡈⠙⣿⣿⣯⡉⡁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸ ⠀⠀⠀⠀⠈⣻⣻⣻⡈⠙⣻⣻⣯⡉⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸ <br> 
⠄⠄⠄⠄⠄⠘⢻⣿⣿⣶⣿⣿⣿⡶⠂⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣿ ⠀⠀⠀⠀⠀⠘⢻⣻⣻⣶⣻⣻⣻⡶⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣻ <br> 
⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⣿⣿ ⠀⠀⠀⠀⠀⣠⣴⣻⣻⣻⣻⣻⣻⣷⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣻⣻ <br> 
⠄⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⡀⠄⠄⠄⠄⠄⣀⣴⣿⣿⣿⣿⠀⣀⣤⣶⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣻⣧⣀⡀⠀⠀⠀⠀⠀⣀⣴⣻⣻⣻⣻ </p>  

The right-hand outcome is the default option. Giving a `True` boolean to the function will convert blank braille characters to single dot braille characters, giving the left-hand outcome. <br><br>
Due to the blank braille character being more narrow than the other braille characters, some lines can differ in length. Putting the option will combat this, but the look of the outcome may differ, especially when rotating. But generally, either option can look better depending on the input.

## Rotate
This script also allows an unicode-art string to be rotated 90°, 180° and 270°.
For example, 90°:

<p>⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠻⠟⠫⠁⠨⠀⠨⠙⠻⢿⣿⣿⣿⣿⣿⣿ <br> 
⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠡⠀⠨⠀⠨⠀⠨⠀⠨⠀⠨⠀⠉⠻⣿⣿⣿⣿ <br> 
⠨⠀⠻⣿⣿⠿⠻⠋⠡⠀⠨⠀⢈⠀⠨⠀⠨⠀⠨⠀⠨⠀⠨⠀⠨⠀⠘⢿⣿⣿ <br> 
⠨⠀⠠⠙⠩⠀⠨⠀⢨⣤⣴⡆⠢⠀⠨⠀⣈⣤⣤⣦⠨⠀⠨⠀⠨⠀⠠⠈⢿⣿ <br> 
⠨⠀⠨⠀⠈⢠⣾⠏⠻⠛⠩⠋⠈⠠⠨⠀⣿⣿⣿⣿⡆⠀⠨⠀⠨⠀⠨⠀⠈⣿ <br> 
⠨⠀⠨⠀⠨⠀⠨⠀⠨⠀⠨⠀⠨⠀⠀⣘⣿⣿⣿⣿⣷⡰⡦⡀⠨⠀⠨⠀⠀⢸ <br> 
⠨⠀⠈⢀⡈⢠⣠⡆⢴⣴⣿⣿⣿⣿⠿⡿⠙⣿⣿⣿⣿⣿⡾⠀⠨⠀⠨⠀⠀⢸ <br> 
⠨⠀⢠⣿⣿⣾⣾⣷⢸⣿⣿⣿⣿⣧⡍⢮⠀⣿⣿⣿⣿⣿⠡⠀⠨⠀⠨⠀⠀⢹ <br> 
⢠⣶⣼⣿⣿⣿⣿⣿⡿⣿⡿⢁⣿⣿⣆⢸⣤⣿⣿⣿⣿⠍⠍⠀⠨⠀⠨⠀⠀⣸ <br> 
⣾⣿⣿⣿⣿⣿⣿⣿⣿⢿⢠⣾⣿⣿⣿⢚⣾⣿⣿⣿⡟⠀⠨⠀⠨⠀⠨⠀⠀⣿ <br> 
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⡜⣿⣿⣿⣿⣿⡿⠨⠀⠨⠀⠨⠀⢰⣿ <br> 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡹⣿⣿⠟⠡⠂⠨⠀⠨⠀⠀⢰⣾⣿ <br> 
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠛⠡⠀⠨⠀⠨⠀⠈⣠⣴⣿⣿⣿ <br> 
⠨⠀⠙⢿⣿⣿⣿⣿⣿⣿⠟⣿⣿⣿⣏⣾⣿⢄⠨⠀⠨⠀⣈⣤⣶⣿⣿⣿⣿⣿ <br> 
⠨⠀⠨⠀⠨⠛⠿⠿⠟⠁⣰⣮⣭⣿⣿⣯⣭⣾⣦⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿ </p> 

180°:

<p>⠐⠐⠐⠐⣠⣶⣿⣿⣿⣿⣿⣷⣶⡄⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⣀⣤⣶⣿ <br> 
⠐⠐⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⡀⠐⠐⠐⠐⠐⠐⣠⣴⣿⣿⣿⣿⣿ <br> 
⠐⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣁⠐⠐⠐⣀⠐⠐⠘⢻⣿⣿⣿⣿⣿ <br> 
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠷⠄⠐⠐⠻⢷⠐⠐⠐⢿⣿⣿⣿⣿ <br> 
⠈⠻⣿⣿⣿⣿⣿⣿⣿⣏⣻⣿⣽⣿⣶⣶⣾⡂⠐⠐⠐⣿⣶⠐⠐⠈⣿⣿⣿⣿ <br> 
⣷⢆⣬⣿⣿⣿⣿⣿⣿⣿⣶⣄⡙⠻⣿⣿⣿⣿⠐⠐⠐⢼⠿⠆⠐⠐⠸⣿⣿⣿ <br> 
⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⠐⠐⢀⠐⠐⠁⠂⠐⠐⠈⠻⣿ <br> 
⣿⢿⣯⣝⣿⣿⣿⣿⠿⣛⡛⣟⣋⣁⣩⢜⢼⣿⡄⣀⠐⠐⠐⠐⠐⠐⠐⠐⠰⣿ <br> 
⣿⣜⡻⠛⠙⣯⣵⣾⣿⣿⣿⣷⣿⣤⣤⣤⣤⣾⣿⣿⣿⣿⣧⠐⠐⠐⠐⠐⠐⠹ <br> 
⣿⡥⠐⠐⠐⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠐⠐⠐⠐⠐⠐ <br> 
⣿⣷⠐⠐⠐⠐⠐⠌⢿⣿⠉⠛⠻⢻⣿⣿⣿⣿⢟⡋⠉⠁⠐⠐⠐⠐⠐⠐⠐⣰ <br> 
⣿⣿⣧⠐⠐⠐⠐⠐⠐⠐⠐⠐⠈⠘⠐⠈⠙⠓⠝⠁⠐⠐⠐⠐⠐⠐⠐⠐⣰⣿ <br> 
⣿⣿⣿⣧⣄⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⢀⣼⣿⣿ <br> 
⣿⣿⣿⣿⣿⣦⣀⡀⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⠐⢀⣠⣶⣿⣿⣿⣿ <br> 
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣤⣄⣀⣀⣠⣀⣀⣀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿ </p>

270°:

<p>⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⠻⡿⣛⣻⣿⣿⣛⡻⠏⢀⣴⣶⣶⣤⡂⠀⡂⠀⡂ <br> 
⣿⣿⣿⣿⣿⠿⠛⡉⠀⡂⠀⡂⠑⣿⡿⣹⣿⣿⣿⣴⣿⣿⣿⣿⣿⣿⣷⣄⠀⡂ <br> 
⣿⣿⣿⠟⠋⡀⠀⡂⠀⡂⠀⢂⣤⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄ <br> 
⣿⡿⠇⠀⠀⡂⠀⡂⠠⢂⣴⣿⣿⣎⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ <br> 
⣿⠇⠀⡂⠀⡂⠀⡂⣾⣿⣿⣿⣿⣿⡜⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿ <br> 
⣿⠀⠀⡂⠀⡂⠀⡂⠀⣼⣿⣿⣿⡿⡥⣿⣿⣿⡿⠃⣷⣿⣿⣿⣿⣿⣿⣿⣿⡿ <br> 
⡏⠀⠀⡂⠀⡂⠀⣐⣐⣿⣿⣿⣿⠛⡇⠹⣿⣿⢁⣾⣿⣾⣿⣿⣿⣿⣿⡟⠿⠃ <br> 
⣇⠀⠀⡂⠀⡂⠀⢂⣿⣿⣿⣿⣿⠀⡳⣘⢻⣿⣿⣿⣿⡇⢿⡿⡿⣿⣿⠃⠀⡂ <br> 
⡇⠀⠀⡂⠀⡂⠀⡾⣿⣿⣿⣿⣿⣄⣾⣶⣿⣿⣿⣿⠟⠗⠸⠋⠃⡈⠁⡀⠀⡂ <br> 
⡇⠀⠀⡂⠀⡂⠈⠺⠎⢿⣿⣿⣿⣿⡍⠀⠀⡂⠀⡂⠀⡂⠀⡂⠀⡂⠀⡂⠀⡂ <br> 
⣿⡀⠀⡂⠀⡂⠀⡂⠀⠸⣿⣿⣿⣿⠀⡂⠂⡀⣠⣂⣤⣦⣰⡿⠃⡀⠀⡂⠀⡂ <br> 
⣿⣷⡀⠂⠀⡂⠀⡂⠀⡂⠻⠛⠛⡉⠀⡂⠀⠢⠸⠟⠛⡃⠀⡂⠀⣂⣄⠂⠀⡂ <br> 
⣿⣿⣷⡄⠀⡂⠀⡂⠀⡂⠀⡂⠀⡂⠀⡂⠀⡁⠀⡂⠀⢂⣠⣦⣶⣿⣿⣦⠀⡂ <br> 
⣿⣿⣿⣿⣦⣀⠀⡂⠀⡂⠀⡂⠀⡂⠀⡂⠀⢂⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀ <br> 
⣿⣿⣿⣿⣿⣿⣷⣦⣄⡂⠀⡂⢀⣢⣴⣦⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧ </p>

Like the invert function, these functions have an option to replace blank braille characters with single dot braille characters.
