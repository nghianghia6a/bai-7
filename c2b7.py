print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Mở file và đọc nội dung
with open('D:/a.txt', 'r', encoding='utf-8') as file:
    char_count = 0  # Đếm số ký tự
    word_count = 0  # Đếm số từ
    line_count = 0  # Đếm số dòng

    for line in file:
        char_count += len(line)  # Tổng số ký tự trong dòng
        word_count += len(line.split())  # Số từ trong dòng
        line_count += 1  # Tăng số dòng

# In kết quả
print(f"Số ký tự: {char_count}")
print(f"Số từ: {word_count}")
print(f"Số dòng: {line_count}")
