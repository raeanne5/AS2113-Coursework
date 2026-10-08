# Policyholder Management Functions ------------------------------------------------------------------------------------------------------------------
# Function to read policyholders from csv and returns as a list of dictionaries
def read_policyholders(policy_filename): #dictionary for each policyholder
    policyholders = []  #empty list to store policyholder data
    with open(policy_filename, "r") as file:  #open the specified file for reading (policyholders.csv)
        for line in file:  #for each line in the file
            row = line.strip().split(',')  #split into a list of values
            policyholders.append(row)  #append to the policyholders list
    return policyholders #return list

# Function to save policyholders into csv formatted file
def save_to_csv(policyholders, policy_filename): 
    filename = input("Enter the filename to save the data (e.g., 'policyholders1.csv'): ")  #get desired filename from user
    if not filename.lower().endswith('.csv'):  #check if filename ends with .csv
        filename += '.csv'  #append .csv if not there
    with open(filename, 'w', newline='') as file:  #open specified file (policyholders) for writing
        for policyholder in policyholders:  #loop through each policyholder in  list
            file.write(','.join(policyholder) + '\n')  #write policyholder data as comma-separated string, go to a new line
    print("Data saved to " + filename + " successfully.")  #notify user that data has been saved
    #return to main menu after saving

# Function to display Policyholders Data
def display_policyholder_details(policyholder_data):
    print("\nPolicyholder Details")
    print("Policy Number:", policyholder_data[0])  #print policy number (first element in list)
    print("Policyholder Name:", policyholder_data[1] + " " + policyholder_data[2])  #print name in full (first name + surname)
    print("Age:", policyholder_data[3])  #print age
    print("Gender:", policyholder_data[4])  #print gender
    print("Area:", policyholder_data[5], "\n")  #print  area             

# Function to add new policyholder with validation for input
def add_policyholder(policyholders, policy_filename):
    while True:
        # Policy number #
        policy_number = input("Enter new policy number (e.g., P1234567): ") #get policy number input 
        if not policy_number.strip(): #cannot be empty or whitespace
            print("Policy number cannot be empty.")
            continue
        #check if the policy number is entered in correct format (starts with 'P', followed by 7 digits)
        if len(policy_number) == 8 and policy_number[0] == 'P' and policy_number[1:].isdigit():
            # length = 8, starts with 'P', second character onwards are all in digits
            if any(policyholder[0] == policy_number for policyholder in policyholders): #check if policy number entered is unique 
                print("Policy number " + policy_number + " already exists. Please enter a *unique* policy number.\n")
                continue
        else:
            print("Invalid policy number format. Please enter a valid policy number.")
            continue
        # First name #
        while True:
            first_name = input("Enter first name: ")
            if first_name.strip() and all(char.isalpha() or char.isspace() for char in first_name):
            #check if not empty, alphabetical (allow names with spaces)
                first_name = ' '.join(part.capitalize() for part in first_name.split())
                #capitalise only first letter (for each part eg. Ruby Jane)
                break
            else:
                print("First name cannot be empty and must consist of alphabets only.")       
        # Surname #
        while True:
            surname = input("Enter surname: ")
            if surname.strip() and all(char.isalpha() or char.isspace() for char in surname):
            #check if not empty, alphabetical (allow names with spaces)
                surname = ' '.join(part.capitalize() for part in surname.split())
                #capitalise only first letter (for each part eg. Ruby Jane)
                break
            else:
                print("Surname name cannot be empty and must consist of alphabets only.")
        # Age #
        while True:
            age = input("Enter age category: 'Young' (below 30) or 'Old' (30 and above): ").lower()
            if age in ['young', 'old']:
                age = age.capitalize()
                break
            else:
                print("Invalid age category. Please enter 'Young' or 'Old'.\n")      
        # Gender #
        while True:
            gender = input("Enter gender ('male' or 'female'): ").lower()
            if gender in ['male', 'female']:
                gender = gender.capitalize()
                break
            else:
                print("Invalid gender. Please enter 'Male' or 'Female'.\n")
        # Area #
        while True:
            area = input("Enter area ('North', 'Central' or 'South'): ").lower()
            if area in ['north', 'central', 'south']:
                area = area.capitalize()
                break
            else:
                print("Invalid area. Please enter 'North', 'Central', or 'South'.\n")
        
        print("\nSummary of Policyholder Input:")
        print("Policy Number: " + policy_number)
        print("First Name: " + first_name)
        print("Surname: " + surname)
        print("Age: " + age)
        print("Gender: " + gender)
        print("Area: " + area)

        while True:
            save_confirmation = input("Do you want to save this policyholder? ('yes' or 'no'): ").lower()
            if save_confirmation in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.\n")

        if save_confirmation == 'yes':
            new_policyholder = [policy_number, first_name, surname, age, gender, area] #new list for the new policyholder
            policyholders.append(new_policyholder)  #add the new policyholder's list to (original) policyholders list
            with open(policy_filename, 'a') as file: #save the new policyholder to '001 Policyholder.txt'
                file.write(','.join(new_policyholder) + '\n')
            print("Policyholder added successfully.\n")
        else:
            print("Policyholder not saved.\n")

        while True:
            add_choice = input("Do you want to add another policyholder? ('yes' or 'no'): ").lower()
            if add_choice in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.\n")

        if add_choice == 'yes':
            print("")  #empty line
            continue  #continue to add another policyholder
        else:
            print("")  #empty line
            break #exit if the user does not want to add another policyholder

