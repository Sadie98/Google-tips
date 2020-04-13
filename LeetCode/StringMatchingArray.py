words = ["blue","green","bu"]

def substring(string: str, substr: str) -> bool:
    for i in range(len(string) - len(substr) + 1):
        if string[i:i + len(substr)] == substr:
            return True
    return False


ans = set()
for checkWord in words:
    for subWordCheck in words:
        if subWordCheck == checkWord:
            pass
        else:
            if substring(subWordCheck, checkWord):
                ans.add(checkWord)

print(list(ans))
