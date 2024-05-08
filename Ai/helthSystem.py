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
                potential_diseases.append("COVID-19")
            else:
                print("Do you have chest pain or discomfort?")
                chest_pain = input("Enter 'yes' or 'no': ").lower()
                if chest_pain == "yes":
                    potential_diseases.append("Bronchitis")
                else:
                    print("Do you have fatigue or body aches?")
                    fatigue = input("Enter 'yes' or 'no': ").lower()
                    if fatigue == "yes":
                        potential_diseases.append("COVID-19")
                    else:
                        print("Do you have headache or confusion?")
                        confusion = input("Enter 'yes' or 'no': ").lower()
                        if confusion == "yes":
                            potential_diseases.append("COVID-19")
                        else:
                            print("Do you have sore throat or runny nose?")
                            throat_nose_symptoms = input(
                                "Enter 'yes' or 'no': "
                            ).lower()
                            if throat_nose_symptoms == "yes":
                                potential_diseases.append("COVID-19")
                            else:
                                potential_diseases.append("COVID-19")
        else:
            print("Do you have muscle aches or fatigue?")
            muscle_aches = input("Enter 'yes' or 'no': ").lower()
            if muscle_aches == "yes":
                potential_diseases.append("COVID-19")
            else:
                print("Do you have sore throat or runny nose?")
                throat_nose_symptoms = input("Enter 'yes' or 'no': ").lower()
                if throat_nose_symptoms == "yes":
                    potential_diseases.append("Common Cold")
                else:
                    potential_diseases.append("COVID-19")
    else:
        print("Do you have a sore throat?")
        sore_throat = input("Enter 'yes' or 'no': ").lower()
        if sore_throat == "yes":
            print("Do you have swollen glands in your neck?")
            swollen_glands = input("Enter 'yes' or 'no': ").lower()
            if swollen_glands == "yes":
                potential_diseases.append("Strep Throat")
            else:
                print("Do you have white patches on your tonsils?")
                white_patches = input("Enter 'yes' or 'no': ").lower()
                if white_patches == "yes":
                    potential_diseases.append("Strep Throat")
                else:
                    potential_diseases.append("Sore Throat")
        else:
            print("Do you have chest congestion or wheezing?")
            chest_congestion = input("Enter 'yes' or 'no': ").lower()
            if chest_congestion == "yes":
                potential_diseases.append("Bronchitis")
            else:
                print("Do you have body aches or joint pain?")
                body_joint_pain = input("Enter 'yes' or 'no': ").lower()
                if body_joint_pain == "yes":
                    potential_diseases.append("COVID-19")
                else:
                    print("Do you have difficulty swallowing or loss of appetite?")
                    swallowing_difficulty = input("Enter 'yes' or 'no': ").lower()
                    if swallowing_difficulty == "yes":
                        potential_diseases.append("Strep Throat")
                    else:
                        potential_diseases.append("No specific disease")

    # Print potential diseases
    if potential_diseases:
        print("Based on your symptoms, potential diseases may include:")
        for disease in potential_diseases:
            print("- " + disease)
    else:
        print("No potential diseases found based on your symptoms.")


# Call the function to start the diagnostic process
health_diagnostic()
