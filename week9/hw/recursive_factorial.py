import sys

# Complete the following
def factorial(n):
    if n == 0: 
        return 1
    else: 
        return n * factorial(n-1) # tạo ra 5!

# Add to the following code to prevent errors for:
# 1. No command line argument provided
def main():
    #được dùng để kiểm tra số lượng tham số truyền vào khi chạy chương trình.
    if len(sys.argv) != 2: #=> tạo ra input ngay ở terminal gồm "Tên file và số" và không quá 3 chữ file name + số only
        print ("Incorrect argument - need a single argument with a value of 0 or more.\n")
        return
    
    try:
        num = int(sys.argv[1]) #=> tạo ra input ngay ở terminal gồm số" 
        #ktra num có bé hơn 0 (âm)
        if num < 0:
            print("Incorrect argument - need a single argument with a value of 0 or more.\n")
            return

        print(factorial(num))

    except ValueError:
        # nếu ko nhập số thì sẽ print dòng dưới
        print("Incorrect argument - need a single argument with a value of 0 or more.\n")
if __name__ == "__main__":
    main()