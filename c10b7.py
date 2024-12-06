print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

# Tìm các từ dài nhất trong văn bản
def find_longest_words(text):
    # Tách văn bản thành các từ (bỏ dấu câu và chuyển về chữ thường)
    words = text.split()
    words = [word.strip('.,!?";:()[]{}') for word in words]  # Loại bỏ dấu câu

    # Tìm chiều dài của từ dài nhất
    max_length = max(len(word) for word in words)
    
    # Lọc ra những từ có chiều dài bằng max_length
    longest_words = [word for word in words if len(word) == max_length]
    
    return longest_words

# Ví dụ sử dụng
text = "Python is an amazing programming language! It's both powerful and fun."
longest_words = find_longest_words(text)

print("Những từ dài nhất trong văn bản là:", longest_words)
