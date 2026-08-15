owened = []
wishlist = []




owened.append(input ("enter the name of a book you own: ").capitalize())

second = input("Enter the name of another book you own, or press enter to skip: ").capitalize()

if second :
  owened.append(second)

print (f"your library: {owened}")




wishlist.append(input ("enter name of book you wish to have in the future: ").capitalize())

second_2 = input("Enter the name of another book you wish to have (or press 'Enter' to skip): ").capitalize()

if second_2 :
  wishlist.append(second_2)

print (f"your wishlist: {wishlist}")




third = input("Enter the name of a book from your wishlist that you have acquired (or press 'Enter' to skip): ").capitalize()

if third in wishlist :
  wishlist.remove(third)
  owened.append(third)

  print (f"""Updated Library: {owened} 
  Updated Wishlist: {wishlist}""")




forth = input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip): ").capitalize()

if forth in owened :
  owened.remove(forth)
  print(f"Final Library after Donation: {owened}")