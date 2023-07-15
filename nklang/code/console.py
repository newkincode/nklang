import re
import lib.pce

def log(code:str):
    text = code.replace("console.log", "")
    return lib.pce.pce(text)