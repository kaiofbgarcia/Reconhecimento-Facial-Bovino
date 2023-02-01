import cv2 
def FrameCapture(path): 
    vidObj = cv2.VideoCapture(path) 
    count = 1 #Começa no numero do frame que deseja
    success = 1
    while success: 
        success, image = vidObj.read() 
        image = cv2.flip(image, 0) #Deixar comentado se o video estiver na horizontal
        cv2.imwrite("frame%d.jpg" % count, image) 
        count += 1
if __name__ == '__main__': 
    FrameCapture("C:\\Users\\kaiof\\Desktop\\Imagens de Teste\\Branquinha48 Test\\I1.mp4") #Colocar caminho para o video desejado





    