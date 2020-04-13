text = "&apos; &lt;&gt;"
characters = {
    '&quot;': "\\\"",
    '&apos;': "'",
    '&amp;': "&",
    '&gt;': ">",
    '&lt;': "<",
    '&frasl;': "/",
}

i = 0
while i < len(text):
    move = False
    if text[i] == '&':
        for word in characters.keys():
            if text[i:i + len(word)] == word:
                text = text.replace(text[i:i + len(word)], characters[word])
                i += len(characters[word])
                move = True
    if not move:
        i += 1
print(text)