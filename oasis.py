import sys

class Anti_soft_Drink():
    
    print("This is a console program that predicts when a user will be diabetic.")
    ## Creating a space for the user to input his or her details ##
    name = raw_input("Please enter your full name: ")
    
    print("Welcome " + name + ", this is a basic Python program that predicts when u are liable to be diabetic.")
    
    
    def gettimes():
        '''Get the number of times softdrinks have been taken'''
        number = int(input("Please enter the number of times you take soft drinks in a week: "))
        
        if 21 <= soft_num <= 30:
                print "Stop taking soft drinks or you will have yourself to blame once you are diagnosed with diabetes"
                
        elif 11 <= soft_num <= 20:
                print "You have to reduce it to less than 5 in a week or you will be diabetic in not less than 5 years"
                
        elif 3 <= soft_num <= 10:
                print "Please Reduce your intake of soft drinks or in 15 yrs you will be diabetic"
        elif 1<= soft_num < 3:
                print("You are safe from diabetes")
    
    gettimes()
                

    print("Thanks {}, for taking my Anti-Soft drink advice.").format(name)


raw_input("Press <enter> to exit ")

## Send me your emails for more raindolf@oasiswebsoft.com ##
## Kindly add us on fb www.fb.com/oasisweb ##
