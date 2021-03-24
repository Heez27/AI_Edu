#'tree.raw'라는 binary파일을 화면에 출력시키시오

from tkinter import *

def loadImage(fname):
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb') #read binary

    for i in range(0,XSIZE):
        tmpList = []
        for k in range(0,YSIZE):
            data = int(ord(fp.read(1)))
            tmpList.append(data)
        inImage.append(tmpList)

    fp.close()

def displayImage(image):
    global XSIZE, YSIZE
    for i in range(0,XSIZE):
        for k in range(0,YSIZE):
            data = image[i][k]
            paper.put('#%02x%02x%02x'%(data, data, data),(k,i))



window = None
canvas = None
XSIZE, YSIZE = 256, 256
inImage = []

#메인코드
window = Tk()
window.title('흑백 사진 보기')
canvas = Canvas(window, width = XSIZE, height = YSIZE)
#canvas = Canvas(window, height = XSIZE, width = YSIZE)
paper = PhotoImage(width = XSIZE, height = YSIZE)
canvas.create_image((XSIZE / 2, YSIZE / 2), image = paper, state = 'normal')

#파일-->메모리
#fname = input('파일 이름을 입력하시오: ')
fname = 'tree.raw'
loadImage(fname) #해당 파일을 inImage리스트에 불러들임

#메모리 --> 화면
displayImage(inImage) #윈도창에 출력

canvas.pack()
window.mainloop() #X(실행중지를 클릭하기 전까지 명령 입력을 기다리는 함수
