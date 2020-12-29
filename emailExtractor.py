# Author:   Bharani Deepak.S.M
# Date:     28.12.2020
# Title:    Extract website urls using Regular Expressions

# HOW TO USE:
# Select a text -> press ctrl+C -> Run the code

import pyperclip
import re

# RegExp object for url detection
urlRegex = re.compile(r'''(
    (http|https|ftp|www)+:\/\/                  # protocol eg., http:// 
    (www\.)?                                    # www. part of url
    [a-zA-Z0-9._%*-]+                           # domain name
    \.([a-zA-Z]{2,4})\/                         # .com/de/org etc
    [a-zA-Z0-9?._%*-=&/]+                       # rest of the url path
    )''',re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())                   # text to be used
matches = []                                    # create a list to store the matches

for groups in urlRegex.findall(text):
    matches.append(groups[0])

# Copy the url found to the list and print it
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('These are the urls found:')
    print('\n'.join(matches))
else:
    print("No website urls were found")