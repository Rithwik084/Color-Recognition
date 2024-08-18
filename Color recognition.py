import cv2
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    
    cx = int(width/2)
    cy = int(height/2)
    
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]
    sat_value = pixel_center[1]
    val_value = pixel_center[2]

    color = "Undefined"
    
    if hue_value < 5:
        color = "Red"
    elif hue_value < 21:
        color = "Orange"
    elif hue_value < 32:
        color = "Yellow"
    elif hue_value < 78:
        color = "Green"
    elif hue_value < 131:
        color = "Blue"
    elif hue_value < 167:
        color = "Violet"
    else:
        color = "Red"
        
    if sat_value < 100 and val_value > 150:
        color = "White"
    elif val_value < 50:
        color = "Black"
    
    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    cv2.putText(frame, color, (10, 70), 0, 1.5, (b, g, r), 2)
    cv2.circle(frame, (cx, cy), 5, (0, 0, 0), 3)
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()