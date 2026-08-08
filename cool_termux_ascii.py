#!/usr/bin/env python3
import os
import sys
import time

# เคลียร์หน้าจอ
os.system("clear")

# ASCII ART ฟีลเดียวกับภาพ
ART = r"""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XX                                                        XX
XX        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM        XX
XX      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM      XX
XX     MMMMMMMMMMSSSSSSSSSSSSSSSSSSSSMMMMMMMMMM       XX
XX    MMMMMMMMMSSSSSSSSSSSSSSSSSSSSSSSMMMMMMMMM       XX
XX    MMMMMMMMSSSSSSSSSSSSSSSSSSSSSSSSSMMMMMMMM       XX
XX    MMMMMMMSSSSSSSSSSSSSSSSSSSSSSSSSSMMMMMMM       XX
XX          . . .       ______       . . .             XX
XX              .-"""-./      \.-"""-.                 XX
XX             /      /  o  o  \      \                XX
XX            |      |    __    |      |               XX
XX            |      |  \____/  |      |               XX
XX             \      \        /      /                XX
XX              '-.___ '------' ___.-'                 XX
XX                  /  MMMMMM  \                       XX
XX              MMMMMMMMMMMMMMMMMMMM                   XX
XX            MMMMMMMMMMMMMMMMMMMMMMMM                 XX
XX          MMMMMMMMMMMMMMMMMMMMMMMMMMMM               XX
XX        MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM             XX
XX      MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM           XX
XX    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM         XX
XX                                                        XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

       o8o       .oooo.       .oooo.       .oooo.
       `"'      .dP""Y8b     .dP""Y8b     .dP""Y8b
     oooo      888   888    888   888    888   888
     `888      888ooo888    888ooo888    888ooo888
      888      888   888    888   888    888   888
      888      `Y8bod8P'    `Y8bod8P'    `Y8bod8P'
     o888o
"""

print(ART)
print()

# แถบโหลดแบบในคลิป
width = 45
for percent in range(101):
    filled = int(width * percent / 100)
    bar = "█" * filled + " " * (width - filled)
    sys.stdout.write(f"\r|{bar}| {percent}%")
    sys.stdout.flush()
    time.sleep(0.025)

print("\n")
print(">>> SYSTEM READY")
print(">>> Welcome to Termux")
