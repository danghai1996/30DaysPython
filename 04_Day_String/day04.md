# Ngày 4 - Strings

# Strings
Văn bản(text) là kiểu dữ liệu `string`. Bất kỳ văn bản nào được viết dưới dạng chuỗi đều là kiểu `string`. Có nhiều các string method và hàm tích hợp sẵn để xử lý dữ liệu kiểu `string`. Ví dụ: để kiểm tra độ dài của chuỗi, sử dụng hàm `len()`

# Creating a String (Tạo 1 chuỗi)
1 chuỗi có thể là 1 ký tự đơn hoặc nhiều văn bản.
```py
_text = 'H'
print(_text)
print(len(_text))

_sentences = 'Một chuỗi có thể là 1 đoạn văn bản !'
print(_sentences)
print(len(_sentences))
```

Chuỗi nhiều dòng được tạo bằng cách sử dụng dấu nháy ba (`'''`) hoặc (`"""`)
```py
multiline_string = '''Sử dụng dấu nháy đơn 3 lần.
Ta có thể tạo văn bản nhiều dòng.
Đó là cách tạo chuỗi trong Python !'''
print(multiline_string)
print(len(multiline_string))
#------#
multiline_string2 = """Sử dụng nháy kép 3 lần.
Ta cũng có kết quả tương tự.
Đó là cách tạo chuỗi trong Python !"""
print(multiline_string2)
print(len(multiline_string2))
```

# String Concatenation (Nối chuỗi)
Ta có thể nối các chuỗi với nhau để thành 1 văn bản thống nhất.
```py
first_name = 'Hai'
last_name = 'Dang'
space = ' '
full_name = first_name + space + last_name

print(full_name)
#Kiểm tra độ dài các chuỗi
print(len(first_name))
print(len(last_name))
print(len(space))
print(len(full_name))
```

# Escape Sequences in Strings
Trong python, ta có thể in ra dấu tab, xuống dòng, in ký tự `'`, `"`, `\`, ...
|Ký hiệu|Ý nghĩa|
|-------|-------|
|`\n`|Xuống dòng|
|`\t`|Tạo 1 dấu tab|
|`\\`|In ra ký tự `\`|
|`\'`|In ra ký tự `'`|
|`\"`|In ra ký tự `"`|

Ví dụ:
```py
print('Tôi hy vọng mọi người đều thích tài liệu về Python này !\nBạn thì sao?')
print('Ngày\tChủ đề')
print('Ngày 1\tIntroduction')
print('Ngày 2\tVariables và Builtin function')
print('Ngày 3\tOperators')
print('Ngày 4\tStrings')

print('Ta có thể in ra dấu nháy đơn \' và dấu nháy kép \"')
print('Tương tự với dấu gạch chéo \\')
```
Output
```py
Tôi hy vọng mọi người đều thích tài liệu về Python này !
Bạn thì sao?
Ngày    Chủ đề
Ngày 1  Introduction
Ngày 2  Variables và Builtin function
Ngày 3  Operators
Ngày 4  Strings
Ta có thể in ra dấu nháy đơn ' và dấu nháy kép "
Tương tự với dấu gạch chéo \
```

# String formating (Định dạng chuỗi)
## Old Style String Formating (% Operator) - Định dạng chuỗi kiểu cũ. Sử dụng toán tử `%`
Trong Python có nhiều cách tạo chuỗi. Toán tử `%` được sử dụng để định dạng 1 tập hợp các biến nằm trong 1 `tuple` (1 list có kích thước cố định).
|Toán tử|Giải thích|
|-------|----------|
|`%s`|Giá trị dạng string (str)|
|`%d`|Giá trị kiểu số nguyên (int). Nếu là số thực thì chỉ hiển thị phần nguyên|
|`%f`|Giá trị kiểu số thực (float)|
|`%.<số chữ số thập phân>f`|Giá trị kiểu số thực (float) với số chữ số thập phân|

Ví dụ:
```py
# Strings only
first_name = 'Hai'
last_name = 'Dang'
country = 'Việt Nam'
formated_string = 'Tôi tên là %s %s. Tôi sống tại %s' %(first_name, last_name, country)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'Chu vi hình tròn có bán kính %d là %.2f.' %(radius, area)

