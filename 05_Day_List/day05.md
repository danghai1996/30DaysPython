# Ngày 5 - List

# List
Có 4 kiểu dữ liệu thu thập trong Python:
- `List`: là 1 tập hợp được sắp xếp theo thứ tự và có thể thay đổi. Cho phép** các giá trị trùng lặp
- `Tuple`: là 1 tập hợp được sắp xếp theo thứ tự** và không thể thay đổi. Cho phép các giá trị trùng lặp
- `Set`: là tập hợp không có thứ tự, không được lập chỉ mục và không thể sửa đổi. Có thể thêm giá trị mới nhưng không được trùng.
- `Dictionary`: là tập hợp không có thứ tự, có thể sửa đổi và lập chỉ mục. Không có giá trị trùng lặp

## Tạo List
Trong Python, có 2 cách để tạo list
### Cách 1: Sử dụng hàm có sẵn
```py
lst = list()    # List không có phần tử
print(len(lst))  # 0
```

### Cách 2: Sử dụng dấu ngoặc vuông `[]`
```py
lst = []        # List không có phần tử
print(len(lst)) # 0
```

Khởi tạo các giá trị cho 1 list:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']                  
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] 
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# In ra các list và độ dài của list 
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
```
Output:
```py
Fruits: ['banana', 'orange', 'mango', 'lemon']
Number of fruits: 4
Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
Number of vegetables: 5
Animal products: ['milk', 'meat', 'butter', 'yoghurt']
Number of animal products: 4
Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
Number of web technologies: 7
Countries: ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
Number of countries: 5
```

List có thể chứa các giá trị với kiểu dữ liệu khác nhau:
```py
lsst = ['Hải', 24, True, {'country':'VietNam', 'city':'Ha Noi'}]

print(lsst)         # ['Hải', 24, True, {'country': 'VietNam', 'city': 'Ha Noi'}]
print(len(lsst))    # 4
```

## Accessing List Items Using Positive Indexing(Truy cập các mục trong List với chỉ mục dương)
List đánh thứ tự các phần tử từ 0. Xem hình minh họa:

<img src="..\image\day05\Screenshot_1.png">

Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # Phần tử đầu tiên của list 
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Vị trí của phần tử cuối cùng
last_index = len(fruits) - 1    # 3
last_fruit = fruits[last_index] # lemon
```

## Accessing List Items Using Negative Indexing (Truy cập các mục trong List với chỉ mục âm)
Ngoài cách đánh chỉ mục dương, Python còn có thể đánh chỉ mục âm từ phải sang, bắt đầu từ -1 rồi giảm dần

<img src="..\image\day05\Screenshot_2.png">

Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
```

## Unpacking List Items (Lấy các phần tử trong List)
```py
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Ví dụ 2
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Ví dụ 3
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)       # Germany
print(fr)       # France
print(bg)       # Belgium
print(sw)       # Sweden
print(scandic)  # ['Denmark', 'Finland', 'Norway', 'Iceland']
print(es)       # Estonia
```

## Slicing Items from a List (Cắt các mục từ 1 List)
### Theo chiều dương (Positive Indexing)
Ta có thể tách nhỏ 1 list thành một list khác nhỏ hơn.

Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] 
all_fruits = fruits[0:] # Nếu không đặt điểm dừng, nó sẽ lấy hết các phần tử còn lại
orange_and_mango = fruits[1:3] # từ phần tử 1 đến 3
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # Lấy các phần tử với bước nhảy đi kèm

print(all_fruits)           #['banana', 'orange', 'mango', 'lemon']
print(orange_and_mango)     #['orange', 'mango']
print(orange_mango_lemon)   #['orange', 'mango', 'lemon']
print(orange_and_lemon)     #['banana', 'mango']
```

### Theo chiều âm (Negative Indexing)
Tương tự nhưng theo chiều ngược lại, từ phải sang trái với chỉ mục âm

Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] 
orange_and_mango = fruits[-3:-1] 
orange_mango_lemon = fruits[-3:] 
reverse_fruits = fruits[::-2] 

print(all_fruits)           #['banana', 'orange', 'mango', 'lemon']
print(orange_and_mango)     #['orange', 'mango']
print(orange_mango_lemon)   #['orange', 'mango', 'lemon']
print(reverse_fruits)       #['lemon', 'orange']
```

## Modifying Lists (Chỉnh sửa List)
List là 1 tập hợp các phần tử được sắp xếp có thể thay đổi hoặc sửa đổi. 

Ví dụ: Chỉnh sửa giá trị các phần tử trong List
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
```

## Checking Items in a List (Kiểm tra sự tồn tại của 1 phần tử trong List)
Ta sử dụng với `in` để kiểm tra

Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```

## Adding Items to a List (Thêm 1 phần tử vào List)
Để thêm, ta sử dụng method `append(item)`

Cú pháp
```py
# syntax
lst = list()
lst.append(item)
```

Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
```

