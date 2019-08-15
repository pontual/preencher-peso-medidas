import sys
from time import sleep
from pyautogui import click, press, typewrite
import pyautogui

# Formato

sample = """
143143 14 30 33,5 35,5
...
"""

def fillprod(cod, p, l, w, h):
    click(43, 16)
    press("f3")
    sleep(0.5)

    click(90, 123)
    typewrite(cod)
    sleep(0.5)
    typewrite('\n')

    sleep(0.5)
    click(727, 373)
    click(75, 339, clicks=2)
    typewrite(p)
    click(401, 447)
    typewrite(l)
    click(504, 447)
    typewrite(w)
    click(594, 447)
    typewrite(h)
    click(586, 497)

    # save
    click(66, 56)

    sleep(2.5)
    
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit("uso: python preencher.py ARQUIVO_COM_CODIGOS")
    pyautogui.PAUSE = 0.3
    input("Feche todas as janelas menos Produto. Escolha Produto e pressione Enter.")
    
    with open(sys.argv[1]) as f:
        for line in f:
            if len(line.strip()) > 0:
                cod, p, l, w, h = line.split()
                print("cod", cod, p, "kg", l, w, h, "cm")
                fillprod(cod, p, l, w, h)
