import math

# Level 1
## Ngày 2 : 30 ngày lập trình Python

firt_name, last_name = 'Hai','Dang'
full_name = 'Dang Do Hai'
country = 'Viet Nam'
city = 'Hung Yen'
age = 24
year = 2020
is_married = False
is_true = True
is_light_on = True

# Level 2
print(type(firt_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print('Độ dài tên: ', len(full_name))
print(max(len(firt_name), len(last_name)))

## Thực hiện các phép toán với hai số 5 và 4
num_one, num_two = 5, 4
_total = num_one + num_two
_diff = num_one - num_two
_product = num_one * num_two
_division = num_one / num_two
_remainder = num_one % num_two
_exp = num_one ** num_two

print('Tổng = ', _total)
print('Hiệu = ', _diff)
print('Tích = ', _product)
print('Thương', _division)
print('Số dư', _remainder)
print('Lũy thừa = ', _exp)

## Tính chu vi, diện tích hình tròn
_radius = float(input('Nhập vào bán kính: '))
area_of_circle = (_radius ** 2) * math.pi
circum_of_circle = 2 * _radius * math.pi

print('Diện tích hình tròn bán kính', _radius, 'là: ', area_of_circle)
print('Chu vi hình tròn bán kính', _radius, 'là: ', circum_of_circle)


## Các keyword trong python
help('keywords')