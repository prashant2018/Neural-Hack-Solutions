import os

files_list = os.listdir('./')
os.mkdir('csv')
os.mkdir('txt')
os.mkdir('mp3')
for fname in files_list:
	
	print fname

	if fname.endswith('mp3'):
		os.rename(fname,'mp3/'+fname)
	if fname.endswith('txt'):
		os.rename(fname,'txt/'+fname)
	if fname.endswith('csv'):
		os.rename(fname,'csv/'+fname)
print "Success!"