## Inserting Items into a List (Chèn 1 phần tử vào List)
Sử dụng `insert()` để thêm 1 phần tử vào vị trí xác định trong List. 
```py
# syntax
lst = ['item1', 'item2']
lst.insert(index, item)
```

Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # chèn 'apple' vào giữa 'orange' và 'mango'
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)
```

## Removing Items from a List (Xóa phần từ khỏi List)
Sử dụng method `remove()`. Nếu trong list có nhiều phần tử cùng giá trị với phần tử xóa thì nó sẽ xóa phần tử đầu tiên

Cú pháp
```py
# syntax
lst = ['item1', 'item2']
lst.remove(item)
```

Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - Xóa phần tử 'banana' đầu tiên xuất hiện trong list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']
```

## Removing Items Using Pop (Xóa các mục bằng `pop`)
`pop()` loại bỏ phần tử với chỉ mục chỉ định (hoặc mục cuối cùng nếu không có chỉ mục được xác định)

Cú pháp:
```py
# syntax
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(index)
```

Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.pop()        # Xóa phần tử cuối cùng của List
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(1)       # Xóa phần tử vị trí 1
print(fruits)       # ['banana', 'mango']
```

## Removing Items Using Del (Xóa phần tử với `del`)
Từ khóa `del` xóa các phần tử với chỉ mục chỉ định và nó cũng có thể được sử dụng để xóa các mục trong phạm vi chỉ mục. Nó cũng có thể xóa hoàn toàn list.

Cú pháp
```py
# syntax
lst = ['item1', 'item2']
del lst[index] # Xóa phần tử có vị trí nhất định
del lst        # Xóa toàn bộ list
```

Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']

del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']

del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']

del fruits[1:3]     # Xóa các phần tử từ 1 đến trước phần tử 3
print(fruits)       # ['orange', 'lime']

del fruits
print(fruits)       # Lỗi 'NameError: name 'fruits' is not defined' do list đã bị xóa
```

## Clearing List Items (Xóa các phần tử trong List với `clear()`)
`clear()` dùng để xóa tất cả các phần tử của list nhưng không làm mất list. Có nghĩa là biến list đó thành list rỗng (emty list)

Cú pháp
```py
# syntax
lst = ['item1', 'item2']
lst.clear()
```

Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []
```

## Copy List (Sao chép 1 list)
### Gán
Ta có thể sao chép giá trị từ lst1 sang lst2 bằng cách gán. Tuy nhiên, khi làm như vậy, lst2 sẽ là tham chiếu của lst1. Mọi thay đổi trên lst2 sẽ làm thay đổi bản gốc là lst1 và ngược lại
```py
# syntax
lst1 = ['item1', 'item2']
lst2 = lst1
```

Ví dụ:
```py
fruits1 = ['banana', 'orange', 'mango', 'lemon']
fruits2 = fruits1

# List 2 giống list1
print('List 1:', fruits1)   #List 1: ['banana', 'orange', 'mango', 'lemon']
print('List 2:', fruits2)   #List 2: ['banana', 'orange', 'mango', 'lemon']

# Sửa list2 -> list1 thay đổi theo
fruits2.append('apple')
print('List 1:', fruits1)   #List 1: ['banana', 'orange', 'mango', 'lemon', 'apple']
print('List 2:', fruits2)   #List 2: ['banana', 'orange', 'mango', 'lemon', 'apple']

# Sửa list1 -> list2 cũng thay đổi theo
fruits1.remove('banana')
print('List 1:', fruits1)   #List 1: ['orange', 'mango', 'lemon', 'apple']
print('List 2:', fruits2)   #List 2: ['orange', 'mango', 'lemon', 'apple']
```

### Sử dụng `copy()`
Trong 1 số trường hợp, ta chỉ muốn lấy 1 bản sao ra mà khi thay đổi sẽ không không làm thay đổi bản gốc. Ta sử dụng `copy()`

Cú pháp:
```py
# syntax
lst = ['item1', 'item2']
lst_copy = lst.copy()
```

Ví dụ:
```py
fruits1 = ['banana', 'orange', 'mango', 'lemon']
fruits2 = fruits1.copy()

# List 2 giống list1
print('List 1:', fruits1)   #List 1: ['banana', 'orange', 'mango', 'lemon']
print('List 2:', fruits2)   #List 2: ['banana', 'orange', 'mango', 'lemon']

# Sửa list2 -> list1 không thay đổi
fruits2.append('apple')
print('List 1:', fruits1)   #List 1: ['banana', 'orange', 'mango', 'lemon']
print('List 2:', fruits2)   #List 2: ['banana', 'orange', 'mango', 'lemon', 'apple']

