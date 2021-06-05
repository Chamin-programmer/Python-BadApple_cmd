import time, os

if __name__ == '__main__':
	f = open('play.txt', 'r')
	frame_raw = f.read()
	frame_raw = frame_raw.replace('.', ' ')
	f.close()
	frames = frame_raw.split('SPLIT')
	init_time = time.time()
	while time.time() <= init_time + 218:
		os.system('cls')
		print(frames[int((time.time()-init_time)*10)])
		time.sleep(0.05)
		if time.time() >= init_time + 218:
		    os.system('cls')

