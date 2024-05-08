# Code written by https://github.com/SorcierMaheP

Knowledge_base = {
    "COVID": [
        "Fever",
        "Cough",
        "Shortness of breath",
        "Fatigue",
        "Muscle aches",
        "Headache",
        "Loss of taste or smell",
        "Sore throat",
        "Congestion",
        "Nausea or vomiting",
        "Diarrhea",
    ],
    "Bronchitis": [
        "Persistent cough",
        "Cough that produces mucus",
        "Shortness of breath",
        "Wheezing",
        "Chest discomfort",
        "Fatigue",
        "Fever",
    ],
    "Strep Throat": [
        "Sore throat",
        "Difficulty swallowing",
        "Fever",
        "Swollen tonsils and lymph nodes",
        "Tiny red spots on the roof of the mouth",
        "Rash",
        "Nausea or vomiting",
    ],
}


def Inference_Engine(symptoms):
    chance = {}

    for disease in Knowledge_base:
        occurrence = 0
        # For each disease in knowledge base check if symptoms are match
        for symptom in Knowledge_base[disease]:
            occurrence += 1 if symptom in symptoms else 0
        chance[disease] = occurrence / len(Knowledge_base[disease])

    guess = (
        [
            disease
            for disease in Knowledge_base
            if chance[disease] == max(chance.values())
        ]
        if max(chance.values()) > 0
        else []
    )
    print()
    Explanation_Module(guess, chance)


def Explanation_Module(guess, chance):
    if len(guess) == 0:
        print("You have no disease according to us.")
    elif len(guess) > 1:
        print("We are confused between the following diseases.")
        for disease_guess in guess:
            print(f"{disease_guess}")
    elif chance[guess[0]] == 1:
        print(f"You definitely have {guess[0]} disease.")
    else:
        print(f"You may have {guess[0]} disease with probability {chance[guess[0]]} .")


def UI():
    symptoms = []
    questions = []

    # Add diseases symptoms to questions list
    for disease in Knowledge_base:
        questions.extend(Knowledge_base[disease])
    # Remove repeating symptoms among diseases
    questions = list(set(questions))

    print("Hello user! We will now evaluate your case.")
    for question in questions:
        reply = input(f"Do you have \033[1m{question}\033[0m as a symptom?[y/N]:")
        if reply.upper() == "Y":
            symptoms.append(question)

    Inference_Engine(symptoms)


if __name__ == "__main__":
    UI()