def policyholder_menu():
    policy_filename = 'policyholders.csv'  #policyholders data file (change to your original policyholders file name)
    policyholders = read_policyholders(policy_filename)  #read policyholders from the file and store in a list

    while True:
        # menu to edit policyholders
        print("Policyholders Menu:") 
        choice = input("1. View Policyholder\n2. Add Policyholder\n3. Save and Exit\nPlease enter your choice: ")
        print("")

        # to view policyholder details
        if choice == '1':
            while True:
                policy_number = input("Enter the policy number to view details: ")
                policy_number = policy_number.strip().lower()  #the user input
                policyholder_data = None

                if policy_number == 'exit':
                    break  # exit the loop and go back to the main menu

                if len(policy_number) == 8 and policy_number[0] == 'p' and policy_number[1:].isdigit(): #check correct format
                    
                    #to find the policyholder
                    for index, policyholder in enumerate(policyholders): #iterate through policyholder list 
                        if policyholder[0].strip('0').lower() == policy_number.strip('0').strip().lower(): #compare if matches
                            policyholder_data = policyholders[index]  #assign matching policyholder's data, 
                            break  #break when match is found

                    if policyholder_data:
                        display_policyholder_details(policyholder_data)
                        break #exit the loop when a valid policy number is found
                    else:
                        print("No policyholder found with the entered policy number " + policy_number.capitalize() + ". Please try again.\n")
                else:
                    print("Invalid policy number format. Please enter a valid policy number (e.g., P1234567).\n")

        # add new policyholder
        elif choice == '2':
            add_policyholder(policyholders, policy_filename) #continue adding policyholders

        elif choice == '3':
            confirm_exit = input("Are you sure you want to exit and save data? ('yes' or 'no'): ").lower()
            while confirm_exit not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.\n")
                confirm_exit = input("Are you sure you want to exit and save data? ('yes' or 'no'): ").lower()

            if confirm_exit == 'yes':
                save_to_csv(policyholders, policy_filename)  # save before exit #save before exit
                break #exit the programme after saving

            elif confirm_exit == 'no':
                print("Returning to the main menu.\n")  # Return to the main menu
                break
        

        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

# Claims Management Functions ------------------------------------------------------------------------------------------------------------------------
# Function to read claims from csv file and return as a list of dictionaries
def read_claims(claims_filename): #dictionary for each claim
    claims = [] #empty list to store claim data
    with open(claims_filename, "r") as file: #open the specified file for reading (claims.txt)
        for line in file: #iterate through each line
            row = line.strip().split(',') #split into a list of values
            claims.append(row) #append dictionary to claims list
    return claims #return list

# Function to save policyholders into csv formatted file
def save_to_csv(policyholders, policy_filename):
    filename = input("Enter the filename to save the data (e.g., 'policyholders1.csv'): ")
    if not filename.lower().endswith('.csv'):
        filename += '.csv'
    with open(filename, 'w', newline='') as file:
        for policyholder in policyholders:
            file.write(','.join(policyholder) + '\n')
    print("Data saved to " + filename + " successfully.")
    
# Function to save claims into csv formatted file
def save_claims(claims):
    filename = input("Enter the filename to save the data (e.g., 'claims1.csv'): ")
    if not filename.lower().endswith('.csv'):
        filename += '.csv'
    with open(filename, 'w', newline='') as file:
        for claim in claims:
            file.write(','.join(claim) + '\n')
    print("Data saved to " + filename + " successfully.")

