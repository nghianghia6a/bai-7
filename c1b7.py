print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Mở file và xử lý
with open('D:/a.txt', 'r') as input_file:
    for line in input_file:
        # Loại bỏ ký tự xuống dòng ở cuối và đảo ngược chuỗi
        print(line.strip()[::-1])
