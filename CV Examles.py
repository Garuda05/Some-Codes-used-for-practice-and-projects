import numpy as np
import cv2
def main():
    img1 = np.zeros((512, 512, 3), np.uint8)
    windowName = "OpenCV BGR Color Palelte"
    cv2.namedWindow(windowName)
    
    while(True):
        cv2.imshow(windowName, img1)
        
        
        if cv2.waitKey(1)==27:
            break
        
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()