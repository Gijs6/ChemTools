import random
import math
import time
import statistics
from statistics import fmean

ions = [
    {
        "name": "Acetaat",
        "formula": "CH3COO",
        "charge": 1,
        "chargetype": "-",
        "is_polyatomic": True
    },
    {
        "name": "Bromide",
        "formula": "Br",
        "charge": 1,
        "chargetype": "-",
        "is_polyatomic": False
    },
    {
        "name": "Chloride",
        "formula": "Cl",
        "charge": 1,
        "chargetype": "-",
        "is_polyatomic": False
    },
    {
        "name": "Fluoride",
        "formula": "F",
        "charge": 1,
        "chargetype": "-",
        "is_polyatomic": False
    },
    {
        "name": "Hydroxide",
        "formula": "OH",
        "charge": 1,
        "chargetype": "-",
        "is_polyatomic": True
    },
    {
        "name": "Jodide",
        "formula": "I",
        "charge": 1,
        "chargetype": "-",
        "is_polyatomic": False
    },
    {
        "name": "Nitraat",
        "formula": "NO3",
        "charge": 1,
        "chargetype": "-",
        "is_polyatomic": True
    },
    {
        "name": "Nitriet",
        "formula": "NO2",
        "charge": 1,
        "chargetype": "-",
        "is_polyatomic": True
    },
    {
        "name": "Waterstofcarbonaat",
        "formula": "HCO3",
        "charge": 1,
        "chargetype": "-",
        "is_polyatomic": True
    },
    {
        "name": "Carbonaat",
        "formula": "CO3",
        "charge": 2,
        "chargetype": "-",
        "is_polyatomic": True
    },
    {
        "name": "Oxide",
        "formula": "O",
        "charge": 2,
        "chargetype": "-",
        "is_polyatomic": False
    },
    {
        "name": "Sulfaat",
        "formula": "SO4",
        "charge": 2,
        "chargetype": "-",
        "is_polyatomic": True
    },
    {
        "name": "Sulfide",
        "formula": "S",
        "charge": 2,
        "chargetype": "-",
        "is_polyatomic": False
    },
    {
        "name": "Sulfiet",
        "formula": "SO3",
        "charge": 2,
        "chargetype": "-",
        "is_polyatomic": True
    },
    {
        "name": "Fosfaat",
        "formula": "PO4",
        "charge": 3,
        "chargetype": "-",
        "is_polyatomic": True
    },
    {
        "name": "Ammonium",
        "formula": "NH4",
        "charge": 1,
        "chargetype": "+",
        "is_polyatomic": True
    },
    {
        "name": "Kalium",
        "formula": "K",
        "charge": 1,
        "chargetype": "+",
        "is_polyatomic": False
    },
    {
        "name": "Lithium",
        "formula": "Li",
        "charge": 1,
        "chargetype": "+",
        "is_polyatomic": False
    },
    {
        "name": "Natrium",
        "formula": "Na",
        "charge": 1,
        "chargetype": "+",
        "is_polyatomic": False
    },
    {
        "name": "Zilver",
        "formula": "Ag",
        "charge": 1,
        "chargetype": "+",
        "is_polyatomic": False
    },
    {
        "name": "Barium",
        "formula": "Ba",
        "charge": 2,
        "chargetype": "+",
        "is_polyatomic": False
    },
    {
        "name": "Calcium",
        "formula": "Ca",
        "charge": 2,
        "chargetype": "+",
        "is_polyatomic": False
    },
    {
        "name": "IJzer(II)",
        "formula": "Fe",
        "charge": 2,
        "chargetype": "+",
        "is_polyatomic": False
    },
    {
        "name": "Lood(II)",
        "formula": "Pb",
        "charge": 2,
        "chargetype": "+",
        "is_polyatomic": False
    },
    {
        "name": "Magnesium",
        "formula": "Mg",
        "charge": 2,
        "chargetype": "+",
        "is_polyatomic": False
    },
    {
        "name": "Nikkel",
        "formula": "Ni",
        "charge": 2,
        "chargetype": "+",
        "is_polyatomic": False
    },
    {
        "name": "Zink",
        "formula": "Zn",
        "charge": 2,
        "chargetype": "+",
        "is_polyatomic": False
    },
    {
        "name": "Aluminium",
        "formula": "Al",
        "charge": 3,
        "chargetype": "+",
        "is_polyatomic": False
    },
    {
        "name": "IJzer(III)",
        "formula": "Fe",
        "charge": 3,
        "chargetype": "+",
        "is_polyatomic": False
    },
    {
        "name": "Lood(IV)",
        "formula": "Pb",
        "charge": 4,
        "chargetype": "+",
        "is_polyatomic": False
    }
]

