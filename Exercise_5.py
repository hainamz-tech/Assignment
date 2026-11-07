c = input()
print(chr((ord(c) + 32 - 1 - ord('a')) % 26 + ord('a')))