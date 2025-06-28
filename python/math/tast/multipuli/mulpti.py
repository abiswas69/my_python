info="enter a number 2 into 2 like 22*28 and last two degit pule = 10 like 2+8=10"
print(f"{info}  ")
user_input = input("Enter your text (e.g., 22*28): ").strip()

# Check if input contains exactly one *
if '*' not in user_input:
    print("No asterisk (*) found in the text")
else:
    # Split into parts around *
    parts = user_input.split('*')
    
    if len(parts) != 2:
        print("Invalid format: should be exactly two numbers with * between them")
    else:
        num1, num2 = parts[0], parts[1]
        
        # Check if both parts are numbers
        if not (num1.isdigit() and num2.isdigit()):
            print("Both parts should be numbers")
        else:
            # Get last digits
            last1 = int(num1[-1])
            last2 = int(num2[-1])
            
            # Check if sum is 10
            if last1 + last2 == 10:
                print(f"Valid: {num1}*{num2} (last digits {last1}+{last2}=10)")
            else:
                print(f"Invalid: {num1}*{num2} (last digits {last1}+{last2}≠10)")