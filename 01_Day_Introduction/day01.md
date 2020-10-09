# Ngày 1 - Introduction

# Giới thiệu
Python là ngôn ngữ lập trình bậc cao. Nó là mã nguồn mở (open source).

Phiên bản Python sử dụng trong tài liệu này sẽ là Python3.

# Tại sao sử dụng Python ?
Python là ngôn ngữ lập trình rất gần với ngôn ngữ con người, và vì thế nó rất dễ học và sử dụng. 

Python được sử dụng trong nhiều ngành công nghiệp và công ty khác nhau (trong đó có cả Google)

Python được sử dụng để phát triển các ứng dụng web, ứng dụng máy tính, quản trị hệ thống và thư viện machine learning. Python được chấp nhận là ngôn ngữ lập trình bậc cao trong cộng đồng data science và machine learning

# Cài đặt môi trường
## Install Python
Truy cập https://www.python.org/ để tải và cài đặt Python theo đúng hệ điều hành mà bạn sử dụng

Kiểm tra phiên bản Python:
```py
python --version
Python 3.7.9
```

## Python shell
Python là 1 ngôn ngữ kịch bản thông dịch ( Có nghĩa là nó sẽ thực thi từng dòng trong code của bạn), vì vậy nó cần được phiên dịch để máy tính có thể hiểu được.

Python đi kèm với Python shell (Python Interactive Shell). Nó được dùng để thực hiện 1 lệnh và nhận kết quả

Python Shell đợi python code từ người dùng. Khi bạn gõ 1 dòng code, nó sẽ thực hiện giải mã và hiển thị kết quả tại dòng tiếp theo.

Từ terminal, gõ `python`
```py
python
```

<img src="..\image\day01\Screenshot_1.png">

Để thoát, gõ lệnh
```py
exit()
```

Khi bạn nhập 1 lệnh sai, bạn sẽ nhận được 1 thông báo lỗi:

<img src="..\image\day01\Screenshot_2.png">

Thực hiện tính toán một số phép tính đơn giản:

- Phép cộng: `3 +5`
- Phép trừ: `5 - 3`
- Phép nhân: `3 * 5`
- Phép chia: `5 / 3`
- Phép chia lấy dư: `8 % 3`
- Phép chia lấy phần nguyên, bỏ số dư: `8 // 3`
- Phép lũy thừa: `2 ** 3`

<img src="..\image\day01\Screenshot_3.png">

Thử nhập văn bản:

<img src="..\image\day01\Screenshot_4.png">

# Cài đặt Visual Studio Code
Python interactive shell rất tốt để thử và kiểm tra các dòng lệnh nhỏ, nhưng nó sẽ không dùng trong 1 dự án lớn. Trong thực tế, các nhà phát triển sử dụng các trình soạn thảo code (code editor) khác nhau để viết code.

Trong các bài viết này, tôi sẽ sử dụng Visual Studio Code. Visual Studio Code là 1 trình soạn thảo phổ biến và rất đa năng. 

[Tải Visual Studio Code](https://code.visualstudio.com/)

Cài đặt thêm tiện ích (Extension) : `ms-python.python`

<img src="..\image\day01\Screenshot_5.png">

Chọn đường dẫn tới thư mục cài đặt Python

<img src="..\image\day01\Screenshot_6.png">

Thử tạo 1 file python `helloworld.py`
```py
print('Hello World !!!')
```
Sau đó, chạy Run file:

<img src="..\image\day01\Screenshot_7.png">

Vậy là bạn đã có 1 chương trình Python đầu tiên của mình (hoặc không phải =)))

# Python cơ bản
## Python Syntax
Các tập lệnh python có thể đặt trong 1 file `.py`

Ví dụ: `helloworld.py`

## Thụt lề trong Python (Python Indentation)
Thụt lề là 1 khoảng trắng trong văn bản.

Thụt lề trong nhiều ngôn ngữ lập trình được sử dụng để trình bày code rõ ràng, tuy nhiên, trong Python thì thụt lề là để tạo khối mã.

Một trong những lỗi hay gặp khi code Python là thụt lề sai.

<img src="..\image\day01\Screenshot_8.png">

## Comment trong Python
Comment rất quan trọng trong bất kỳ ngôn ngữ lập trình nào và Python cũng không ngoại lệ. Nó giúp code của ta dễ đọc và những lưu ý trong 1 phần code nào đó. 

Python sẽ không chạy các nội dung là comment

Bất kỳ dòng văn bản nào bắt đầu với dấu `#` đều được tính là comment.

**Ví dụ:**

Comment 1 dòng đơn lẻ:
```py
# Đây là 1 comment
# Python đang xâm chiếm thế giới
# Hãy ăn nótrước khi điều đó xảy ra
```

