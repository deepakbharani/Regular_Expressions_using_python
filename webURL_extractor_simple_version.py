# Author:   Bharani Deepak.S.M
# Date:     30.12.2020
# Title:    Extract website urls using Regular Expressions

# HOW TO USE:
# Select a text -> press ctrl+C -> Run the code

import pyperclip
import re

# RegExp object for url detection
urlRegex = re.compile(r'(http://\S+|https://\S+)')      # search for URL starting with https:// (or) http://

                                                        # followed by any character that is not a space
                                                        # tab or a new line (\S)
# Find matches in clipboard text
text = str(pyperclip.paste())                           # text to be used
matchobject = urlRegex.findall(text)
print(matchobject)
if len(matchobject) > 0:                                # if matches were found then print them
    print('\n'.join(matchobject))
else:
    print("No website urls were found")                 # if no matches were found then print the message
