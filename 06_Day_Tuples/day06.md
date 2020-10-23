# Ngày 6 - Tuples

# Tuples
Tuple là một tập hợp các kiểu dữ liệu khác nhau được sắp xếp theo thứ tự và không thể thay đổi. 

Tuple được viết trong cặp ngoặc đơn `(...)`. Khi tạo 1 tuples, ta không thể thay đổi giá trị của nó. Vì vậy các method như add, insert, remove, .. không thể sử dụng với Tuples

Một số method sử dụng với tuples:

- `tuple()`: Tạo 1 tuple trống
- `count()`: Đếm số lượng của 1 mục được chỉ định trong 1 tuple
- `index()`: Tìm chỉ mục (index) của 1 giá trị chỉ định
- `operator`: Nối 2 hoặc nhiều tuple và tạo 1 tuple mới


# Create Tuple
### Tạo 1 tuple trống
```py
# Tạo 1 tuple trống
empty_tuple = ()

# Tạo bằng hàm tạo tuple
empty_tuple = tuple()
```

### Tạo 1 tuple với các giá trị ban đầu
```py
# Cú pháp
tpl = ('item1', 'item2','item3')
```

Ví dụ:
```py
fruits = ('banana', 'orange', 'mango', 'lemon')
```

# Tuple length
Ta có thể sử dụng `len()` để lấy độ dài của tuple:
```py
# Cú pháp
tpl = ('item1', 'item2', 'item3')
len(tpl) # Kết quả: 3
```

# Accessing Tuple Items
Tương tự như List, Tuple có index theo chiều dương từ 0, 1, 2, ...

<img src="..\image\day06\Screenshot_1.png">

```py
# Cú pháp
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
```

Ví dụ:
```py
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]

print(first_fruit) # banana
print(second_fruit) # orange
print(last_fruit) # lemon
print(last_fruit) # lemon
```

Theo chiều âm:

<img src="..\image\day06\Screenshot_2.png">

```py
# Cú pháp
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
```

# Slicing tuples
Ta có thể cắt nhỏ 1 đoạn của tuple để tạo thành 1 tuple mới:

Theo chiều dương (Positive Indexes)
```py
# Cú pháp
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # ('item1', 'item2', 'item3','item4')
all_items = tpl[0:]         # ('item1', 'item2', 'item3','item4')
middle_two_items = tpl[1:3]  # ('item2', 'item3')
```

Theo chiều âm (Negative Indexes)
```py
# Cú pháp
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # ('item1', 'item2', 'item3','item4')
middle_two_items = tpl[-3:-1]  # ('item2', 'item3')
```

# Changing Tuples to Lists
Ta có thể đổi các giá trị trong tuple thành list hoặc từ list thành tuple. Khi chuyển tuple thành list, ta có thể thay đổi giá trị trong nó.

```py
# Cú pháp
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```

Ví dụ:
```py
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```

# Checking an Item in a Tuple (Kiểm tra 1 item có trong tuple không)
```py
# cú pháp
tpl = ('item1', 'item2', 'item3','item4')
check = 'item2' in tpl
print(check)  # True
```

# Joining Tuples (ghép các tuple)
```py
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```

Ví dụ:
```py
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables) # ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
```

# Deleting Tuples
Tuy không thể chỉnh xóa 1 item trong tuple nhưng ta có thể xóa chính tuple đó
```py
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
```

Ví dụ:
```py
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
print(fruits) # NameError: name 'fruits' is not defined
```

# 💻 Exercises: Day 6
**File:** [ex-day06.py](./ex-day06.py)

1. Tạo 1 tuple trống
2. Tạo 1 tuple chứa tên của anh em trai -> `brother`. 1 tuple chứa tên của chị em gái -> `sister` (có thể lấy ví dụ tùy chọn)
3. Nối `brother` và `sister` -> `siblings`
4. Số anh chị em là bao nhiêu ?
5. Từ `siblings`, thêm tên của bố mẹ vào và lưu dưới biến `family_members`
6. 