# Function to display claim details
def display_claim_details(claim_data):
    print("\nClaim Details")
    if len(claim_data) >= 3:
        print("Claim Number:", claim_data[0])  # print claim number (first element in list)
        print("Policy Number:", claim_data[1])  # print policy number
        print("Claim Amount:", claim_data[2])  # print claim amount
    else:
        print("Invalid claim data structure.")


# Function to add a new claim with validation
def add_claim(claims, policyholders,claims_filename):
    while True:
        print("") #add empty line before new data input
        # Claim Number #
        claim_number = input("Enter new claim number (e.g., C01234): ") #get claim number input
        if not claim_number or len(claim_number) != 6 or not claim_number[0] == 'C' or not claim_number[1:].isdigit():
            print("Invalid claim number format. Please enter a valid claim number.")          
            continue
        if any(claim[0] == claim_number for claim in claims): #check if claim number entered is unique 
            print("Claim number " + claim_number + " already exists. Please enter a *unique* claim number.")
            continue
        # Policy Number #
        while True:
            policy_number = input("Enter policy number for the claim (e.g., P0001234): ")
            if not policy_number.strip():
                print("Policy number cannot be empty.")
                continue
            if not any(policy_number == policyholder[0].strip().upper() for policyholder in policyholders):
                print("Policy number not found in the policyholder database.\n")
                #check if the policy number exists in the policyholder database
                continue
            else:
                break   
        #Claim Amount #
        while True:
            claim_amount = input("Enter claim amount: ")
            if not claim_amount.strip() or not claim_amount.isdigit(): # check if empty or is digit
                print("Invalid claim amount. Please enter a numerical value.\n")
                continue
            else:
                break

        # Display summary of input
        print("\nSummary of Claim Input:")
        print("Claim Number: " + claim_number)
        print("Policy Number: " + policy_number)
        print("Claim Amount: " + claim_amount)

        # Confirmation to save the claim 
        while True:
            save_confirmation = input("Do you want to save this claim? (yes or no): ")
            if save_confirmation in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.\n")       
        if save_confirmation.lower() == "yes":
            new_claim = [claim_number, policy_number, claim_amount] #dictionary for new claim data
            claims.append(new_claim) #append new claim data to claims list
            # Save the new claim to 'claims.csv'
            with open(claims_filename, 'a',newline='') as file: #append
                file.write(','.join(new_claim) + '\n')    
            print("Claim added successfully to 'claims.csv.\n")
        else:
            print("Claim not saved.\n")

        # Option to add another claim
        while True:
            add_choice = input("Do you want to add another claim? ('yes' or 'no'): ").lower()
            if add_choice in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.\n")        
        if add_choice == 'yes':
            continue  #continue to add another claim
        else:
            print("")  #empty line
            break #exit if the user does not want to add another claim


# Function to edit an existing claim
def edit_claim(claims, policyholders, claims_filename):
    while True:
        print("")
        #enter the claim number to edit
        claim_number = input("Enter the claim number to edit: ")
        if not claim_number.strip():
            print("Claim number cannot be empty.")
            continue
        #initialize variable to store index of the claim (for editing)
        index_to_edit = -1
        for i, claim in enumerate(claims): #iterate over claims list
            if claim[0] == claim_number: #check if claim number matches input
                index_to_edit = i #store index if match
                break #break if claim is found
        if index_to_edit == -1: # claim was not found
            print("Claim number not found.")
            continue

        print("Current Claim Details:")
        display_claim_details(claims[index_to_edit]) #display current details of claim for editing
        while True:
            new_policy_number = input("Enter new policy number: ")
            if not new_policy_number.strip():
                print("Policy number cannot be empty.")
                continue
            if not any(policyholder[0] == new_policy_number for policyholder in policyholders):
                #check if new policy number exists in policyholder database
                print("Policy number not found in the policyholder database.\n")
                continue
            else:
                break

        while True:
            new_claim_amount = input("Enter new claim amount: ")
            if  new_claim_amount.strip().isdigit():
                break
            else:
                print("Invalid claim amount. Please enter a numerical value.\n")

        #confirmation to edit data   
        while True:
            confirm_edit = input("Do you want to make these changes? (yes or no): ") #confirm changes
            if confirm_edit in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.\n")
                
        if confirm_edit.lower() == "yes": #update data
            #update claim in list
            claims[index_to_edit] = [claim_number, new_policy_number, str(new_claim_amount)]
            print("Claim updated successfully.\n")

            #save updated data back to file
            with open(claims_filename, 'w') as file:
                for claim in claims:
                    file.write(','.join(claim) + '\n')
        else:
            print("Claim not updated.")
        break

