import csv
def stats(id , hp , xp , class1):

    if(hp > 100):
        hp = 100
    print("Player Info :\n\nId : " + id + "\nHP : " + str(hp) + "\nXP : " + str(xp) + "\nClass : " + class1 + "\n\n" )

def hpchange(hp):
    chhp = int(input("\nEnter the amount by which to change HP: "))
    return hp + chhp

def xpchange(xp):
    chxp = int(input("\nEnter the amount by which to change XP: "))
    return xp + chxp

with open('filename.csv','r') as file1:

    reader1 = csv.DictReader(file1)

    with open('finalplayer.csv','w') as file2:
        fieldvalue = ['Id','HP','XP','Class']

        write1 = csv.DictWriter(file2, fieldnames=fieldvalue, delimiter=',')

        write1.writeheader()

        for line in reader1:
            write1.writerow(line)
    while(1):
        
        
        
        
        
        id1 = input("\n\nEntre ID: ") 
        
        hp =100
        xp = 0 
        write1.writerow({'Id':id1,'HP':hp,'XP':xp})
        num1 = int(input("Please choose a class\n1.\tWarrior\n2.\tArcher\n3.\tMege\n\n"))

        if(num1 == 1):
            class1 = "Warrior"   
            while(1): 
                num2 = int(input("\n1.\tChange HP\n2.\tChange XP\n3.\tGet current stats\n4.\tExit\n\n"))
                if(num2 == 1):
                   hp = hpchange(hp)
                   write1.writerow({'Id':id1,'HP':hp,'XP':xp})
                   continue    
                elif(num2 == 2):
                   xp = xpchange(xp)
                   write1.writerow({'Id':id1,'HP':hp,'XP':xp})
                   continue
                elif(num2 == 3):
                   stats(id1,hp,xp,class1)
                   continue
                elif(num2 == 4):
                    break
                
        elif(num1 == 2):
            class1 = "Archer"   
            while(1): 
                num2 = int(input("\n1.\tChange HP\n2.\tChange XP\n3.\tGet current stats\n4.\tExit\n\n"))
                if(num2 == 1):
                   hp = hpchange(hp)
                   write1.writerow({'Id':id1,'HP':hp,'XP':xp})
                   continue    
                elif(num2 == 2):
                   xp = xpchange(xp)
                   write1.writerow({'Id':id1,'HP':hp,'XP':xp})
                   continue
                elif(num2 == 3):
                   stats(id1,hp,xp,class1)
                   continue
                elif(num2 == 4):
                    break

                

        elif(num1 == 3):
            class1 = "Mege"   
            while(1): 
                num2 = int(input("\n1.\tChange HP\n2.\tChange XP\n3.\tGet current stats\n4.\tExit\n\n"))
                if(num2 == 1):
                   hp = hpchange(hp)
                   write1.writerow({'Id':id1,'HP':hp,'XP':xp})
                   continue    
                elif(num2 == 2):
                   xp = xpchange(xp)
                   write1.writerow({'Id':id1,'HP':hp,'XP':xp})
                   continue
                elif(num2 == 3):
                   stats(id1,hp,xp,class1)
                   continue
                elif(num2 == 4):
                    break

    