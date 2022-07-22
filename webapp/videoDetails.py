# import cv2
# import datetime
# import os

# from pathlib import Path

# data = cv2.VideoCapture('http://127.0.0.1:8000/videos/videos/5._Install_JDK_10_on_a_Mac.mp4')

# frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
# print(frames)

# fps = data.get(cv2.CAP_PROP_FPS)
# print(fps)

# seconds = frames / fps
# minute = seconds / 60
# print(minute)
# video_time = datetime.timedelta(seconds=seconds)
# print(video_time)

# def convert_bytes(num):
#     """
#     this function will convert bytes to MB.... GB... etc
#     """
#     for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
#         if num < 1024.0:
#             return "%3.1f %s" % (num, x)
#         num /= 1024.0

# def file_size(file_path):
#     """
#     this function will return the file size
#     """
#     if os.path.isfile(file_path):
#         file_info = os.stat(file_path)
#         return convert_bytes(file_info.st_size)
        
# file_size()

