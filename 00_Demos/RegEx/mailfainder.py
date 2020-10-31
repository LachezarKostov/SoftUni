import re
text = input()
regex = r'[ |^][a-zA-Z][a-zA-Z0-9\-*\.*\_*]+@[a-zA-Z][a-zA-Z0-9\-*\.*]+[.][a-zA-Z]+'

mails = []
mails += re.findall(regex, text)

print("\n".join(mails))
