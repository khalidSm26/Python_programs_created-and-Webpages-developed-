# Advanced Voting System



# Initialize Candidate List

valid_candidates = ["Alice", "Bob", "Charlie"]



# Initialize Variables

voters = []  # List to hold dictionaries of voter data



# Function to register a new voter

while True:

        age_input = input("Enter voter's age (18 to 120): ").strip()

        if not age_input.isdigit():

            print("Error: Age must be a number.")

            continue

        age = int(age_input)

        if age < 18 or age > 120:

            print("Error: Age must be between 18 and 120.")

            continue



 # Candidate choice validation

        candidate = input("Enter candidate choice (Alice, Bob, Charlie): ").strip()

        if candidate not in valid_candidates:

            print(f"Error: Invalid candidate. Choose from {valid_candidates}.")

            continue



 # Voter ID validation

        voter_id = input("Enter unique alphanumeric Voter ID: ").strip()

        if not voter_id or not voter_id.isalnum():

            print("Error: Voter ID must be non-empty and alphanumeric.")

            continue



 # Check for duplicate ID

        if any(voter["voter_id"] == voter_id for voter in voters):

            print("Error: Voter ID already exists. Use a unique ID.")

            continue



 # Store validated data

        voter_data = {

            "voter_id": voter_id,

            "age": age,

            "candidate": candidate

        }

        voters.append(voter_data)

        print("✅ Voter registered successfully!")

        break



# Function to display all registered voters


        if not voters:

            print("No voters registered yet.")

        else:

            print("\n=== Registered Voters ===")

        for voter in voters:

            print(f"ID: {voter['voter_id']}, Age: {voter['age']}, Candidate: {voter['candidate']}")

            print("\n")



# Function to search for a voter by ID


        search_id = input("Enter Voter ID to search: ").strip()

        for voter in voters:

            if voter["voter_id"] == search_id:

                 print(f"Voter Found - ID: {voter['voter_id']}, Age: {voter['age']}, Candidate: {voter['candidate']}")

                 print("Voter ID not found.")


#Main menu loop
                

        while True:

            print("\n==== Voting System Menu ====")

            print("1. Register New Voter")

            print("2. Display All Registered Voters")

            print("3. Search for a Voter by Voter ID")

            print("4. Exit the Program")

        choice = input("Select an option (1-4): ").strip()



        if choice == "1":
    
            register_voter()

        elif choice == "2":

            display_voters()

        elif choice == "3":

            search_voter()

        elif choice == "4":

            print("Exiting program. Goodbye!")

            break

        else:

            print("Invalid option. Please select from 1 to 4.")

print(__name__ == "_main_menu")
    



