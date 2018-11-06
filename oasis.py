import sys

class Anti_soft_Drink:
    
    
    def blank():
        print('')
        print('')
        
        
    blank()
    print("This is a console program that predicts when a user will be diabetic.")
    blank()
    query = "Please enter your full name:"
    name = raw_input(query)
    print("Welcome  {}, this is a basic Python program that predicts when u are liable to be diabetic.".format(name))
    blank()
    query = "Please enter the number of times you take soft drinks in a week: "
    number = int(input(query))
        
        
    if 21 <= number <= 30:
            print("Stop taking soft drinks or you will have yourself to blame once you are diagnosed with diabetes")
    elif 11 <= number <= 20:
            print("You have to reduce it to less than 5 in a week or you will be diabetic in not less than 5 years")
    elif 3 <= number <= 10:
            print("Please Reduce your intake of soft drinks or in 15 yrs you will be diabetic")
    elif 1<= number < 3:
            print("You are safe from diabetes")
            
    blank()
    print("Thanks {} , for taking my Anti-Soft drink advice.".format(name))

## Send me your emails for more raindolf@oasiswebsoft.com ##
## Kindly add us on fb www.fb.com/oasisweb ##
