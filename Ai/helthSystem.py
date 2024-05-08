
def health_diagnostic():
    print("Welcome to the Health Diagnostic System!")
    potential_diseases = []

    # Ask questions based on the knowledge base
    print("Do you have a fever?")
    fever = input("Enter 'yes' or 'no': ").lower()
    if fever == "yes":
        print("Do you have a cough?")
        cough = input("Enter 'yes' or 'no': ").lower()
        if cough == "yes":
            print("Do you have shortness of breath?")
            breathlessness = input("Enter 'yes' or 'no': ").lower()
            if breathlessness == "yes":
                potential_diseases.append("COVID")
            else:
                potential_diseases.append("Bronchitis")
        else:
            potential_diseases.append("COVID")
    else:
        print("Do you have a sore throat?")
        sore_throat = input("Enter 'yes' or 'no': ").lower()
        if sore_throat == "yes":
            potential_diseases.append("Strep Throat")

    # Print potential diseases
    if potential_diseases:
        print("Based on your symptoms, potential diseases may include:")
        for disease in potential_diseases:
            print("- " + disease)
    else:
        print("No potential diseases found based on your symptoms.")


# Call the function to start the diagnostic process
health_diagnostic()
