row_1 = ['!', '!', '!']
row_2 = ['!', '!', '!']
row_3 = ['!', '!', '!']


print(f"were should the rabbit go '*'\n\n{row_1}\n{row_2}\n{row_3}\n")


place = list(input("please enter the row and the column in numbers: "))




if place[0] == "1":
  row_1[int(place[1])-1] = '*'

elif place[0] == "2":
  row_2[int(place[1])-1] = '*'

elif place[0] == "3":
  row_3[int(place[1])-1] = '*'
 
else :
  print ('invalid number')



print(f'{row_1}\n{row_2}\n{row_3}')
