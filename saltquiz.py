import random
import math
import time
from statistics import fmean



neg_ions = [
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
    }
]


pos_ions = [
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

class style:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BG_RED = "\u001b[41m"
    BG_GREEN = "\u001b[42m"
    BG_YELLOW = "\u001b[43m"
    BG_BLUE = "\u001b[44m"
    BG_MAGENTA = "\u001b[45m"
    BG_CYAN = "\u001b[46m"
    BG_WHITE = "\u001b[47m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDER = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    RESET = "\033[0m"
    CLEAR = "\033[2J"


def generate_name_formula_pair():
    pos_ion = random.choice(pos_ions)
    neg_ion = random.choice(neg_ions)
    chemname = pos_ion["name"] + neg_ion["name"].lower()

    lcm = math.lcm(pos_ion["charge"], neg_ion["charge"])
    amount_pos_ion = lcm // pos_ion["charge"]
    amount_neg_ion = lcm // neg_ion["charge"]

    if amount_pos_ion == 1:
        amount_pos_ion = ""
    if amount_neg_ion == 1:
        amount_neg_ion = ""

    if pos_ion["is_polyatomic"] and amount_pos_ion:
        formula_pos_ion_part = f"({pos_ion["formula"]}){amount_pos_ion}"
    else:
        formula_pos_ion_part = f"{pos_ion["formula"]}{amount_pos_ion}"

    if neg_ion["is_polyatomic"] and amount_neg_ion:
        formula_neg_ion_part = f"({neg_ion["formula"]}){amount_neg_ion}"
    else:
        formula_neg_ion_part = f"{neg_ion["formula"]}{amount_neg_ion}"

    formula = formula_pos_ion_part + formula_neg_ion_part

    return chemname, formula


def check_awnser(input, awnser, capitals):
    # If capitals == true, the capitals NEED to be checked
    if input.lower().strip() in ["exit", "quit", "sluiten", "stop"]:
        exit(1)
    if capitals:
        return input.strip() == awnser.strip()
    else:
        return input.strip().lower() == awnser.strip().lower()




while True:
    print("Oefenen met zoutformules")
    print("Je kunt vragen ")
    user_input_amount_questions = input("Hoeveel vragen? ")
    amount_questions = int(user_input_amount_questions) if user_input_amount_questions.isdigit() else 5

    print("Hoe wil je oefenen?")
    print("1: Van naam naar formule")
    print("2: Van formule naar naam")
    print("3: Gemengd")
    user_input_qtype = input("Keuze: ")
    if user_input_qtype.isdigit() and 0 <= int(user_input_qtype) < 4:
        user_input_qtype_formatted = int(user_input_qtype)
    else:
        user_input_qtype_formatted = 3
        print("Dat is geen geldige keuze. We doen maar gemengd oefenen.")
    print("\nDaar gaan we!\n")


    durations = []
    correct_answers = 0
    semicorrect_answers = 0
    incorrect_answers = 0

    for i in range(1, amount_questions + 1):
        chemname, formula = generate_name_formula_pair()

        chemname_lower = chemname[0].lower() + chemname[1].lower() + chemname[2:]  # The first 2 letters (with the IJ) but not all (with Roman numerals)
        formula_subscript = ''.join('₀₁₂₃₄₅₆₇₈₉'[int(char)] if char.isdigit() else char for char in formula)


        if user_input_qtype_formatted in [1, 2]:
            question_type = user_input_qtype_formatted
        else:
            question_type = random.choice([1, 1, 2])


        if question_type == 1:
            # Naam -> Formule
            vraag = f"Geef de formule van {style.NEGATIVE}{chemname_lower}{style.RESET}."
            antwoord = formula
            antwoord_formatted = formula_subscript
            capitals_setting = True
        elif question_type == 2:
            vraag = f"Geef de naam van {style.NEGATIVE}{formula_subscript}{style.RESET}."
            antwoord = chemname_lower
            antwoord_formatted = chemname
            capitals_setting = False

        print(f"Vraag {i}/{amount_questions}")
        print(vraag)
        start_time = time.time()
        input_attempt0 = input("Antwoord: ")

        if check_awnser(input_attempt0, antwoord.strip(), capitals_setting):
            end_time = time.time()
            correct_answers += 1

            print(f"{style.NEGATIVE}{antwoord_formatted}{style.RESET}{style.BLACK}{style.BG_GREEN} is inderdaad goed!{style.RESET}\n")
        else:
            print(f"{style.BG_RED}Dat is helaas niet goed.{style.RESET}\n")
            input_attempt1 = input("Probeer het opnieuw: ")
            if check_awnser(input_attempt1, antwoord.strip(), capitals_setting):
                end_time = time.time()
                semicorrect_answers += 1

                print(f"{style.NEGATIVE}{antwoord_formatted}{style.RESET}{style.BLACK}{style.BG_GREEN} is goed.{style.RESET}\n")
            else:
                end_time = time.time()
                incorrect_answers += 1

                print(f"{style.BG_RED}Dat is helaas weer niet goed.{style.RESET}\n")

                print(f"Het goede antwoord was {style.NEGATIVE}{antwoord_formatted}{style.RESET}\n")

        durations.append(end_time - start_time)

    print("--- Statistieken ---")
    print(f"Je had {correct_answers} vragen in 1 keer goed ({round(correct_answers / amount_questions * 100, 1)}%).")
    print(f"Je had {semicorrect_answers} vragen na 1 fout toch goed ({round(semicorrect_answers / amount_questions * 100, 1)}%).")
    print(f"Je had {incorrect_answers} vragen fout ({round(incorrect_answers / amount_questions * 100, 1)}%).")
    print(f"Je deed gemiddeld {round(fmean(durations), 1)} seconden over een vraag.")



    input_again = input("\nWil je nog een keer oefenen? (ja/nee): ")
    if input_again.lower().strip() == "ja":
        print("Nog een keer!")
    elif input_again.lower().strip() == "nee":
        print("Bedankt voor het oefenen!")
        break
    else:
        print("Dat is geen geldige keuze. Nou we gaan gewoon nog een keertje!")
