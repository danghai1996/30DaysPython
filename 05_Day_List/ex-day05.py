# 1 + 2 + 3 +4
list_test = list()
list_test = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print('Độ dài danh sách list_test:', len(list_test))
print('Phần tử đầu:', list_test[0])
print('Phần tử giữa:', list_test[len(list_test) // 2])
print('Phần tử cuối:', list_test[len(list_test) - 1])

# 5
info = ['Hai', 24, 'Vietnam', 'Ha Noi']

# 6 
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7
print('Danh sách info:', info)
print('Danh sách IP Companies:', it_companies)

# 8
print('Số công ty: ', len(it_companies))

# 9
print('Công ty đầu:', it_companies[0])
print('Công ty giữa:', it_companies[len(it_companies) // 2])
print('Công ty cuối:', it_companies[len(it_companies) - 1])

# 10
it_companies[2] = 'HaiCompany'
print('Danh sách công ty sau khi sửa:', it_companies)

# 11
it_companies.append('Microsoft')
print('Danh sách công ty sau khi thêm:', it_companies)

# 12
it_companies.insert(len(it_companies) - 1, 'NhemCompany')
print('Danh sách công ty sau khi thêm:', it_companies)

# 13
it_companies[1] = it_companies[1].upper()
print('Danh sách công ty sau khi sửa:', it_companies)

# 14
companies = '#;'.join(it_companies)
print(companies)

# 15
print('NhanHoa' in it_companies)

# 16
it_companies.sort()
print('Danh sách công ty sau khi sắp xếp:', it_companies)

# 17
it_companies.reverse()
print('Danh sách công ty sau khi đảo ngược:', it_companies)

# 18
it_companies1 = it_companies[3:]
print('Danh sách công ty sau khi cắt 3 công ty đầu:', it_companies1)

# 19
it_companies2 = it_companies[0:len(it_companies) - 3]
print('Danh sách công ty sau khi cắt 3 công ty cuối:', it_companies2)

# 21 + 22 + 23 + 24 + 25
it_companies.pop(0)
print('Danh sách công ty sau khi bỏ công ty đầu:', it_companies)

it_companies.pop(len(it_companies) - 1)
print('Danh sách công ty sau khi bỏ công ty cuối:', it_companies)

it_companies.pop(len(it_companies) // 2)
print('Danh sách công ty sau khi bỏ công ty giữa:', it_companies)

it_companies.clear()
print('Danh sách công ty sau khi clear:', it_companies)

del it_companies

# 26 + 27
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
tech_list = front_end + back_end
print('Sau khi ghép: ', tech_list)
full_stack = tech_list.copy()
print('Full stack: ', full_stack)
index_redux = full_stack.index('Redux')
print('Vị trí Redux: ', index_redux)
full_stack.insert(index_redux + 1, 'Python')
full_stack.insert(index_redux + 2, 'SQL')
print('Full stack sau khi thêm: ', full_stack)
