# parenthesis character extraction

import re

p = re.compile('\([^)]+\)')
def pce(text):
    return p.findall(text)