print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

from itertools import islice

# Hàm đọc n dòng đầu tiên của tệp
def file_read_from_head(fname, nlines):
    with open(fname, 'r') as f:
        # Dùng islice để lấy n dòng đầu tiên
        for line in islice(f, nlines):
            print(line, end='')  # In dòng mà không thêm ký tự newline

# Ví dụ sử dụng
file_read_from_head('test.txt', 2)  # Đọc 2 dòng đầu tiên của tệp 'test.txt'
