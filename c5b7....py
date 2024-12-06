print("Sinh Vien : Tran Van Nghia")
print("Ma so SV : 235752021610018")

def file_read(fname):
    with open(fname, "a") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises\n")
    with open(fname, "r") as txt:
        print(txt.read())

# Example usage
file_read('abc.txt')
