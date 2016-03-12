import model
import view


def main(view): 
  while(True): 
	createMenu()
	point = input()
	if(point == 1):
		calculate_calories(readGender, readWeigh, readHeight, readAge, readPA)
	else(point == 2):
		break
	else
		print("Wrong input! Try again")


main()		
		