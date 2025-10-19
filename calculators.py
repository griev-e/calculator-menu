while True:
    print()
    print(" - Calculator Menu - ")
    print()
    print(" 1 - Dividend Yield ")
    print(" 2 - Income ")
    print(" 3 - Compound Interest ")
    print()
    print(" 4 - Exit ")
    print()

    choice = input("Select an option (1 - 4): ")

    if choice == "1":
        print()
        print(" - Starting Dividend Yield Calculator! - ")
        # starts loop
        while True:
            
            # asks user for account balance
            print()
            balance = input("Account total?: ") 

            # asks user for their estimated dividend income in dollars
            print()
            yield_ = input("Estimated annual dividend income?: ")

            # calculates yield percentage
            yieldpercent = (float(yield_)/float(balance)) * 100
    
            # adds percent sign and rounds to nearest hundreth
            yieldpercentage = str(round(yieldpercent, 2)) + "%"

            # confirms the user's input
            print()
            print(f"Account Total: ${balance}")
            print(f"Estimated Dividend Income: ${yield_}")

            # asks user to confirm
            print()
            answer = input("Is this correct? Y/N to confirm. ")
    
            # if confirmed yes, prints dividend yield
            if answer == "Y" or answer == "y" or answer == "yes" or answer == "Yes":
                print()
                print()
                print(f"Your estimated dividend yield is {yieldpercentage}")
                print()
                print()

                choice2 = input("'1' to return to Calculator Menu\n'2' to Exit\n\nInput: ")
                if choice2 == "1":
                # breaks loop
                    break
                elif choice2 == "2":
                    print()
                    print("Thank you for using the Calculator Menu!")
                    print()
                    exit()
            # if confirmed no, loop
            else:
                print()
                print("Try again. Reinput values. ")
            
    elif choice == "2":
        print()
        print(" - Starting Income Calculator! - ")
        # starts loop
        while True:
            # asks for stock price / total account value
            print()
            stockprice = input("Stock price (per share) or Total Account Value: ")
            # asks for dividend yield
            print()
            divyield = input("Dividend Yield Percentage: ")
            # asks for total shares
            print()
            totalshares = input("(If using Total Account Value, type 1) \nNumber of shares: ")


            # calculations

            # calculates annual dividend
            annualdividend = (float(stockprice) * float(divyield)) / 100
            # applies to total number of shares
            totaldivincome = float(annualdividend) * float(totalshares)
            monthlydividend = float(annualdividend) / 12
 
        # confirms the user's input
            print()
            print(f"Stock price/Account Total: ${stockprice}")
            print(f"Dividend Yield Percentage: {divyield}%")

            # output
            print()
            answer1 = input("Is this correct? Y/N to confirm. ")
    
            # if confirmed yes, prints income
            if answer1 == "Y" or answer1 == "y" or answer1 == "yes" or answer1 == "Yes":
                print()
                print()
                print(f"Annual Dividend Income = ${round(totaldivincome, 2)} \nMonthly Dividend Income = ${round(monthlydividend, 2)}")
                print()
                print()
                
                choice2 = input("'1' to return to Calculator Menu\n'2' to Exit\n\nInput: ")
                if choice2 == "1":
                # breaks loop
                    break
                elif choice2 == "2":
                    print()
                    print("Thank you for using the Calculator Menu!")
                    print()
                    exit()
            else:
                # if confirmed no, loops back
                print()
                print("Try again. Reinput values. ")
    
    elif choice == "3":
        print()
        print(" - Starting Compound Interest Calculator - ")
        # starts loop
        while True:
            # asks user for values
            print()
            principal = input("Starting Principal: ")

            print()
            rate = input("Estimated Interest Rate Percentage: ")

            print()
            time = input("Time (in Years): ")

            print()
            compfreq = input("Compounding Frequency:\n'1' - Yearly\n'4' - Quarterly\n'12' - Monthly\n'365' - Daily\n\nInput: ")
            
            # calculations
            decimalrate = round(float(rate), 2) / 100

            finalvalue = float(principal) * (1 + float(decimalrate) / float(compfreq)) ** (float(compfreq) * float(time))

            print()
            print(f"Starting Principal: ${principal}")
            print(f"Estimated Interest Rate: {rate}%")
            print(f"Years: {time}")
            print(f"Compounding Frequency: {compfreq}")
            print()
            answer = input("Is this correct? Y/N to confirm: ")

            if answer == "Y" or answer == "y" or answer == "yes" or answer == "Yes":
                print()
                print()
                print(f"Your future principal value is ${round(finalvalue, 2)}. ")
                print()
                print()

                choice2 = input("'1' to return to Calculator Menu\n'2' to Exit\n\nInput: ")
                if choice2 == "1":
                # breaks loop
                    break
            elif choice2 == "2":
                    print()
                    print("Thank you for using the Calculator Menu!")
                    print()
                    exit()
            else:
            # if confirmed no, loops back
                print()
                print("Try again. Reinput values. ")
                
            

    elif choice == "4":
        print()
        print ("Thank you for using the Calculator Menu!")
        print()
        break
    else:
        print()
        print("Invalid option. Please choose 1, 2 3, or 4. ")