pos_ions = [ion for ion in ions if ion["chargetype"] == "+"]
neg_ions = [ion for ion in ions if ion["chargetype"] == "-"]


def charges_to_indexes(chargeA, chargeB):
    lcm = math.lcm(chargeA, chargeB)
    amount_A = lcm // chargeA
    amount_B = lcm // chargeB

    if amount_A == 1:
        amount_A = ""
    if amount_B == 1:
        amount_B = ""
    return amount_A, amount_B


def generate_name_formula_pair():
    posion = random.choice(pos_ions)
    negion = random.choice(neg_ions)
    chemname = posion["name"] + negion["name"].lower()

    lcm = math.lcm(posion["charge"], negion["charge"])
    amount_posion = lcm // posion["charge"]
    amount_negion = lcm // negion["charge"]

    if amount_posion == 1:
        amount_posion = ""
    if amount_negion == 1:
        amount_negion = ""

    if posion["is_polyatomic"] and amount_posion:
        formula_posion_part = f"({posion["formula"]}){amount_posion}"
    else:
        formula_posion_part = f"{posion["formula"]}{amount_posion}"

    if negion["is_polyatomic"] and amount_negion:
        formula_negion_part = f"({negion["formula"]}){amount_negion}"
    else:
        formula_negion_part = f"{negion["formula"]}{amount_negion}"

    formula = formula_posion_part + formula_negion_part

    return chemname, formula


def check_awnser(input, awnser, capitals):
    # If capitals == true, the capitals NEED to be checked
    if capitals:
        return input.strip() == awnser.strip()
    else:
        return input.strip().lower() == awnser.strip().lower()




while True:
    print("Oefenen met zoutformules")
    user_input_amount_questions = input("Hoeveel vragen? ")
    amount_questions = int(user_input_amount_questions) if user_input_amount_questions.isdigit() else 5
    print("\nDaar gaan we!\n")

    durations = []
    correct_answers = 0
    semicorrect_answers = 0
    incorrect_answers = 0

    for i in range(1, amount_questions + 1):
        chemname, formula = generate_name_formula_pair()

        chemname_lower = chemname[0].lower() + chemname[1].lower() + chemname[
                                                                     2:]  # The first 2 letters (with the IJ) but not all (with Roman numerals)
        formula_subscript = ''.join('₀₁₂₃₄₅₆₇₈₉'[int(char)] if char.isdigit() else char for char in formula)

        if random.choice([0, 0, 1]) == 0:
            # Naam -> Formule
            vraag = f"Geef de formule van {chemname_lower}."
            antwoord = formula
            antwoord_formatted = formula_subscript
            capitals_setting = True
        else:
            vraag = f"Geef de naam van {formula_subscript}."
            antwoord = chemname_lower
            antwoord_formatted = chemname_lower
            capitals_setting = False

        print(f"Vraag {i}/{amount_questions}")
        print(vraag)
        start_time = time.time()
        input_attempt0 = input("Antwoord: ")

        if check_awnser(input_attempt0, antwoord.strip(), capitals_setting):
            end_time = time.time()
            correct_answers += 1

            print("Dat is goed!\n")
        else:
            print("Dat is helaas niet goed.")
            input_attempt1 = input("Probeer het opnieuw: ")
            if check_awnser(input_attempt1, antwoord.strip(), capitals_setting):
                end_time = time.time()
                semicorrect_answers += 1

                print("Dat is goed!\n")
            else:
                end_time = time.time()
                incorrect_answers += 1

                print("Dat is helaas weer niet goed.")
                print(f"Het goede antwoord was {antwoord_formatted}\n")

        durations.append(end_time - start_time)

    print("--- Statistieken ---")
    print(f"Je had {correct_answers} vragen in 1 keer goed ({round(correct_answers / amount_questions * 100, 1)}%).")
    print(f"Je had {semicorrect_answers} vragen na 1 fout toch goed ({round(semicorrect_answers / amount_questions * 100, 1)}%).")
    print(f"Je had {incorrect_answers} vragen fout ({round(incorrect_answers / amount_questions * 100, 1)}%).")
    print(f"Je deed gemiddeld {fmean(durations)} seconden over een vraag.")



    input_again = input("\nWil je nog een keer oefenen? (ja/nee): ")
    if input_again.lower().strip() == "ja":
        print("Nog een keer!")
    elif input_again.lower().strip() == "nee":
        print("Bedankt voor het oefenen!")
        break
    else:
        print("Dat is geen geldige keuze. Nou we gaan gewoon nog een keertje!")
