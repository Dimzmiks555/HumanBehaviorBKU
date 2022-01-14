from c3d.utils.array_util import *
import c3d.parameters as params
import cv2
import subprocess as sp

def get_video_clips(video_path):
    frames = get_video_frames(video_path)
    clips = sliding_window(frames, params.frame_count, params.frame_count)
    return clips, len(frames)


def get_video_frames(video_path):
    cap = cv2.VideoCapture(video_path + '.mp4')
    # print(video_path)
    # ret, frame = cap.read()
    # height, width, ch = frame.shape
    
    # ffmpeg = 'FFMPEG'
    # dimension = '{}x{}'.format(width, height)
    # f_format = 'bgr24' # remember OpenCV uses bgr format
    # fps = str(cap.get(cv2.CAP_PROP_FPS))

    # command = [ffmpeg,
    #         '-y',
    #         '-f', 'rawvideo',
    #         '-vcodec','rawvideo',
    #         '-s', dimension,
    #         '-pix_fmt', 'bgr24',
    #         '-r', fps,
    #         '-i', '-',
    #         '-an',
    #         '-vcodec', 'mpeg4',
    #         '-b:v', '5000k',
    #         output_file ]

    # proc = sp.Popen(command, stdin=sp.PIPE, stderr=sp.PIPE)

    frames = []
    cap.open(video_path)
    print(cap.isOpened(), 'открыт ли КАПП')
    while (True):
        ret, frame = cap.read()
        
        print(frame)
        if ret == True:
            frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        else:
            break
    print(frames)
    return frames