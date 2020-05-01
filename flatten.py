path = "/Users/curlyz/Downloads/button-v1.0.svg"
converted = "/Users/curlyz/Downloads/button-v1.0-converted.svg"

with open(path) as f:
	lines = f.readlines()

newlines = []
for line in lines:
	if line.startswith('</g>'):
		continue
	if line.startswith('<g id='):
		continue
	newlines.append(line)

with open(converted, 'w') as f :
	f.write("\n".join(newlines))

