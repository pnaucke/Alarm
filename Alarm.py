print('Hoeveel keer moet het alarm afgaan?')
z = input()

if int(z) > 0:
    for x in range(1, int(z)+1):
        print(f"Alarm {x} !")
else:
  raise Exception("Sorry, Geen getal lager dan 1") 