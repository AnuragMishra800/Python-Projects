while(True): 
    def checker(email):
        if(len(email) < 11):
            print("Email Must Be 11 Characters Long.")
            return "Invalid Email."
        for char in email:
            if char.istitle():
                print("No Capital Words Are Allowed In The Email.")  
                return "Invalid Email." 
        # if any(char.isdigit() for char in email):
        #     print("No Digits Allowed.")
        #     return "Invalid Email." 
        if email[0].isdigit():
            print("No Digits Are Allowed In The Start Of The Email.")
            return "Invalid Email."
        if not email.endswith('@gmail.com'):
            print("Your Email Must Contain @gmail.com In The End.") 
            return "Invalid Email."
        if email.count('@') != 1:
            print("Only One @ Is Allowed In The Whole Email.")
            return "Invalid Email."
        local_part, domain_part = email.split('@gmail.')  
        if not local_part.isalnum() or not domain_part.isalnum():
            print("No Special Characters Are Allowed In The Email Besides The @ For Only Once.") 
            return "Invalid Email."
        else:
            print("Congratulations! You Entered The Right Email.")
            return "Valid Email."

    email = input("Enter Your Email: ") 
    result = checker(email) 
    print(result)  