# Ngày 3 - Operators (Toán tử)

# Boolean
Kiểu dữ liệu Boolean cho 2 giá trị là: `True` và `False`. Việc sử dụng kiểu dữ liệu này sẽ rõ ràng khi chúng ta bắt đầu sử dụng toán tử so sánh.
```py
print(True)
print(False)
```

# Operators
Ngôn ngữ Python hỗ trợ một số loại toán tử. Trong phần này, chúng tôi sẽ tập trung vào một vài trong số chúng.

## Assignment Operators (Toán tử gán)
Nó được sử dụng để gán giá trị cho các biến. 

Bảng dưới đây cho thấy các loại toán tử gán khác nhau trong Python. Dữ liệu lấy từ [w3school](https://www.w3schools.com/python/python_operators.asp)

<img src="..\image\day03\Screenshot_1.png">

## Arithmetic Operators (Toán tử số học)
- Cộng(+): a + b
- Trừ(-): a - b
- Nhân(*):a * b
- Chia(/): a / b
- Chia lấy dư(%):a % b
- Chia lấy phần nguyên(//): a // b
- Lũy thừa(**):a ** b

<img src="..\image\day03\Screenshot_2.png">

## Comparison Operators (Toán tử so sánh)
<img src="..\image\day03\Screenshot_3.png">

Ví dụ: sử dụng toán tử so sánh:
```py
# Kiểm tra 1 phép so sánh có đúng hay không
print(3 > 2)    #True
print(3 >= 2)   #True
print(3 < 2)    #False

# Sử dụng lồng với các hàm khác, như len()
print(len('Hello') >= len('Hi'))    #True
print(len('Hello') < len('Hi'))    #False

# So sánh chuỗi
print('Hello' == 'Hi')  #False
print('mango' > 'mangi')    #True -> so sánh giá trị của ký tự trong bảng mã ASCSII
print('mango' == 'mango')   #True

# 
print('True == True: ', True == True)   #True
print('True == False: ', True == False) #False
print('False == False:', False == False)    #True
print('True and True: ', True and True) #True
print('True or False:', True or False)  # True
```

Ngoài việc sử dụng các toán tử so sánh ở trên, Python còn sử dụng:
- `is` : trả về `True` nếu cả 2 biến là cùng 1 đối tượng (object). (`x is y`)
- `is not` : trả về `True` nếu 2 biến không cùng 1 đối tượng (object). (`x is not y`)
- `in` : trả về `True` nếu danh sách được truy vấn chứa 1 mục nhất định (`x in y`) 
- `not in` : trả về `True` nếu danh sách được truy vấn không chứa 1 mục nhất định (`x not in y`) 

Ví dụ:
```py
print('1 is 1', 1 is 1)             # True
print('1 is not 2', 1 is not 2)     # True
print('H in Hai', 'H' in 'Hai')     # True
print('B in Hai', 'B' in 'Hai')     # False 
print('Hai' in 'Dang Do Hai')       # True 
print('4 is 2 ** 2:', 4 is 2 ** 2)  # True
```

## Logical Operators (Toán tử logic)
Python sử dụng các toán tử logic: `and`, `or`, `not`

<img src="..\image\day03\Screenshot_4.png">

Ví dụ:
```py
print(3 > 2 and 4 > 3) # True
print(3 > 2 and 4 < 3) # False
print(3 < 2 and 4 < 3) # False 
print(3 > 2 or 4 > 3)  # True
print(3 > 2 or 4 < 3)  # True
print(3 < 2 or 4 < 3)  # False
print(not 3 > 2)     # False
print(not True)      # False
print(not False)     # True
print(not not True)  # True
print(not not False) # False
```

# 💻 Exercises - Day 3
**File:** [ex-day03.py](./ex-day03.py)

1. Khai báo tuổi của mình dưới dạng số nguyên (integer)
2. Khai báo chiều cao của bạn dưới dạng float
3. Khai báo 1 biến số phức
4. Viết tập lệnh yêu cầu người dùng nhập độ dài đáy và chiều cao của 1 tam giác -> in ra diện tích tam giác
    ```py
    Nhập độ dài đáy: 20
    Nhập chiều cao: 10
    Diện tích tam giác: 100
    ```
5. Nhập độ dài 3 cạnh của tam giác -> in ra chu vi tam giác
    ```py
    Nhập cạnh a: 5
    Nhập cạnh b: 4
    Nhập cạnh c: 3
    Chu vi tam giác: 12
    ```
6. Nhập chiều dài và chiều rộng của hình chữ nhật -> in ra diện tích và chu vi hình chữ nhật
7. Nhập bán kính -> in diện tích và chu vi hình tròn
11. Tính giá trị của `y = x^2 + 6x + 9` . `x` nhập vào từ bàn phím
12. Tìm độ dài của `python'` và `jargon` và thực hiện một phát biểu so sánh sai.
13. Sử dụng `and` và toán tử để kiểm tra xem `on` có trong 2 từ `python` và `jargon` hay không
14. Kiểm tra trong câu `I hope this course is not full of jargon.` có từ `jargon` không
15. Kiểm tra mệnh đề: "Không có `on` trong `dragon` và `python`"
16. Tìm độ dài của từ `python` và chuyển nó về float, sau đó là string
17. Kiểm tra 1 số có phải số chẵn không
18. Chia lấy nguyên 7/3
19. Kiểm tra '10' có bằng 10 không
20. Kiểm tra `int(9.8)` có bằng `10` không
21. Viết đoạn code, nhập số giờ làm, lương mỗi giờ -> tính lương người đó
    ```py
    Nhập số giờ làm:5
    Nhập lương mỗi giờ: 30
    Tổng lương:  150.0
    ```
22. Nhập vào số năm -> tính ra thời gian bằng giây
    ```py
    Nhập số năm: 10
    10 năm =  315360000 giây
    ```

23. Viết tập lệnh hiển thị bảng sau:
    ```py
    1 1 1 1 1
    2 1 2 4 8
    3 1 3 9 27
    4 1 4 16 64
    5 1 5 25 125
    ```