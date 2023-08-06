import cv2
 
img = cv2.imread("solar-system.jpg") 

cv2.putText(img,
            "sun",
            (100,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.9,
            (0,0,225))

cv2.putText(img,
            "Mercury",
            (100,190),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,222,0))

cv2.putText(img,
            "venus",
            (200,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,222,0))

cv2.putText(img,
            "Earth",
            (280,175),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,222,0))

cv2.putText(img,
            "Mars",
            (390,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,222,0))

cv2.putText(img,
            "Jupiter",
            (530,50),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,222,0))

cv2.putText(img,
            "Saturn",
            (820,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,222,0))

cv2.putText(img,
            "Uranus",
            (957,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,222,0))

cv2.putText(img,
            "Neptune",
            (1100,150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,222,0))

cv2.imshow("output",img)

cv2.waitKey(0)

cv2.imwrite("Solar_system_with_name.jpg",img)

