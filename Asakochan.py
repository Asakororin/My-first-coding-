guests =['John','Jack','Jason','Jamie']

print('This is my first list')
print(guests)
print(f"Sadly,{guests[3]}is sick")
del guests[3]
print('this is my new list')
print(guests)
new_guests= 'Taro'
guests.append(new_guests)
print(guests)
print('Taro is so cute')
guests.insert(1,new_guests)
print(guests)
new_table =[]
print(new_table)
new_guests = guests.pop(3)
print(new_table)
print(f"I know you are being invited {guests[1]},and {guests[2]}")
new_table.append(new_guests)
print(new_table)
