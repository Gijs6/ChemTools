import random
import math


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


for _ in range(10):
    print(generate_name_formula_pair())