Comment 1 đoạn: 3 dấu ngoặc kép có thể sử dụng để comment 1 đoạn nhiều dòng
```py
"""Đây là 1 comment
Python đang xâm chiếm thế giới
Hãy ăn nótrước khi điều đó xảy ra
"""
```

## Kiểu dữ liệu (Data Type)
Trong Python có một số kiểu dữ liệu. Hãy xem một số loại phổ biến. Các kiểu dữ liệu khác nhau sẽ được đề cập chi tiết trong các phần khác.

Hãy xem qua những kiểu dữ liệu phổ biến.

### Number
- Integer: kiểu số nguyên (...,-3, -2, -1, 0, 1, 2, 3,...)
- Float: Số thực (..., -3.5, -2.2, -0.54, 0.0, 1.2314, 2.6, 3.0, ...)

### String
Tập hợp 1 hay nhiều ký tự dưới 1 dấu nháy đơn (`'...'`) hoặc nháy kép (`"..."`)

Ví dụ:
```py
'Hello World'
"Python"
```

### Booleans
Booleans có 2 giá trị là True và False. Ký tự đầu tiên `T` và `F` luôn phải viết hoa.

Ví dụ:
```py
True  #  Is the light on? If it is on, then the value is True
False # Is the light on? If it is off, then the value is False
```

### List
Python list là 1 tập hợp có thứ tự cho phép lưu trữ các mục có kiểu dữ liệu **khác nhau**. Một python list tương tự 1 array (mảng) trong JavaScript.

Ví dụ:
```py
[0, 1, 2, 3, 4, 5]  # Tất cả các phần từ cùng kiểu dữ liệu số - List number
['Banana', 'Orange', 'Mango', 'Avocado'] # Tất cả cùng kiểu dữ liệu String - List fruits
['Finland','Estonia', 'Sweden','Norway'] # Tất cả cùng kiểu dữ liệu String - List countries
['Banana', 10, False, 9.81] # Các phần tử có kiểu dữ liệu khác nhau - string, number, boolean, float
```

### Dictionary
Một **python dictionary object** là 1 tập hợp dữ liệu không có thứ tự ở định dạng `key:value`

Ví dụ:
```py
{'name':'HaiDD', 'country':'VietNam', age:24, 'is_married':False}
```

### Tuple
Giống như ***List*** nhưng không thể thay đổi các bộ giá trị sau khi chúng được tạo. Chúng là bất biến (immutable)

Ví dụ:
```py
('Ha Noi', 'Da Nang', 'Ho Chi Minh City')
```

### Set
**Set** là một tập hợp các kiểu dữ liệu khác nhau như ***List*** và ***Tuple***

Không giống ***List*** và ***Tuple***, **Set** không phải 1 tập hợp các mục có thứ tự. Giống như trong toán học, **Set** trong python chỉ những item duy nhất.

Ví dụ:
```py
{3.14, 9.81, 2.7} # Thứ tự không quan trọng trong Set
```


Trong các phần sau, ta sẽ đi chi tiết về các kiểu dữ liệu này.

## Check Data types
Để kiểm tra kiểu dữ liệu của 1 dữ liệu hay 1 biến, ta sử dụng hàm `type`.

Xem ví dụ dưới đây ta sẽ thấy các kiểu dữ liệu khác nhau:
```py
>>> type(10)
<class 'int'>
>>>
>>> type(3.14)
<class 'float'>
>>>
>>> type('Hello')
<class 'str'>
>>>
>>> type([1,2,3])
<class 'list'>
>>>
>>> type({'name':'HaiDD', 'age':'24'})
<class 'dict'>
>>>
>>> type((4,5,6))
<class 'tuple'>
>>>
>>> type({3.4, 5.6, 7.5})
<class 'set'>
```

<img src="..\image\day01\Screenshot_9.png">

# 💻 Bài tập
## Level 1
1. Kiểm tra phiên bản Python đang sử dụng: **Python 3.7.9**
    Thực hiện trên terminal
    ```py
    python --version
    ```

    <img src="..\image\day01\Screenshot_10.png">

2. Truy cập  python interactive shell và thực hiện các phép toán dưới đây. 2 toán hạng là 3 và 4.
    - Cộng (+)
    - Trừ (-)
    - Nhân (*)
    - Chia lấy dư (%)
    - Chia (/)
    - Lũy thừa(**)
    - Chia lấy phần nguyên(//)

    <img src="..\image\day01\Screenshot_11.png">

3. Viết các thông tin sau trên python interactive shell
    - Your name
    - Your country
    - Age

    <img src="..\image\day01\Screenshot_12.png">

4. Kiểm tra các kiểu dữ liệu:

    <img src="..\image\day01\Screenshot_9.png">

## Level 2
Thực hiện 4 mục ở level 1 trong 1 file python.

File: [ex-day01.py](./ex-day01.py)

**Kết quả:**

<img src="..\image\day01\Screenshot_13.png">