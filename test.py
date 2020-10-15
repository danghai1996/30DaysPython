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