# Sửa list1 -> list2 không thay đổi
fruits1.remove('banana')
print('List 1:', fruits1)   #List 1: ['orange', 'mango', 'lemon']
print('List 2:', fruits2)   #List 2: ['banana', 'orange', 'mango', 'lemon', 'apple']
```

## Join List (Nối các list)
Có một số cách để thực hiện nối các list với nhau.

### Toán tử `+`
Cú pháp
```py
# syntax
list3 = list1 + list2
```

Ví dụ:
```py
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )
```
OUPUT
```
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

### Sử dụng `extend()`
Cú pháp
```py
# syntax
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
```

Ví dụ:
```py
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )
```
OUTPUT
```
Numbers: [0, 1, 2, 3, 4, 5, 6]
Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

## Counting Items in a List (Đếm số lượng xuất hiện của 1 phần tử trong List)
Ta sử dụng `count()`

Cú pháp
```py
# syntax
lst = ['item1', 'item2']
lst.count(item)
```

Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```

## Finding Index of an Item (Tìm vị trí của 1 phần tử)
`index()` sẽ trả về vị trí (index) của phần tử trong list

Cú pháp
```py
# syntax
lst = ['item1', 'item2']
lst.index(item)
```

Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2 - vị trí xuất hiện đầu tiên trong list
```

## Reversing a List (Đảo ngược thứ tự của list)
Sử dụng `reverse()` để đảo ngược list

Cú pháp:
```py
# syntax
lst = ['item1', 'item2']
lst.reverse()
```

Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)
```
OUTPUT
```
['lemon', 'mango', 'orange', 'banana']
[24, 25, 24, 26, 25, 24, 19, 22]
```

## Sorting List Items (Sắp xếp list)
Để sắp xếp ta có thể sử dụng `sort()` hoặc `sorted()`
- `sort()`  : Sắp xếp các mục tăng dần và sửa list ban đầu. Nếu thêm `reverse=True` -> `sort(reverse=True)` thì nó sẽ sắp xếp theo thứ tự giảm dần
- `sorted()` : Tương tự như `sort()` nhưng không làm thay đổi list ban đầu

### Sử dụng `sort()`
Cú pháp
```py
# syntax
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending
```

Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # xếp theo thứ tự bảng chữ cái
fruits.sort(reverse=True)
print(fruits)
print('====================')
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)
```
OUTPUT
```
['banana', 'lemon', 'mango', 'orange']
['orange', 'mango', 'lemon', 'banana']
====================
[19, 22, 24, 24, 24, 25, 25, 26]
[26, 25, 25, 24, 24, 24, 22, 19]
```

### Sử dụng `sorted()`
Ví dụ:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))     

# Đảo ngược
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)    
```
OUTPUT
```
['banana', 'lemon', 'mango', 'orange']
['orange', 'mango', 'lemon', 'banana']
```

# 💻 Exercises - Day 5
**File:** [ex-day05.py](./ex-day05.py)

## Level 1
1. Khai báo 1 danh sách trống
2. Khai báo danh sách có hơn 5 phần tử
3. Tìm độ dài danh sách đó
4. Lấy ra thông tin phần tử đầu, giữa và cuối của danh sách đó
5. Khai báo 1 danh sách thông tin cá nhân của bạn (tên, tuổi, quốc gia, thành phố)
6. Khai báo 1 danh sách là `it_companies` gồm Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
7. In danh sách bằng `print()`
8. In số công ty trong danh sách công ty `it_companies`
9. In công ty đầu tiên, giữa và cuối cùng của danh sách
10. In danh sách công ty sau khi sửa đổi 1 công ty
11. Thêm 1 công ty vào `it_companies`
12. Chèn thêm 1 công ty vào giữa danh sách `it_companies`
13. Thay đổi tên 1 công ty thành chữ hoa (ngoài `IBM`)
14. Nối các công ty trong `it_companies` bằng `#;`
15. Kiểm tra xem 1 công ty có trong danh sách hay không
16. Sắp xếp danh sách bằng phương thức `sort()`
17. Đảo ngược danh sách theo thứ tự giảm dần bằng phương thức `reverse()`
18. cắt 3 công ty đầu tiên khỏi danh sách
19. cắt 3 công ty cuối cùng khỏi danh sách
20. Loại bỏ công ty CNTT hạng trung hoặc các công ty khỏi danh sách
21. Xóa công ty đầu tiên khỏi danh sách
22. Xóa công ty ở giữa khỏi danh sách
23. Xóa công ty cuối cùng khỏi danh sách
24. Xóa tất cả công ty khỏi danh sách
25. Xóa danh sách `it_companies`
26. Ghép 2 list
    ```
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    ```
27. Copy danh sách đã ghép ở 26 -> `full_stack`. Chèn `Python` và `SQL` vào sau `Redux`