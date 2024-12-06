print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Sao chép nội dung từ tệp này sang tệp khác
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()  # Đọc toàn bộ nội dung của tệp nguồn
        with open(destination_file, 'w') as dest:
            dest.write(content)  # Ghi nội dung vào tệp đích
        print(f"Nội dung đã được sao chép từ {source_file} sang {destination_file} thành công.")
    except FileNotFoundError:
        print(f"Tệp nguồn {source_file} không tồn tại.")
    except Exception as e:
        print(f"Đã có lỗi xảy ra: {e}")

# Ví dụ sử dụng
source_file = 'source.txt'  # Tên tệp nguồn
destination_file = 'destination.txt'  # Tên tệp đích
copy_file(source_file, destination_file)
