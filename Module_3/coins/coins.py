# name of student: joel
# number of student: 
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #

if change > 0: #
  coinValue = 500 #
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #
    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, 'cents' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +   'cents did you return? '))
      change -= nrCoinsReturned * coinValue #

# comment on code below: 
    if coinValue == 500:
      coinValue = 200
      nrCoinsReturned500 = nrCoinsReturned
    elif coinValue == 200:
      coinValue = 100  
      nrCoinsReturned200 = nrCoinsReturned
    elif coinValue == 100:
      coinValue = 50
      nrCoinsReturned100 = nrCoinsReturned
    elif coinValue == 50:
      coinValue = 20
      nrCoinsReturned50 = nrCoinsReturned
    elif coinValue == 20:
      coinValue = 10
      nrCoinsReturned20 = nrCoinsReturned
    elif coinValue == 10:
      coinValue = 5
      nrCoinsReturned10 = nrCoinsReturned
    elif coinValue == 5:
      coinValue = 2
      nrCoinsReturned5 = nrCoinsReturned
    elif coinValue == 2:
      coinValue = 1
      nrCoinsReturned2 = nrCoinsReturned
    else:
      coinValue = 0
      nrCoinsReturned1 = nrCoinsReturned

if change > 0: #
  print('Change not returned: ', str(change) + "cents")
else:
  print('done')
  print(nrCoinsReturned500,"x 500 cents",nrCoinsReturned200,"x 200 cents",nrCoinsReturned100,"x 100 cents",nrCoinsReturned50,"x 50 cents",nrCoinsReturned20,"x 20 cents",nrCoinsReturned10,"x 10 cents",nrCoinsReturned5,"x 5 cents",nrCoinsReturned2,"x 2 cents",nrCoinsReturned1,"x 1 cent" )