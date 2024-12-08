from PIL import Image
import os

source_folder = 'E:/f/vpn/coco128/images/train2017/'
destination_folder = 'E:/f/vpn/coco128/images/train2017 - Copy/'

# Kiểm tra nếu thư mục đích không tồn tại, tạo nó
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

directory = os.listdir(source_folder)
print(directory)

counter = 1  # Khởi tạo biến đếm từ 1

for item in directory:
    img = Image.open(source_folder + item)
    
    # Kiểm tra và chuyển đổi ảnh nếu đang ở chế độ RGBA
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    # Resize ảnh
    new_width = 640
    new_height = 640
    imgResize = img.resize((new_width, new_height))
    
    # Tạo tên mới với số thứ tự
    new_filename = f"{counter}.jpg"  # Đánh số ảnh từ 1
    imgResize.save(os.path.join(destination_folder, new_filename))
    
    # Tăng biến đếm
    counter += 1
