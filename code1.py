gameminecraft = ('''                _   

               .__                                  __                   .__                                   _____  __   
__  _  __ ____ |  |   ____  ____   _____   ____   _/  |_  ____     _____ |__| ____   ____   ________________ _/ ____\/  |_ 
\ \/ \/ // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \   /     \|  |/    \_/ __ \_/ ___\_  __ \__  \\   __\\   __\
 \     /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> ) |  Y Y  \  |   |  \  ___/\  \___|  | \// __ \|  |   |  |  
  \/\_/  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/  |__|_|  /__|___|  /\___  >\___  >__|  (____  /__|   |__|  
             \/          \/            \/     \/                       \/        \/     \/     \/           \/             
''')

print(gameminecraft)

welcomescreenminecraft = 'here we are, in the world of Minecraft'
print(welcomescreenminecraft)



play_input = input('type play to play and exit to exit the application')
if play_input == 'play':
    print("okay, let's play (status: active)")
else:
    print('exiting the application')
    niceonechooseme = input ('do you choose to go down the basement or not? Type Y or N ')
    if niceonechooseme == 'Y':
        print('You got killed by a creeper')
        if niceonechooseme == 'N':
            print('Yay you can continue')
eattime = input("hey,your low on food.You might die if you don't eat soon.(type eat to eat and wait to wait for your friend to give you food")
if eattime == 'eat':
    print("Yay! you're still alive!")
    if eattime == 'wait':
        print("Oh no! you're friend has come too late! You died beacause of hunger ")
yes = input ("I think it is dinner time. But we don't have enough time to hunt all the food beacause of the the outside mobs(type wait to wait for morning or type eat to eat raw food which doesnt taste good ")
if yes == 'wait':
    print('You had less food points,now you died')
    if yes == 'eat':
        print("You are alive beacause you ate ")
        seevillage = input("Hey,there's a village.do you want to go there or not? Type Y or N")
        if seevillage == 'Y':
            tradevillager = input('Do you want to trade?. Type Y or N')
            if tradevillager == 'Y':
                print('You have traded with a villager and you are alive')
                if tradevillager == 'N':
                    print('You are dead beacause you did not have any food and needed to trade')
