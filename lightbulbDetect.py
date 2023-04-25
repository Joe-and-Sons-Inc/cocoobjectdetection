import matlab.engine
import cv2

def detectLightbulbProportion(webcam=0):
    eng = matlab.engine.start_matlab()
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 224)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 224)
    cap.set(cv2.CAP_PROP_FPS, 36)
    ret, image = cap.read()
    results = eng.lightbulbDetect(image)
    eng.quit()
    return results["proportion"], results["maskedImage"]

def isLightbulb():
    prop, _ = detectLightbulbProportion()
    return prop > 0.02

