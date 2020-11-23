import os   #with this import, we will be able to use the command lines of the terminal in atom (python)

#in this script I just call the command lines that I have used in the previous exercises
#as in the terminal, I access to the bunny video with the addecuate command lines
os.system('ls') #we write the command line inside this function
os.system('cd Desktop')

#EX1
os.system('ffmpeg -ss 00:04:18 -i bbb.mp4 -to 00:00:10 -c copy bbb10sec.mp4')

#EX2
os.system('ffplay bbb10sec.mp4 -vf histogram')
os.system('ffplay bbb10sec.mp4 -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay"')

#EX3
os.system('ffmpeg -i bbb10sec.mp4 -filter:v scale=720:-2 -c:a copy bbb10sec720.mp4')
os.system('ffmpeg -i bbb10sec.mp4 -filter:v scale=480:-2 -c:a copy bbb10sec480.mp4')
os.system('ffmpeg -i bbb10sec.mp4 -filter:v scale=360:240 -c:a copy bbb10sec360x240.mp4')
os.system('ffmpeg -i bbb10sec.mp4 -filter:v scale=160:120 -c:a copy bbb10sec160x120.mp4')

#EX4
os.system('ffmpeg -i bbb10sec.mp4 -ac 1 bbb10secmono.mp4')
os.system('ffmpeg -i bbb10sec.mp4 -acodec eac3 -vcodec copy bbb10secDolbyDigitalPlus.mp4')
