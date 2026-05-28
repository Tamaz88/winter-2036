from ast import literal_eval
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def initFile(path):
    if ".lift" not in path:
        raise Exception("Wrong file extension: given path must be a .lift file")
    with open(path, "r", encoding="utf-8") as file: tfile = file.read()
    tfile = tfile.replace("\n", "")
    tfile = tfile.split(";")
    content = {}
    for s in tfile:
        if len(s) > 0:
            if "::" in s:
                processed = s.split("::")
                if processed[1] == "True": pbool = True
                elif processed[1] == "False": pbool = False
                content[processed[0]] = pbool
            if "=" in s:
                pint = s.split("=")
                pint[1] = int(pint[1])
                content[pint[0]] = pint[1]
            if "#" in s:
                plist = s.split("#")
                plist[1] = []+plist[1].split(",")
                content[plist[0]] = plist[1]
                if plist[1][0] == '': content[plist[0]] = []
            if "$" in s:
                pstring = s.split("$")
                content[pstring[0]] = pstring[1]
            if "?" in s:
                pdict = s.split("?")
                content[pdict[0]] = literal_eval(pdict[1])
    return content

def saveFile(path, content):
    if ".lift" not in path:
        raise Exception("Wrong file extension: given path must be a .lift file")
    with open(path, "r", encoding="utf-8") as file: tfile = file.read()
    tfile = tfile.replace("\n", "")
    tfile = tfile.split(";")
    with open(path, "w", encoding="utf-8") as file:
        for s in tfile:
            if len(s) > 0:
                if "::" in s:
                    processed = s.split("::")
                    proc = f"{processed[0]}::{content[processed[0]]};\n"
                if "=" in s:
                    processed = s.split("=")
                    proc = f"{processed[0]}={content[processed[0]]};\n"
                if "#" in s:
                    processed = s.split("#")
                    li = ""
                    for item in content[processed[0]]:
                        li+=f"{item},"
                    li = li[0:len(li)-1]
                    proc = f"{processed[0]}#{li};\n"
                if "$" in s:
                    processed = s.split("$")
                    proc = f"{processed[0]}${content[processed[0]]};\n"
                if "?" in s:
                    processed = s.split("?")
                    li = ""
                    for item in content[processed[0]]:
                        li+=f"'{item}': {content[processed[0]][item]},"
                    li = li[0:len(li)-1]
                    proc = f"{processed[0]}?{{{li}}};\n"
                file.write(proc)

# cont = initFile("status.lift")
# saveFile("status.lift", cont)