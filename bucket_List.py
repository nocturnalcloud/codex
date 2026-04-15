# Write code below 💖
choice = 0
bucket_list = []

print('                          ')


while choice != 3:
  print('                       ')
  print('=====================================')
  print('           Bucket List 2026          ')
  print('=====================================')
  print('                       ')
  for i in range(len(bucket_list)):
    print(f'{i + 1}) {bucket_list[i]}')
  print('                                      ')
  print('[1]add [2]delete [3]exit')
  print('---------------------------------------')
  print('                                       ')
  choice = int(input('What would you like todo? '))
  print('                                        ')
  if choice == 1:
    todo = ''
    print('"Type q to quit and go back to main menu"')
    print('                          ')
    while todo != 'q':
      todo = input('Add to your bucket list: ')
      print('                                 ')
      if todo == 'q':
        break
      else:
        bucket_list.append(todo)
  elif choice == 2:
    todo = int(input('Type the number you would like to check off your list: '))
    bucket_list.pop(todo - 1)
print('                                 ')
print('Thank you for using Bucket List. Bye for now:)')
print('                                              ')

print('                       ')
print('=====================================')
print('           Bucket List 2026          ')
print('=====================================')
print('                       ')
for i in range(len(bucket_list)):
  print(f'{i + 1}) {bucket_list[i]}')
print('                                      ')

