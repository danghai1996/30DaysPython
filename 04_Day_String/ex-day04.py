# 1. Nối chuỗi: "30", "Days", "of", "Python"
print('30 ' + 'Days ' + 'of ' + 'Python ')

# 2. Nối chuỗi: 'Coding', 'For' , 'All' thành 'Coding For All'
print('Coding ' + 'For ' + 'All')

# 3 + 4 + 5 + 6 +7 + 8 + 9 + 10 +11 + 12 + 13
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:7])
print(company.find('Coding'))
print(company.replace('Coding', 'Python'))
company_2 = 'Python for Everyone'
print(company_2.replace('Python for Everyone', 'Python for All'))
print(company.split(' '))

# 14. Tách chuỗi `Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon` ngăn cách bằng dấu phẩy `,`
_string1 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(_string1.split(', '))

# 15. Tìm ký tự tại index = 0 trong biến `company`
print(company[0])

# 16.Chỉ số cuối cùng của chuỗi `Coding For All`
print(len('Coding For All') - 1)

# 17. Ký tự nào ở index = 10 trong biến `company`
print(company[10])

# 20. Xác định vị trí đầu tiên của chữ `C` trong chuỗi `Coding For All`
print(company.index('C'))

# 21. Xác định vị trí đầu tiên của chữ `F` trong chuỗi `Coding For All`
print(company.index('F'))

# 22. Sử dụng `rfind` để xác định vị trí của lần xuất hiện cuối cùng của `l` trong `Coding For All People`
print('Coding For All People'.rfind('l'))

# 23. Sử dụng `find()` hoặc `index()` để tìm vị trí xuất hiện đầu tiên của từ `because` trong câu sau: `You cannot end a sentence with because because because is a conjunction`
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# 24. Sử dụng `rindex()` để tìm vị trí xuất hiện cuối cùng của từ `because` trong câu sau: `You cannot end a sentence with because because because is a conjunction`
print(sentence.rindex('because'))

# 25. Cắt bỏ cụm từ `because because because` trong câu: `You cannot end a sentence with because because because is a conjunction`
print(sentence.replace(' because because because',''))

# 26. Tìm vị trí xuất hiện đầu tiên của `because` trong câu: `You cannot end a sentence with because because because is a conjunction`
print(sentence.find('because'))

# 28. Kiểm tra `Coding For All` có bắt đầu bằng `Coding` không?
print(company.startswith('Coding'))

# 29. Kiểm tra `Coding For All` có kết thúc bằng `coding` không?
print(company.endswith('coding'))

# 30. `   Coding For All      `. Hãy xóa các khoảng trắng bên trái và bên phải của chuỗi
s1 = '   Coding For All      '
print(s1.strip(' '))

# 31. Biến nào sau đây trả về True khi ta sử dụng `isidentifier()`
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32. Danh sách sau có tên của 1 số thư viện Python `['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']`. Ghép chúng thành chuỗi, phân cách bằng dấu cách
list_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(list_lib))

# 33
print('I am enjoying this challenge. \nI just wonder what is next.')

# 34
print('Name\tAge\tCountry\nAsabeneh\t250\tFinland'.expandtabs(10))

# 35
radius = 10
area = 3.14 * radius ** 2
print('The area of a cricle with radius {} is {:.2f} meters square.'.format(radius, area))

# 36
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))