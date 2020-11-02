#choose full or knee
while True:
  try:
    choice = input('Are you measuring FULL or KNEE height?\n')
    if choice=='FULL' or choice == 'KNEE' or choice == 'Full' or choice == 'Knee' or choice == 'full' or choice == 'knee':
      print('Choice understood')
      break;
    else:
      print ('Unrecognised input, please type FULL or KNEE')
  except:
    continue
print('You are measuring %s height' % choice )

#enter distance from person
while True:
  try:
    distance = float(input('Please enter the distance between you and patient in metres:'))
  except ValueError:
    print("That's not a number")
    continue
  else:
    break



#define full as 1 and knee as 2
if choice=='FULL' or choice == 'Full' or choice == 'full':
 x = 1
elif choice=='KNEE' or choice == 'Knee' or choice == 'knee':
 x= 3

#Calculations
if x<2: #full

  while True: # Full height
    try:
      UpAngle = float(input('Please enter the angle to TOP OF HEAD in degrees: '))
      LowerAngle = float(input('Please enter the angle to FEET in degrees: '))
    except ValueError:
        print("Sorry, that's not a number")
        continue
    else:
      print('Angles successfully entered')
      
      break;

elif x>2: #knees

  while True: #Knee height
    try:
      UpAngle = float(input('Please enter the angle to TOP OF KNEE in degrees: '))
      LowerAngle = float(input('Please enter the angle to FEET in degrees: '))
    except ValueError:
        print("Sorry, that's not a number")
        continue
    else:
      print('Angles successfully entered')
      break;



