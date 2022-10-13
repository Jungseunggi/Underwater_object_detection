from pytube import YouTube
from PIL import Image
from tqdm import tqdm
import cv2, os, pathlib, glob, shutil


print('주소 입력:')
url = input()
print('동영상 이름:')
file_name = input()
print('폴더 이름:')
fn = input()
folder = '../pytube/'+ fn +'/'
print('파일 이름:')
fn2 = input()

def yt_download(url):
    yt = YouTube(url)
    # yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    out_file = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print('Download is finished.')
    os.rename(out_file, file_name +'.mp4')
    # shutil.move(out_file, file_name +'.mp4')
    # os.remove(out_file)
    # os.rename(yt.streams.first().default_filename, 'test.mp4')
    # 파일명바꾸는게 자꾸 오류남
    return

    

def capture_mp4():
    
    cap = cv2.VideoCapture(file_name +'.mp4')
    if not os.path.isdir(folder):
        os.mkdir(folder)
     
    interval = 2 # 몇 초 간격으로 캡쳐를 할지 결정합니다.
    success = True
    count = 0
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = int(frame_count/fps) + 1
    fill_zero = len(str(duration))
     
    progress = ['-', '/', '|', '\\']
    print('Capture :  ', end = '')
    while success:
        success, image = cap.read()
        if count%(interval*fps) == 0 :
            second = str(int(count/fps)).zfill(fill_zero)
            prefix = fn2+'_'
            extension = '.jpg'
            filename = prefix + second + extension
            cv2.imwrite(folder + filename, image)
        print('\b' + progress[count % 4], end = '')
        count += 1
     
    list = []
    for path, subdirs, files in os.walk(folder):
        for name in files:
            list.append(os.path.join(path, name))
     
    ext_list = ['.jpg']
    for file in list:
        if os.path.getsize(file) == 0:
            if any(ext.lower() in pathlib.Path(file).suffix.lower() for ext in ext_list):
                print('\nDeleted file(s) : ', file)
                os.remove(file)
     
    cap.release()
    cv2.destroyAllWindows()
    return 


def delete_temp():
    os.remove(file_name + '.mp4')

if __name__ == '__main__':
    yt_download(url)
    capture_mp4()
    delete_temp()
    