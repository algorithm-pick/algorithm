text = input().strip()
text = text.replace('XXXX', 'AAAA')
text = text.replace('XX', 'BB')
if 'X' in text:
    print(-1)
else:
    print(text)