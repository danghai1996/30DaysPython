# Ngày 2 - Variables, Builtin Functions (Biến và các function có sẵn)

## Các function tích hợp sẵn trong Python
Trong python có rất nhiều function được tích hợp sẵn. Một số function phổ biến được sử dụng: `print()`, `len()`, `type()`, `int()`, `float()`, `str()`, `input()`, `list()`, `dict()`, `min()`, `max()`, `sum()`, `sorted()`, `open()`, `file()`, `help()`, `dir()`.

Bảng các function được tích hợp sẵn trong Python. Dữ liệu được lấy từ [Python documentation](https://docs.python.org/2/library/functions.html)

<img src="..\image\day02\Screenshot_1.png">

Ví dụ :

<img src="..\image\day02\Screenshot_2.png">

## Variables - Biến
Các biến sẽ lưu trữ dữ liệu trong bộ nhớ máy tính. Nó được khuyến khích sử dụng trong việc lập trình.

Quy tắc về biến trong Python:
- Biến phải được bắt đầu bằng ký tự chữ hoặc dấu gạch dưới (`_`)
- Biến phân biệt ký tự HOA-thường . ví dụ: `abc`, `Abc`, `ABC`, `aBc` là các biến khác nhau
- Không được bắt đầu bằng ký tự số. 
- Không được sử dụng ký tự đặc biệt
- Không sử dụng dấu gạch ngang (`-`)
- Không đặt tên biến trùng với reserved words.

Để hiển thị các reserved word. Gõ lệnh sau trên shell của Python:
```py
help('keywords')
```
Kết quả:
```py
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
```

<img src="..\image\day02\Screenshot_3.png">


Một số ví dụ về tên biến hợp lệ:
```py
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # Nếu muốn đặt tên chứa reserved words
year_2020
year2020
current_year_2020
num1
num2
```

Một số tên biến không hợp lệ:
```py
first-name
num-1
1num
```

Khi đặt tên biến dài, nên sử dụng dấu gạch dưới để nối (`_`)

Ví dụ: `first_name`, `last_name`, ...

Khi ta gán 1 kiểu dữ liệu cho 1 biến thì nó được gọi là khai báo biến.

Ví dụ:
```py
first_name = 'Hai'
last_name = 'Dang'
country = 'Viet Nam'
age = 24
is_married = False
```
hoặc có thể khai báo trên cùng 1 dòng:
```py
first_name, last_name, country, age, is_married = 'Hai', 'Dang', 'Viet Nam', 24, False
```

Sử dụng các hàm có sẵn `print()` và `len()`. `print()` sẽ nhận nhiều đối số (arguments). Đối số là một giá trị mà chúng ta truyền hoặc đặt bên trong dấu ngoặc đơn.

**Ví dụ:**
```py
print('Hello, World!')
print('Hello',',', 'World','!') # Nhận nhiều đối số
print(len('Hello, World!')) # nhận 1 đối số là kết quả của hàm len()
```

<img src="..\image\day02\Screenshot_4.png">

Sử dụng `print()` với các biến:
```py
first_name = 'Hai'
last_name = 'Dang'
country = 'Viet Nam'
age = 24
is_married = False

print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
```

<img src="..\image\day02\Screenshot_5.png">

Ta có thể sử dụng hàm `input()` để nhận giá trị từ bàn phím nhập vào:
```py
first_name = input('What is your name: ')
age = input('How old are you? ')

print('Name', first_name)
print('Age:', age)
```

<img src="..\image\day02\Screenshot_6.png">

## Kiểm tra kiểu dữ liệu (Data Type) và ép kiểu (Casting)
### Kiểm tra kiểu dữ liệu (Data type)
Để kiểm tra kiểu dữ liệu, ta dùng `type()`

Ví dụ:
```py
first_name = 'Hai'
last_name = 'Dang'
country = 'Viet Nam'
age = 24
is_married = False

print(type(first_name))
print(type(last_name))
print(type(country))
print(type(age))
print(type(is_married))
print(type(10))
print(type(3.14))
```

<img src="..\image\day02\Screenshot_7.png">

### Ép kiểu (Casting)
Để chuyển đổi kiểu dữ liệu sang 1 kiểu dữ liệu khác.

Ví dụ:
```py
# int to float

num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int

gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int
num_str = '10.6'
print('num_int', int(float(num_str)))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)
print(first_name)                    # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
```

## Numbers
Kiểu dữ liệu số trong Python:
- Interger : Số nguyên. Ví dụ: ... -3, -2, -1, 0, 1, 2, 3 ...
- Float : Số thực. Ví dụ: ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
- Complex Numbers : Số phức. Ví dụ: 1 + j, 2 + 4j, 1 - 1j

# 💻 Bài tập
## Level 1: 
- Tạo 1 file `.py`
- Viết comment: `Ngày 2 : 30 ngày lập trình Python`
- Khai báo các biến sau và gán giá trị cho chúng:
    - `firt_name`
    - `last_name`
    - `full_name`
    - `country`
    - `city`
    - `age`
    - `year`
    - `is_married`
    - `is_true`
    - `is_light_on`
- Khai báo nhiều biến trên 1 dòng

## Level 2:
1. Kiểm tra kiểu dữ liệu của các biến trên
2. Tìm độ dài tên của bạn
3. So sánh độ dài của tên và họ của bạn
4. Khai báo `5` là `num_one`, `4` là `num_two`
    - Thực hiện cộng 2 số `num_one` và `num_two` -> kết quả `_total`
    - Lấy `num_one` trừ đi `num_two` -> kết quả `_diff`
    - Nhân `num_two` với `num_one` và -> `_product`
    - Chia `num_one` cho `num_two` -> `_division`
    - Tính số dư khi chia `num_one` cho `num_two` -> `_remainder`
    - Tính lũy thừa `num_one` mũ `num_two` -> `_exp`

5. Bán kính của hình tròn là 30 mét
    - Tính diện tích hình tròn -> `area_of_circle`
    - Chu vi hình tròn -> `circum_of_circle`
    - Lấy bán kính làm đầu vào của người dùng và tính toán diện tích

**File:** [ex-day02.py](./ex-day02.py)