from ai_camera import IMX500Detector
import time

camera = IMX500Detector()

camera.start(show_preview=False)

labels = camera.get_labels()

while True:
	detections = camera.get_detections()
	
	for detection in detections:
		label = labels[int(detection.category)]
		confidence = detection.conf
		
		if label == "person" and confidence > 0.4:
			print(f"Person found with {confidence:.2f} confidence!")
			
	time.sleep(0.15)
	
