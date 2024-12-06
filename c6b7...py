print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

import os

# Hàm đọc n dòng cuối cùng của tệp
def file_read_from_tail(fname, lines):
    bufsize = 8192  # Kích thước bộ đệm
    fsize = os.stat(fname).st_size  # Lấy kích thước tệp
    iter = 0
    data = []

    with open(fname) as f:
        # Nếu kích thước bộ đệm lớn hơn kích thước tệp, chỉnh lại kích thước bộ đệm
        if bufsize > fsize:
            bufsize = fsize - 1
        
        while True:
            iter += 1
            f.seek(fsize - bufsize * iter)  # Di chuyển con trỏ tệp
            data.extend(f.readlines())  # Đọc các dòng từ tệp

            # Nếu đã đủ số dòng hoặc đã đến cuối tệp, in ra kết quả
            if len(data) >= lines or f.tell() == 0:
                print(''.join(data[-lines:]))  # In ra các dòng cuối cùng
                break

# Ví dụ sử dụng
file_read_from_tail('test.txt', 2)  # Đọc 2 dòng cuối cùng của tệp 'test.txt'