def claims_menu():
    policyholders_filename = 'policyholders.csv'
    claims_filename = 'claims.csv'

    # load existing policyholders and claims data
    policyholders = read_policyholders(policyholders_filename) #read policyholders data
    claims = read_claims(claims_filename) #read claims data

    # Main menu
    while True:
        print("Claims Menu:")
        print("1. View Claim Details")
        print("2. Add New Claim")
        print("3. Edit Existing Claim")
        print("4. Save and Exit")

        choice = input("Please enter your choice: ")

        if choice == '1': #view claim details
            for claim in claims:
                display_claim_details(claim) 
            print("")    
        elif choice == '2': #add new claim
            add_claim(claims, policyholders, claims_filename) 
        elif choice == '3': #edit existing claim
            edit_claim(claims, policyholders, claims_filename) 
        elif choice == '4':
            confirm_exit_claim = input("Are you sure you want to exit and save data? ('yes' or 'no'): ").lower()
            while confirm_exit_claim not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.\n")
                confirm_exit_claim = input("Are you sure you want to exit and save data? ('yes' or 'no'): ").lower()
            if confirm_exit_claim == 'yes':
                save_claims(claims) #save before exit
                break #exit the programme after saving
            elif confirm_exit_claim == 'no':
                print("Returning to the main menu.\n")  # Return to the main menu
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.\n")

# Analysis Functions----------------------------------------------------------------------------------------------------------------------------------
# Mapping for policyholders
def mapping_policyholder():
    policyholder_mapping = {}
    with open('policyholders.csv', 'r') as file: #read data from 'policyholders.csv' file
        lines = file.readlines()
        header = lines[0].strip().split(',')
        for line in lines[1:]: #process each line in the file from the second line (index 1)
            data = line.strip().split(',') #split each line into a list of values
            # creating a mapping using policy number as the key
            policyholder_mapping[data[0]] = {
                'First name': data[1].strip(),
                'Surname': data[2].strip(),
                'Age': data[3].strip(),
                'Gender': data[4].strip(),
                'Area': data[5].strip()
            }
    return policyholder_mapping

# Mapping for claims
def mapping_claim(policyholder_mapping):
    claims_mapping = {}
    with open('claims.csv', 'r') as file:
        lines = file.readlines()
        header = lines[0].strip().split(',')
        for line in lines[1:]:
            data = line.strip().split(',')
            try:
                claim_amount = int(data[2].strip())
            except ValueError:
                continue
            policy_number = data[1].strip()
            if policy_number in policyholder_mapping:
                if policy_number not in claims_mapping:
                    claims_mapping[policy_number] = {'Policy Number': policy_number, 'claims': []}
                claims_mapping[policy_number]['claims'].append(claim_amount)
    return claims_mapping


# Function to get valid input from the user
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().capitalize()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please enter a valid option.\n")

# function to perform analysis for the selected group
def analyse_selected_group(policyholder_data, claims_data, age, gender, area):
    group_key = (age, gender, area) #created a tuple to represent the group key based on age, gender and area
    #list to store policy numbers and claims for the selected group that the user input
    group_policyholders = []
    group_claims = []

    #iterate through policyholder data to identify members of the selected group
    for policy_number, policy_info in policyholder_data.items():
        if (policy_info['Age'] == age and
            policy_info['Gender'] == gender and
            policy_info['Area'] == area):
            # collect policy numbers and claims for the selected group
            group_policyholders.append(policy_number)
            if policy_number in claims_data:
                group_claims.extend(claims_data[policy_number]['claims'])

    #analysis calculations
    num_policyholders = len(group_policyholders)
    num_claims = len(group_claims)
    claim_frequency = num_claims / num_policyholders if num_policyholders else 0 ##if

    min_claim = max_claim = mean_claim = std_dev_claim = 0
    #set default values when there are no claims (number of claims <= 0) 
    if num_claims > 0:
        min_claim = min(group_claims) #the smallest size of claim in that group
        max_claim = max(group_claims) #the largest size of claim in that group
        mean_claim = sum(group_claims) / num_claims #the mean claim in that group
        std_dev_claim = (sum((x - mean_claim) ** 2 for x in group_claims) / num_claims) ** 0.5 #the standatd deviation of claims in that group
    
    # display analysis results for the selected group
    print("\nAnalysis for Group:", str(group_key))
    print("Number of policyholders: ", str(num_policyholders))
    print("Number of claims: ", str(num_claims))
    print("Claim frequency: {:.4f}".format(claim_frequency))  # Display claim frequency to 4 decimal places
    print("Smallest size of claim: ", str(min_claim))
    print("Largest size of claim: ", str(max_claim))
    print("Mean claim: {:.2f}".format(mean_claim))  # Display mean claim to 2 decimal places
    print("Standard deviation of claims: {:.2f}".format(std_dev_claim))

    #return relevant infomation for further use if needed
    return group_key, num_policyholders, num_claims, claim_frequency, min_claim, max_claim, mean_claim, std_dev_claim

