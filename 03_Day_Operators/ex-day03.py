# Khai báo cơ bản
_age = 24
_height = 1.63
_complex = 3 + 2j

print('Tuổi:', _age)
print('Chiều cao:', _height)
print('Số phức: ', _complex)

print('-----------------------')
# Tính diện tích tam giác
_base = float(input('Nhập độ dài đáy: '))
_hight = float(input('Nhập chiều cao: '))
_area = float(0.5 * _base * _hight)
print('Diện tích tam giác: ', _area)

print('-----------------------')
# Tính chu vi tam giác
_a = float(input('Nhập độ dài cạnh a:'))
_b = float(input('Nhập độ dài cạnh b:'))
_c = float(input('Nhập độ dài cạnh c:'))
_perimeter = float(_a + _b + _c)
print('Chu vi tam giác: ', _perimeter)

print('-----------------------')
# Tính chu vi và diện tích hình chữ nhật
_length = float(input('Nhập chiều dài:'))
_width = float(input('Nhập chiều rộng: '))
rect_area = float(_length * _width)
rect_perimeter = float(2 * (_length + _width))
print('Diện tích hình chữ nhật: ', rect_area)
print('Chu vi hình chữ nhật: ', rect_perimeter)

print('-----------------------')
# Tính chu vi và diện tích hình tròn
_radius = float(input('Nhập vào bán kính: '))
pi = float(3.14)
area_of_circle = float((_radius ** 2) * pi)
circum_of_circle = float(2 * _radius * pi)

print('Diện tích hình tròn bán kính', _radius, 'là: ', area_of_circle)
print('Chu vi hình tròn bán kính', _radius, 'là: ', circum_of_circle)

print('-----------------------')
# Tính giá trị biểu thức
x = int(input('Nhập giá trị của x: '))
y = x**2 + 6*x + 9
print('Giá trị y = ', y)

print('-----------------------')
# Tìm độ dài của `python'` và `jargon` và thực hiện một phát biểu so sánh sai.
print('Độ dài của python', len('python'))
print('Độ dài của jargon', len('jargon'))
print(len('python') > len('jargon'))

print('-----------------------')
# Sử dụng `and` và toán tử để kiểm tra xem `on` có trong 2 từ `python` và `jargon` hay không
print(('on' in 'python') and ('on' in 'jargon'))

print('-----------------------')
# Kiểm tra trong câu `I hope this course is not full of jargon.` có từ `jargon` không
print('jargon' in 'I hope this course is not full of jargon`')

print('-----------------------')
# Kiểm tra mệnh đề: "Không có `on` trong `dragon` và `python`"
print(('on' not in 'dragon') and ('on' not in 'python'))

print('-----------------------')
# Tìm độ dài của từ `python` và chuyển nó về float, sau đó là string
_py = 'python'
print(type(float(len(_py))))
print(type(str(len(_py))))

print('-----------------------')
# Kiểm tra 1 số có phải số chẵn không
_number = int(input('Nhập 1 số nguyên: '))
print('Là số chẵn ?', _number % 2 == 0)

print('-----------------------')
# Chia lấy nguyên 7/3
print('7 chia 3 có phần nguyên : ', 7//3)

print('-----------------------')
# Kiểm tra '10' có bằng 10 không
print('Chuỗi "10" có bằng 10 không?','10' == 10)

print('-----------------------')
# Kiểm tra int(9.8) có bằng 10 không
print(int(9.8) == 10)

print('-----------------------')
# Viết đoạn code, nhập số giờ làm, lương mỗi giờ -> tính lương người đó
_hours = float(input('Nhập số giờ làm:'))
_rate_per_hour = float(input('Nhập lương mỗi giờ: '))
_salary = _hours * _rate_per_hour
print('Tổng lương: ', _salary)

print('-----------------------')
# Nhập vào số năm -> tính ra thời gian bằng giây
total_year = int(input('Nhập số năm: '))
total_section = int(total_year * 365 * 24 * 60 * 60)
print(total_year, 'năm = ', total_section, 'giây')

print('-----------------------')
# In ra 1 bảng giá trị
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')