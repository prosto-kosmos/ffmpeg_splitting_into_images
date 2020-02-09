#перед запуском скачайте библиотеку
#pip install ffmpeg-python

#Установите FFmpeg и добавьте путь к  ffmpeg.exe в переменные среды

import ffmpeg
import os
import sys
import datetime 

def splitting(dir_path, time_start, time_stop):
    time_start_n = datetime.datetime.strptime(time_start, "%H:%M:%S")
    time_stop_n = datetime.datetime.strptime(time_stop, "%H:%M:%S")
    time_delta = time_stop_n-time_start_n
    os.popen('mkdir '+dir_path)
    req = 'ffmpeg -ss {time_start} -i input.mp4 -t {time_delta} {dir_path}\\image%d.png '
    
    os.popen(req.format(time_start=time_start,time_delta=time_delta,dir_path=dir_path))
    return True

if __name__ == "__main__":
    splitting(sys.argv[1],sys.argv[2],sys.argv[3])
    
