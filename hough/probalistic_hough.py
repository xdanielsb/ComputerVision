import cv2
import numpy as np

"""
    This function read an image
"""
def readi(path, typer = "color"):
    if typer == "color":
        return cv2.imread(path, 1)
    elif typer == "gray":
        return cv2.imread(path, 0)


"""
    Show image for a certain time
    time -> miliseconds
    0 is an execption
"""
def time_show_image(time = 0):
    #0 means, show the image indefenetely until any keypress
    #25 means, show the image for 25 miliseconds
    if time == 0:
        print("\n\tPlease, press any key for finish the program")
    cv2.waitKey(time)

"""
    Close windows and de-allocate memory asociated with it.
"""
def close_windows():
    cv2.destroyAllWindows()



def Hough_transformlines(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    lines = []
    for minLineLength in range (10, 100):
        for maxLineGap in range (10,11):
            lines.extend( cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap))

    for l in lines:
        for x1,y1,x2,y2 in l:
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

    cv2.imshow("Hough transform", img)


if __name__ == "__main__":

    img = readi('../assets/images/sudoku.png')
    Hough_transformlines(img)
    time_show_image()
    close_windows()
