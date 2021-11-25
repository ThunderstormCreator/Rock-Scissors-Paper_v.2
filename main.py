import random
another_game= True
while another_game:
  robot= random.randint (1,3)
  human= input ("Enter 1 for rock, 2 for sissors, 3 for paper:  ")

  flag = True
  while flag:
    try:
      human = int (human)
    except:
      human=0
      print ("Please use digitals only")
    if human != 0:
      flag = False
      

  flag1 = True
  while flag1:
    if int(human) == 1:
      print ("You've chosen rock and my choice is...")
      flag1=False
    elif int(human) == 2:
      print ("You've chosen sissors and my choice is...")
      flag1=False
    elif int(human) == 3:
      print ("You've chosen paper and my choice is...")
      flag1=False
    else:
      input ("Type 1 or 2 or 3: ")
      
   
    
  if robot ==1:
    print ("Rock!")
  if robot ==3:
    print ("Paper!")
  if robot ==2:
    print ("Sissors")

  if robot == int (human):
    print ("Draw")
  elif robot ==1 and int(human)==2:
    print ("You lost!")
  elif robot ==2 and int(human)==3:
    print ("You lost")
  elif robot ==3 and int(human)==1:
    print ("You lost...")
  else:
    print("You won!!!!")
  print ("")
  replay= input ("Would you like to play again? y/n: ")
  if replay == "n":
    another_game = False


