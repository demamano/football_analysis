from ultralytics import YOLO
model = YOLO("yolov8m")

result =  model.predict("input_files/202409110515.mp4",save=True)
print(result[0])
print("====================================================")
for box in result[0].boxes:
    print(box)

