print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Viết nội dung danh sách vào tệp
def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w') as file:
            for item in data_list:
                file.write(f"{item}\n")
        print(f"Dữ liệu đã được ghi vào tệp {file_path} thành công.")
    except Exception as e:
        print(f"Đã có lỗi xảy ra: {e}")

# Ví dụ sử dụng
data_list = ['Dòng 1', 'Dòng 2', 'Dòng 3', 'Dòng 4']  # Danh sách cần ghi vào tệp
file_path = 'output.txt'  # Đường dẫn tệp đầu ra
write_list_to_file(file_path, data_list)
