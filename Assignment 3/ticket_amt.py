# 11. Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition:
#Children below 1230% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

age1 = int(input('Enter age of peson:'))
amt1 = int(input('Enter ticket amount:'))

if(age1 < 12):
    amt1 = amt1 * 0.70
elif(age1 > 59):
    amt1 = amt1 * 0.50

age2 = int(input('Enter age of peson:'))
amt2 = int(input('Enter ticket amount:'))

if(age2 < 12):
    amt2 = amt2 * 0.70
elif(age2 > 59):
    amt2 = amt2 * 0.50

age3 = int(input('Enter age of peson:'))
amt3 = int(input('Enter ticket amount:'))   

if(age3 < 12):
    amt3 = amt1 * 0.70
elif(age3 > 59):
    amt3 = amt1 * 0.50

age4 = int(input('Enter age of peson:'))
amt4 = int(input('Enter ticket amount:'))   

if(age4 < 12):
    amt4 = amt1 * 0.70
elif(age4 > 59):
    amt4 = amt1 * 0.50

age5 = int(input('Enter age of peson:'))
amt5 = int(input('Enter ticket amount:'))   

if(age5 < 12):
    amt5 = amt1 * 0.70
elif(age5 > 59):
    amt5 = amt1 * 0.50

total = amt1 + amt2 + amt3 + amt4 + amt5

print(f"Total Ticket Amount :{total}.")
