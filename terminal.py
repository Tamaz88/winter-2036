import sys
from shutil import get_terminal_size
from os import system, _exit
from random import randint, choice
from math import floor, ceil
from time import sleep
from colorama import Fore, Back, Style

def terminlaLicense():
    print("Tamaz made ts ig")

def _greaterList(lists):
    greatest = []
    for li in lists:
        if len(li) > len(greatest): greatest = li
    return greatest

def get_terminal_width():
    columns, _ = get_terminal_size(fallback=(80, 24))
    return columns

def get_terminal_height():
    _, rows = get_terminal_size(fallback=(80, 24))
    return rows

def refresh():
    print(get_terminal_size().columns*" ", end="\r")

def centerText(line, padding=0):
    terminal_size = get_terminal_size()
    screen_width = terminal_size.columns
    if padding == 0: padding = (screen_width - len(line)) // 2

    if padding > 0:
        return " " * padding + line
    else:
        return line
    
def centeredInput(prompt="", clear=True):
    centered_prompt = centerText(prompt)
    sys.stdout.write(centered_prompt)
    sys.stdout.flush()
    user_input = sys.stdin.readline().strip()
    if clear:
        sys.stdout.write("\033[F\033[K")
        sys.stdout.flush()
    return user_input

def alert(e, sleepTime=0.02, clear=True, lingerTime=1, framed=False):
    end = "\r" 
    frame1 = ""
    frame2 = ""
    for l in range(len(e)):
        if framed:
            frame1 = "["
            frame2 = f"{" "*(len(e)-l-1)}]"
        if l == len(e)-1: end = "\n"
        print(centerText(frame1+e[:l+1]+frame2), end=end)
        sleep(sleepTime)
    sleep(lingerTime)
    if clear: refresh()

def printAsciiArt(text=list, center=True):
    if center:
        for line in text:
            print(centerText(line))
    else:
        for line in text:
            print(line)

def event(text=list, eventfunc="pass", clear=True):
    for line in text:
        if line != "":
            line = line.replace("BLANK", "")
            for l in range(len(line)):
                print(centerText(line[:l+1]), end="\r")
                sleep(0.01)
            print()
            sleep(1)
        else: 
            centeredInput("[ENTER]")
            refresh()
            print()
    exec(eventfunc)
    if clear: system("cls")

def connectAsciiArt(texts=list, p=6):
    product = []
    max_rows = len(_greaterList(texts))
    for ii in range(max_rows):
        subproduct = []
        for i, text in enumerate(texts):
            padding = p * " " if i < len(texts) - 1 else ""
            try:
                subproduct.append(text[ii] + padding)
            except IndexError:
                subproduct.append(" " * len(text[0]) + padding)
        product.append("".join(subproduct))
    return product

def createBox(w:int, h:int, content:list, boxType:int=0):
    boxTypes = [
        {
            "ur": "┐",
            "ul": "┌",
            "ll": "└",
            "lr": "┘"
        },
        {
            "ur": "α",
            "ul": "α",
            "ll": "α",
            "lr": "α"
        },
        {
            "ur": ">",
            "ul": "<",
            "ll": "<",
            "lr": ">"
        }
    ]
    if len(content)>h: h = len(content)
    for line in content:
        if len(line)>w: w = len(line)
    box = [f"{boxTypes[boxType]["ul"]}─"+"─"*w+f"─{boxTypes[boxType]["ur"]}"]
    for i in range(h+1):
        if i == h: line = f"{boxTypes[boxType]["ll"]}─"+"─"*w+f"─{boxTypes[boxType]["lr"]}"
        else: 
            try:
                line = "│ " + (content[i]+" "*(w-len(content[i]))) + " │"
            except IndexError:
                line = "│ "+" "*w+" │"
        box.append(line)
    return box

def invertScreen(clear=False):
    if not clear:
        print(Fore.BLACK)
        print(Back.WHITE)
    else:
        print(Fore.RESET)
        print(Back.RESET)
    for _ in range(get_terminal_height()):
        for _ in range(get_terminal_width()):
            print(" ", end="")
        print()
    system("cls")