python_libraries = ['Django', 'Flask', 'Numpy', 'Pandas']
formated_string = 'Theo dõi các thư việc của Python:%s' % (python_libraries)
print(formated_string)
```

## New Style String Formating (str.format) - Định dạng chuỗi kiểu mới được sử dụng `.format`
Định dạng này xuất hiện từ Python3 trở lên. Hãy xem kỹ ví dụ dưới đây để hiểu được cách sử dụng của nó.

Ví dụ:
```py
# String
first_name = 'Hai'
last_name = 'Dang'
country = 'Việt Nam'
formated_string = 'Tôi tên là {} {}. Tôi sống tại {}'.format(first_name, last_name, country)
print(formated_string)


# Number
a = 10
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # Giới hạn 2 chữ số thập phân

# Strings  and numbers
radius = 5
pi = 3.14
area = pi * radius ** 2
formated_string = 'Chu vi hình tròn có bán kính {} là {:.2f}'.format(radius, area) # Lấy 2 chữ số thập phân sau dấu phẩy
print(formated_string)
```

Output
```py
Tôi tên là Hai Dang. Tôi sống tại Việt Nam
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.33
Chu vi hình tròn có bán kính 5 là 78.50
```

## String Interpolation / f-Strings (Python 3.6+)
Các chuỗi bắt đầu bằng `f` và chúng có thể đưa dữ liệu vào các vị trí tương ứng của chúng.

Ví dụ:
```py
a = 2
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} mod {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ^ {b} = {a ** b}')
```
Ouput
```
2 + 3 = 5
2 - 3 = -1
2 * 3 = 6
2 / 3 = 0.67
2 mod 3 = 2
2 // 3 = 0
2 ^ 3 = 8
```

# Python Strings as Sequences of Characters (Chuỗi dưới dạng chuỗi ký tự)
Để trích xuất các ký tự có trong chuỗi, đó là giải nén chúng thành các biến tương ứng

## Unpacking Characters
Giải nén chuỗi vào các biến. Yêu cầu số biến phải bằng độ dài của chuỗi

Ví dụ:
```py
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
```
Output
```
P
y
t
h
o
n
```
Tuy nhiên, với cách này khi xử lý 1 chuỗi nhiều ký tự thì sẽ rất khó khăn

## Accessing Characters in Strings by Index
Truy cập ký tự trong chuỗi bằng chỉ mục (index). Trong lập trình, việc đếm sẽ bắt đầu từ 0.

<img src="..\image\day04\Screenshot_1.png">

Ví dụ:
```py
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
```

Nếu ta muốn bắt đầu từ bên phải, thì index sẽ bắt đầu từ -1 rồi -2, -3, ...

Ví dụ:
```py
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o
```

## Slicing Python Strings (Cắt chuỗi)
Trong python, ta có thể cắt chuỗi thành các chuỗi nhỏ (substrings)

**Cú pháp:**
```
<chuỗi>[vị trí con trỏ bắt đầu : vị trí con trỏ kết thúc]
```

Ví dụ 1: Cắt xuôi
```py
fullname = 'HaiDang'
first_name = fullname[0:3] # Bắt đầu từ 0 lên tới 3 nhưng không bao gồm ký tự tại index 3
last_name = fullname[3:7]

print('First name :', first_name)
print('Last name :', last_name)
```
Output
```
First name : Hai
Last name : Dang
```

Ví dụ 2: Cắt ngược
```py
fullname = 'HaiDang'
first_name = fullname[:-4]
last_name = fullname[-4:]

print('First name :', first_name)
print('Last name :', last_name)
```
Output
```
First name : Hai
Last name : Dang
```

**Lưu ý:**
- Nếu ta để trống giá trị đầu (Ví dụ: `[:3]`) thì có nghĩa là lấy từ vị trí đầu đến vị trí xác định
- Nếu ta để trống giá trị cuối (Ví dụ: `[3:]`) thì có nghĩa là lấy từ vị trí xác định đến cuối chuỗi

## Passing step (Bước nhảy)
**Mặc định:** khi không khai báo thì bước nhảy bằng 1.

Cú pháp:
```
<chuỗi>[vị trí bắt đầu : vị trí dừng : bước nhảy]
```

Ví dụ:
- Mặc định bước nhảy là 1
```py
_string = 'Python'
print(_string[0:7])
print('Bước nhảy mặc định là 1: ',_string[0:7:1])

#==Output==
Python
Bước nhảy mặc định là 1:  Python
```

- Bước nhảy là 2:
```py
_string = 'Python'
print('Chuỗi ban đầu:', _string[0:7])
print('Bước nhảy là 2: ',_string[0:7:2])

#==Output==
Chuỗi ban đầu: Python
Bước nhảy là 2:  Pto
```

- Ta có thể lấy từ phải sang trái bằng cách dùng bước nhảy âm:
```py
_string = 'Python'
print('Chuỗi ban đầu:', _string[0:7])
print('Bước nhảy là -3 và lấy từ phải sang trái: ',_string[7:0:-3])

#==Output==
Chuỗi ban đầu: Python
Bước nhảy là -3 và lấy từ phải sang trái:  nt
```

## Reversing a String (Đảo ngược chuỗi)
Để đảo ngược chuỗi, ta sử dụng bước nhảy âm là `-1`

Ví dụ:
```py
_string = 'Python'
print('Chuỗi ban đầu:', _string[0:7])
print('Chuỗi ngược: ',_string[::-1])

#==Output==
Chuỗi ban đầu: Python
Chuỗi ngược:  nohtyP
```

# String methods (Phương thức chuỗi)
Có nhiều string method cho phép ta định dạng chuỗi. Xem một số phương thức dưới đây:

- `capitalize()`: Chuyển ký tự đầu tiên thành chữ in hoa
    ```py
    _string = 'python là ngôn ngữ lập trình'
    print(_string.capitalize()) # Python là ngôn ngữ lập trình
    ```

- `count()` : Đếm số lần xuất hiện của 1 substring trong 1 chuỗi hoặc 1 đoạn của chuỗi. ` count(substring, start=.., end=..)`
    ```py
    _string = 'python là ngôn ngữ lập trình'
    print(_string.count('n'))           # 5
    print(_string.count('n', 10, 14))   # 2
    print(_string.count('ng'))          # 2
    ```

- `endswith()`: Kiểm tra 1 chuỗi có kết thúc bằng phần cuối chỉ định hay không
    ```py
    _string = 'python là ngôn ngữ lập trình'
    print(_string.endswith('trình'))    # True
    print(_string.endswith('mình'))     # False
    ```

- `expandtabs()`: Thay thế tab bằng dấu cách. Có thể chèn đối số kích thước tab
    ```py
    _string = 'python\tlà\tngôn\tngữ\tlập\ttrình'
    print(_string.expandtabs())     # 'python  là      ngôn    ngữ     lập     trình'
    print(_string.expandtabs(10))   # 'python    là        ngôn      ngữ       lập       trình'
    ```

- `find()`: Trả về vị trí đầu tiên của chuỗi con. Nếu không có thì trả về `-1`
    ```py
    _string = 'python là ngôn ngữ lập trình'
    print(_string.find('ngôn'))     # 10
    print(_string.find('người'))    # -1
    ```

- `rfind()` : Trả về vị trí cuối cùng của chuỗi con. Nếu không có thì trả về `-1`
    ```py
    _string = 'python là ngôn ngữ lập trình'
    print(_string.rfind('n'))       # 26
    print(_string.rfind('người'))   # -1
    ```

- `format()`: Định dạng đầu ra

- `index()` : Trả về chỉ số thấp nhấp của 1 substring
    ```py
    _string = 'python là ngôn ngữ lập trình'
    print(_string.index('ngôn'))       # 10
    print(_string.index('người'))      # ERROR
    ```

- `rindex():` : Trả về chỉ số thấp nhấp của 1 substring
    ```py
    _string = 'python là ngôn ngữ lập trình'
    print(_string.rindex('ngôn'))       # 10
    print(_string.rindex('người'))      # ERROR
    ```

- `isalnum()` : Kiểm tra ký tự chữ và số
    ```py
    _string = '30DaysPython'
    print(_string.isalnum())    # True

    _string1 = 'python là ngôn ngữ lập trình'
    print(_string1.isalnum())   # False - do dấu cách không phải ký tự chữ hoặc số
    ```

- `isalpha()`: Kiểm tra ký tự chữ. Tất cả là ký tự chữ (a-z, A-Z) thì True, không thì False
    ```py
    _string = 'Python'
    print(_string.isalpha())    # True       
    
    _string1 = '30Days Python'
    print(_string1.isalpha())   # False
    ```

- `isdecimal()`: Kiểm tra ký tự là số (0-9)
    ```py
    _string = '30 Days Python'
    print(_string.isdecimal())  # False       
    
    _string1 = '12326487'
    print(_string1.isdecimal()) # True
    ```

- `isidentifier()` : Kiểm tra xem tên giá trị có được dùng làm biến hay không
    ```py
    _string = '30DaysPython'
    print(_string.isidentifier())      # False - Do bắt đầu là ký tự số 
    
    _string1 = 'days4python'
    print(_string1.isidentifier())      # True
    ```

- `islower()` : Kiểm tra xem tất cả các ký tự có phải ký tự thường hay không
    ```py
    _string = '30DaysPython'
    print(_string.islower())       # False
    
    _string1 = 'days4python'
    print(_string1.islower())       # True
    ```

- `isupper()` : Kiểm tra xem tất cả các ký tự có phải ký tự hoa hay không
    ```py
    _string = '30DaysPython'
    print(_string.isupper())       # False
    
    _string1 = 'DAY4PYTHON'
    print(_string1.isupper())       # True
    ```

- `join()` : Trả về chuỗi được nối lại với nhau với mã nối được khai báo
    ```py
    web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
    result = '# '.join(web_tech)
    print(result) # 'HTML# CSS# JavaScript# React'
    ```

- `strip()` : Removes all given characters starting from the beggining and end of the string(Loại bỏ tất cả ký tự đã cho khỏi từ đầu và kết thúc) 
    ```py
    _string = '30 Days Python'
    print(_string.strip('oyn'))  # 30 Days Pyth
    ```

- `replace()`: Thay thế 1 substring bằng 1 string
    ```py
    _string = '30 Days Python'
    print(_string.replace('Python', 'Coding'))   # 30 Days Coding
    ```

- `split()` : Tách chuỗi đã cho. Sử dụng chuỗi thêm vào xác định dấu phân tách
    ```py
    _string = '30 Days Python'
    print(_string.split())       # ['30', 'Days', 'Python']
    
    _string1 = '30, Days, Python'
    print(_string1.split(', '))  # ['30', 'Days', 'Python']
    ```

- `title()` : Viết hoa các chữ cái đầu của từ trong chuỗi
    ```py
    _string = '30 days python'
    print(_string.title())  # 30 Days Python
    ```

- `swapcase()` : Đổi chữ hoa thành thường và ngược lại
    ```py
    _string = '30 Days Python'
    print(_string.swapcase())    # 30 dAYS pYTHON
    
    _string1 = '30 days python'
    print(_string1.swapcase())  # 30 DAYS PYTHON
    ```

- `startswith()` : Kiểm tra chuỗi có bắt đầu bằng chuỗi chỉ định không
    ```py
    _string = '30 Days Python'
    print(_string.startswith('30'))       # True
    
    _string1 = '30 days python'
    print(_string1.startswith('python'))    # False
    ```

# 💻 Exercises - Day 4
**File:** [ex-day04.py](./ex-day04.py)

1. Nối chuỗi: "30", "Days", "of", "Python" thành "30DaysofPython"
2. Nối chuỗi: 'Coding', 'For' , 'All' thành 'Coding For All'
3. Đặt 1 biến là `company` và gán cho nó `Coding For All`
4. In biến `company` ở mục 3 bằng `print`
5. In độ dài biến `company` ở trên
6. Thay đổi tất cả ký tự của biến `company` thành chữ in hoa
7. Thay đổi tất cả ký tự của biến `company` thành chữ thường
8. Sử dụng các phương thức `capitalize()`, `title()`, `swapcase()` để định dạng giá trị của biến `company`
9. Cắt từ đầu tiên của chuỗi `Coding For All` trong biến `company`
10. Kiểm tra xem biến `company` có chứa từ `Coding` không?
11. Đổi từ `Coding` trong biến `company` thành `Python`
12. Thay `Python for Everyone` thành `Python for All`
13. Tách chuỗi `Coding For All` trong biến `company` dấu phân cách là dấu cách (space)
14. Tách chuỗi `Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon` ngăn cách bằng dấu phẩy `,`
15. Tìm ký tự tại index = 0 trong biến `company`
16. Chỉ số cuối cùng của chuỗi `Coding For All`
17. Ký tự nào ở index = 10 trong biến `company`
20. Xác định vị trí đầu tiên của chữ `C` trong chuỗi `Coding For All`
21. Xác định vị trí đầu tiên của chữ `F` trong chuỗi `Coding For All`
22. Sử dụng `rfind` để xác định vị trí của lần xuất hiện cuối cùng của `l` trong `Coding For All People`
23. Sử dụng `find()` hoặc `index()` để tìm vị trí xuất hiện đầu tiên của từ `because` trong câu sau: `You cannot end a sentence with because because because is a conjunction`
24. Sử dụng `rindex()` để tìm vị trí xuất hiện cuối cùng của từ `because` trong câu sau: `You cannot end a sentence with because because because is a conjunction`
25. Cắt bỏ cụm từ `because because because` trong câu: `You cannot end a sentence with because because because is a conjunction`
26. Tìm vị trí xuất hiện đầu tiên của `because` trong câu: `You cannot end a sentence with because because because is a conjunction`
28. Kiểm tra `Coding For All` có bắt đầu bằng `Coding` không?
29. Kiểm tra `Coding For All` có kết thúc bằng `coding` không?
30. `   Coding For All      `. Hãy xóa các khoảng trắng bên trái và bên phải của chuỗi
31. Biến nào sau đây trả về True khi ta sử dụng `isidentifier()`
    - `30DaysOfPython`
    - `thirty_days_of_python`
32. Danh sách sau có tên của 1 số thư viện Python `['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']`. Ghép chúng thành chuỗi, phân cách bằng dấu cách
33. Sử dụng dấu xuống dòng để in ra văn bản sau:
    ```
    I am enjoying this challenge.
    I just wonder what is next.
    ```
34. Sử dụng dấu tab, xuống dòng để in ra văn bản sau:
    ```
    Name      Age     Country
    Asabeneh  250     Finland
    ```
35. Sử dụng string formating để hiển thị như dưới đây
    ```
    radius = 10
    area = 3.14 * radius ** 2
    The area of a cricle with radius 10 is 314 meters square.
    ```
36. Sử dụng string formating để hiển thị:
    ```
    8 + 6 = 14
    8 - 6 = 2
    8 * 6 = 48
    8 / 6 = 1.33
    8 % 6 = 2
    8 // 6 = 1
    8 ** 6 = 262144
    ```