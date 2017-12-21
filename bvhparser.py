import sys

boneName = []
frameCount = 0

if (len(sys.argv)!=2):
    print 'Usage: python bvhparser.py path/to/filename'
    sys.exit()

filename = sys.argv[1]

f = file(filename).read()
words = f.split()
addNext = False


for word in words:
	if addNext:
        
		boneName.append(word + 'Xpos')
		boneName.append(word + 'Ypos')
		boneName.append(word + 'Zpos')
		boneName.append(word + 'Yrot')
		boneName.append(word + 'Xrot')
		boneName.append(word + 'Zrot')
		
		addNext = False
		
	if word == 'ROOT' or word == 'JOINT':
		addNext = True
	
	if word == 'Frames:':
		frameCount = int(words[words.index('Frames:')+1])
	if word == 'Time:':
		words = words[words.index('Time:')+2:]
		break

data = [[] for _ in range(len(boneName))]
size = len(boneName)


count = 0
for word in words:
	bin = count % size
	data[bin].append(word)
	count+=1		
	
		
f = open(filename[:filename.index('.')] + ".csv",'w')
f.write('Frames,')
for i in range(1, frameCount+1):
    f.write(str(i) + ',')
f.write('\n')

count = 0
for name in boneName:
	f.write(name + ',')
	for word in data[count]:
		f.write(word + ',')
	f.write('\n')
	count+=1
	

f.close()