import cv2
import numpy as np
from gpiozero import LED

myDir = "./myYoloIsTiny/"
weight = myDir + "yolov4-tiny_final.weights"
cfg = myDir + "yolov4-tiny.cfg"
name = myDir + "mynames.names"

MA1 = LED(3)
MA2 = LED(4)
MB1 = LED(6)
MB2 = LED(5)

# start video
cap = cv2.VideoCapture(0)

class YOLO:
    def __init__(self):
        self.label = []

    def getLabel(self):
        if(len(self.label)>0):
            return self.label[-1]

    def yoloCam(self, display = False):
        # video stream
        while (True):
            ret, img = cap.read()
            while (cap.isOpened()):
                height, width, channels = img.shape
                cv2.waitKey(1)

                # detect object
                blob = cv2.dnn.blobFromImage(img, 0.00392, (320, 320), (0, 0, 0), True, crop=False)
                net.setInput(blob)
                outs = net.forward(output_layers)

                # get detection result
                class_ids = []
                confidences = []
                boxes = []
                for out in outs:
                    for detection in out:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]
                        if confidence > 0.5:
                            center_x = int(detection[0] * width)
                            center_y = int(detection[1] * height)
                            w = int(detection[2] * width)
                            h = int(detection[3] * height)
                            x = int(center_x - w / 2)
                            y = int(center_y - h / 2)
                            boxes.append([x, y, w, h])
                            confidences.append(float(confidence))
                            class_ids.append(class_id)

                # remove noise: non-maximum suppression
                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

                # show detection result
                font = cv2.FONT_HERSHEY_SIMPLEX
                for i in range(len(boxes)):
                    if i in indexes.flatten():
                        x, y, w, h = boxes[i]
                        label = str(classes[class_ids[i]])
                        self.label.append(label)
                        color = colors[i]
                        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                        cv2.putText(img, label, (x, y + 30), font, 1, color, 3)

                # show video
                if(display):
                    cv2.imshow('My pi is delicious', img)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                return img

            cap.release()
            cv2.destroyAllWindows()

if __name__ == '__main__':
    # load yolo
    net = cv2.dnn.readNet(weight, cfg)
    output_layers = []
    classes = []
    with open(name, "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    for i in net.getUnconnectedOutLayers():
        output_layers.append(layer_names[i[0] - 1])
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    cnt = 0
    label_before = ""

    while True:
        y = YOLO()
        img = y.yoloCam(True)
        label = y.getLabel()
        if label != label_before:
            label_before = label
            print(label_before)
            if label_before == "click":
                cv2.imwrite("click_%d.jpg" % cnt, img)
                cv2.waitKey(10)
                cnt += 1

            elif label_before == "come":
                MA1.on()
                MB1.on()
                MA2.off()
                MB2.off()
                
            elif label_before == "go":
                MA1.off()
                MB1.off()
                MA2.on()
                MB2.on()
                
            elif label_before == "stop":
                MA1.off()
                MB1.off()
                MA2.off()
                MB2.off()

        cv2.waitKey(1)