# Function to save analysis to a binary file
def save_analysis_to_file(analysis_data, filename):
    with open(filename, 'wb') as file:
        encoded_data = "\n".join([f"{key}:{value}" for key, value in analysis_data.items()]).encode('utf-8')
        file.write(encoded_data)
    print("Analysis saved to '" + filename + "'.\n")

# retrieve analysis from a binary file
def retrieve_analysis_from_file(filename):
    analysis_data = {}
    with open(filename, 'rb') as file:
        # manually decode the bytes and reconstruct the analysis_data
        decoded_data = file.read().decode('utf-8')
        for line in decoded_data.split('\n'):
            if line:
                key, value = line.split(':', 1)
                analysis_data[key] = value
    print("Analysis retrieved from "+ filename)
    return analysis_data

policyholder_mapping = mapping_policyholder()
claims_mapping = mapping_claim(policyholder_mapping)

# Main analysis loop Function
def analysis_menu():
    # initialize variables before loop
    group_key = num_policyholders = num_claims = claim_frequency = min_claim = max_claim = mean_claim = std_dev_claim = None
    while True:
        # User inputs for age, gender, and area groups
        age_options = ['Young', 'Old']
        gender_options = ['Male', 'Female']
        area_options = ['South', 'Central', 'North']

        selected_age = get_valid_input("Enter age group (Young/Old): ", age_options)
        selected_gender = get_valid_input("Enter gender group (Male/Female): ", gender_options)
        selected_area = get_valid_input("Enter area group (South/Central/North): ", area_options)

        # perform analysis for the selected group
        group_key, num_policyholders, num_claims, claim_frequency, min_claim, max_claim, mean_claim, std_dev_claim = analyse_selected_group(
        policyholder_mapping, claims_mapping, selected_age, selected_gender, selected_area)

        #save and retrieve analysis
        save_filename = input("Enter the file name to save the analysis (e.g., analysis_saved.bin): ").strip()
        # Save analysis
        analysis_to_save = {
            'Group': group_key,
            'Number of policyholders': num_policyholders,
            'Number of claims': num_claims,
            'Claim frequency': claim_frequency,
            'Smallest size of claim': min_claim,
            'Largest size of claim': max_claim,
            'Mean claim': mean_claim,
            'Standard deviation of claims': std_dev_claim if num_claims > 1 else 'N/A'}
        save_analysis_to_file(analysis_to_save, save_filename)
        
        while True:
            print("Options:")
            print("1. Retrieve and view past analysis")
            print("2. Perform another analysis")
            print("3. Exit")
            user_choice = input("Please enter your choice (1, 2, or 3): ").strip()
            if user_choice == '1': # user input for the retrieve file name
                retrieve_filename = input("Enter the file name to retrieve the analysis: ").strip()
                # retrieve the file and display the analysis
                retrieved_analysis = retrieve_analysis_from_file(retrieve_filename)
                print("\nRetrieved Analysis: ")
                for key, value in retrieved_analysis.items():
                    print(key + ": " + value)
                print("")
                continue
            elif user_choice == '2': # break inner loop to start a new analysis
                break
            elif user_choice == '3': #exit
                # confirmation before exiting
                confirm_exit = input("Are you sure you want to exit the program? (yes/no): ").strip().lower()
                while confirm_exit not in ['yes', 'no']:
                    print("Invalid input. Please enter 'yes' or 'no'.\n")
                    confirm_exit = input("Are you sure you want to exit the program? (yes/no): ").strip().lower()
                if confirm_exit == 'yes':
                    print("Exiting the program.")
                    exit()
                else:
                    print("Returning to the main menu.\n")
                    continue
            else:
                print("Invalid choice. Please enter 1, 2, or 3.\n")

#---------------------------------------------------------------------------------------------------------------
# Main Menu
def main_menu():
    
    while True:
        print("\nMain Menu:")
        print("1. Policyholder Management")
        print("2. Claims Management")
        print("3. Analysis")
        print("4. Exit")

        choice = input("Please enter your choice: ")
        print("")

        if choice == '1':
            policyholder_menu()
        elif choice == '2':
            claims_menu()
        elif choice == '3':
            analysis_menu()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main_menu()
