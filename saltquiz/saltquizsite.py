from flask import Flask, redirect, flash, render_template, request
import random
import math
import re



app = Flask(__name__)



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
        formula_pos_ion_part = f"({pos_ion['formula']}){amount_pos_ion}"
    else:
        formula_pos_ion_part = f"{pos_ion['formula']}{amount_pos_ion}"

    if neg_ion["is_polyatomic"] and amount_neg_ion:
        formula_neg_ion_part = f"({neg_ion['formula']}){amount_neg_ion}"
    else:
        formula_neg_ion_part = f"{neg_ion['formula']}{amount_neg_ion}"

    formula = formula_pos_ion_part + formula_neg_ion_part

    return chemname, formula


def check_answer(user_input, answer, capitals):
    user_input = user_input.strip()
    answer = answer.strip()

    if capitals.lower() != "true":
        user_input = user_input.lower()
        answer = answer.lower()

    answer1 = re.sub(r'\([^)]*\)', '', answer)

    return user_input == answer or user_input == answer1



@app.route("/oefenen_zouten", methods=["GET", "POST"])
def zoutenoefenen():
    if request.method == "POST":
        question = request.form.get("question", "")
        capitals = request.form.get("capitals", "")
        app.logger.info(f"capitals {capitals}")
        antwoordinput = request.form.get("answer", "???")
        attempt = int(request.form.get("attempt", 0))
        correct_answer = request.form.get('correct_answer', '').strip()
        answer_formatted = request.form.get('answer_formatted', '').strip()


        if check_answer(antwoordinput, correct_answer.strip(), capitals):
            flash(f"{answer_formatted} is inderdaad goed!", "goed")

            return redirect("/oefenen_zouten")

        else:
            if attempt >= 2:
                flash(f"Helaas, dat is niet goed!\nHet goede antwoord is {answer_formatted}.", "fout2")
                return redirect("/oefenen_zouten")

            else:
                attempt += 1
                if any(char.isdigit() for char in correct_answer):
                    antwoordinput = "\(" + re.sub(r'(\d+)', r'_{\1}', antwoordinput) + "\)"
                flash(f"{antwoordinput} is helaas niet goed.\nProbeer het opnieuw.", "fout")
                return render_template('salt.html', question=question, correct_answer=correct_answer, answer_formatted=answer_formatted, capitals=capitals, attempt=attempt)



    else:
        chemname, formula = generate_name_formula_pair()

        chemname_lower = chemname[0].lower() + chemname[1].lower() + chemname[2:]  # The first 2 letters (with the IJ) but not all (with Roman numerals)

        formula_subscript = re.sub(r'(\d+)', r'_{\1}', formula)

        question_type = random.choice([1, 1, 2])


        if question_type == 1:
            # Naam -> Formule
            vraag = f"Geef de formule van {chemname_lower}."
            antwoord = formula
            antwoord_formatted = f"\({formula_subscript}\)"
            capitals_setting = True
        else:
            # Formule -> Naam
            vraag = f"Geef de naam van \({formula_subscript}\)."
            antwoord = chemname_lower
            antwoord_formatted = chemname
            capitals_setting = False


        app.logger.info(f"antwoord_formatted {antwoord_formatted}")


        return render_template('salt.html', question=vraag, correct_answer=antwoord, answer_formatted=antwoord_formatted, capitals=capitals_setting, attempt=0)
