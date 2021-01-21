import csv
import pandas as pd

class player:

    def hpchange(self ,hp):
       chhp = int(input("\nEnter the amount by which to change HP: "))
       return hp + chhp

    def xpchange(self,xp):
       chxp = int(input("\nEnter the amount by which to change XP: "))
       return xp + chxp   
    def stats(self,id , hp , xp , class1):
        if(hp > 100):
            hp = 100
        print("Player Info :\n\nId : " + id + "\nHP : " + str(hp) + "\nXP : " + str(xp) + "\nClass : " + class1 + "\n\n") 
df = pd.read_csv('filename.csv')
cols = df['Id']
hp1 = df['HP']
class2 = df['Class']
xp1  = df['XP']
lent = len(cols)

with open('filename.csv','r') as file1:


    reader1 = csv.DictReader(file1)
    file1.close()    
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

            num1 = int(input("Please choose a class\n1.\tWarrior\n2.\tArcher\n3.\tMege\n\n"))
            test = 0  
            if(num1 == 1):
                class1 = "Warrior" 
                for  i in range(lent):
                    if(cols[i] == id1):
                        test+=1
                        hp = hp1[i]
                        xp = xp1[i]
                        test = i
                        class1 = class2[i]
                        print("\n\nSorry If you choose wrong class but your class has been taken\n")  
                while(1): 
                    
                    num2 = int(input("\n\n1.\tChange HP\n2.\tChange XP\n3.\tGet current stats\n4.\tExit\n\n"))
                    if(num2 == 1):
                      hp = player().hpchange(hp)
                      
                      continue    
                    elif(num2 == 2):
                      xp = player().xpchange(xp)
                      
                      continue
                    elif(num2 == 3):
                      player().stats(id1,hp,xp,class1)

                      continue
                    elif(num2 == 4):
                      if(test != 0):
                        write1.writerow({id1,hp,xp,class1})
                      else:  
                        write1.writerow({'Id':id1,'HP':hp,'XP':xp,'Class':class1})
                        break               
                    

                        

                    
            elif(num1 == 2):
                class1 = "Archer" 
                for  i in range(lent):
                    if(cols[i] == id1):
                        hp = hp1[i]
                        xp = xp1[i]
                        class1 = class2[i]
                        print("\n\nSorry If you choose wrong class but your class has been taken\n")
                while(2): 
                    num2 = int(input("\n\n1.\tChange HP\n2.\tChange XP\n3.\tGet current stats\n4.\tExit\n\n"))
                    if(num2 == 1):
                      hp = player().hpchange(hp)
                      
                      continue    
                    elif(num2 == 2):
                      xp = player().xpchange(xp)
                      
                      continue
                    elif(num2 == 3):
                      player().stats(id1,hp,xp,class1)
                      continue
                    elif(num2 == 4):
                      if(test != 0):
                        write1.writerow({id1,hp,xp,class1})
                      else:  
                        write1.writerow({'Id':id1,'HP':hp,'XP':xp,'Class':class1})               
                        break
                  

            elif(num1 == 3):
                class1 = "Mege" 
                for  i in range(lent):
                    if(cols[i] == id1):
                        hp = hp1[i]
                        xp = xp1[i]
                        class1 = class2[i]
                        print("\n\nSorry If you choose wrong class but your class has been taken\n")  
                while(1): 
                    num2 = int(input("\n\n1.\tChange HP\n2.\tChange XP\n3.\tGet current stats\n4.\tExit\n\n"))
                    if(num2 == 1):
                      hp = player().hpchange(hp)
                     
                      continue    
                    elif(num2 == 2):
                      xp = player().xpchange(xp)
                     
                      continue
                    elif(num2 == 3):
                      player().stats(id1,hp,xp,class1)
                      continue
                    elif(num2 == 4):
                      if(test != 0):
                        write1.writerow({id1,hp,xp,class1})
                      else:  
                        write1.writerow({'Id':id1,'HP':hp,'XP':xp,'Class':class1})              
                        break
                    

            