import cv2
from ultralytics import YOLO

# Tải mô hình (có thể thay 'yolov5s' bằng 'yolov8n', 'yolov8s', v.v.)
model = YOLO('last.pt')

# Đọc ảnh
img_path = 'img_1.png'  # Đường dẫn tới ảnh của bạn
img = cv2.imread(img_path)

# Nhận diện
results = model(img)
results = results[0]

# Hiển thị kết quả
results.show()  # Hiển thị ảnh với bounding boxes
# results.save('output.jpg')  # Lưu kết quả
