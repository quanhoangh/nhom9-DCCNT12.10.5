from ultralytics import YOLO

# Tải mô hình đã huấn luyện trước
model = YOLO('last.pt')

# Hoặc bắt đầu từ đầu với file cấu hình

results = model.train(data='coco8xl.yaml', epochs=50 , imgsz=640)