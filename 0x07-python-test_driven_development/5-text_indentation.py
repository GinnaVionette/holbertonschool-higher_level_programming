#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    i = 0
    text_length = len(text)
    while i < text_length:
        result += text[i]
        if text[i] in {'.', '?', ':'}:
            result += "\n\n"
            while i + 1 < text_length and text[i + 1] == '':
                i += 1
                i += 1
                for line in result.split("\n"):
                    print(line.strip())
