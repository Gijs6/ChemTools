import random
import math
import re

ions = [
    {
        "name": "Acetaat",
        "formula": "CH3COO",
        "charge": "1",
        "chargetype": "-"
    },
    {
        "name": "Bromide",
        "formula": "Br",
        "charge": "1",
        "chargetype": "-"
    },
    {
        "name": "Chloride",
        "formula": "Cl",
        "charge": "1",
        "chargetype": "-"
    },
    {
        "name": "Fluoride",
        "formula": "F",
        "charge": "1",
        "chargetype": "-"
    },
    {
        "name": "Hydroxide",
        "formula": "OH",
        "charge": "1",
        "chargetype": "-"
    },
    {
        "name": "Jodide",
        "formula": "I",
        "charge": "1",
        "chargetype": "-"
    },
    {
        "name": "Nitraat",
        "formula": "NO3",
        "charge": "1",
        "chargetype": "-"
    },
    {
        "name": "Nitriet",
        "formula": "NO2",
        "charge": "1",
        "chargetype": "-"
    },
    {
        "name": "Waterstofcarbonaat",
        "formula": "HCO3",
        "charge": "1",
        "chargetype": "-"
    },
    {
        "name": "Carbonaat",
        "formula": "CO3",
        "charge": "2",
        "chargetype": "-"
    },
    {
        "name": "Oxide",
        "formula": "O",
        "charge": "2",
        "chargetype": "-"
    },
    {
        "name": "Sulfaat",
        "formula": "SO4",
        "charge": "2",
        "chargetype": "-"
    },
    {
        "name": "Sulfide",
        "formula": "S",
        "charge": "2",
        "chargetype": "-"
    },
    {
        "name": "Sulfiet",
        "formula": "SO3",
        "charge": "2",
        "chargetype": "-"
    },
    {
        "name": "Fosfaat",
        "formula": "PO4",
        "charge": "3",
        "chargetype": "-"
    },
    {
        "name": "Ammonium",
        "formula": "NH4",
        "charge": "1",
        "chargetype": "+"
    },
    {
        "name": "Kalium",
        "formula": "K",
        "charge": "1",
        "chargetype": "+"
    },
    {
        "name": "Lithium",
        "formula": "Li",
        "charge": "1",
        "chargetype": "+"
    },
    {
        "name": "Natrium",
        "formula": "Na",
        "charge": "1",
        "chargetype": "+"
    },
    {
        "name": "Zilver",
        "formula": "Ag",
        "charge": "1",
        "chargetype": "+"
    },
    {
        "name": "Barium",
        "formula": "Ba",
        "charge": "2",
        "chargetype": "+"
    },
    {
        "name": "Calcium",
        "formula": "Ca",
        "charge": "2",
        "chargetype": "+"
    },
    {
        "name": "IJzer(II)",
        "formula": "Fe",
        "charge": "2",
        "chargetype": "+"
    },
    {
        "name": "Magnesium",
        "formula": "Mg",
        "charge": "2",
        "chargetype": "+"
    },
    {
        "name": "Nikkel",
        "formula": "Ni",
        "charge": "2",
        "chargetype": "+"
    },
    {
        "name": "Zink",
        "formula": "Zn",
        "charge": "2",
        "chargetype": "+"
    },
    {
        "name": "Aluminium",
        "formula": "Al",
        "charge": "3",
        "chargetype": "+"
    },
    {
        "name": "IJzer(III)",
        "formula": "Fe",
        "charge": "3",
        "chargetype": "+"
    }
]

pos_ions = [ion for ion in ions if ion["chargetype"] == "+"]
neg_ions = [ion for ion in ions if ion["chargetype"] == "-"]


def charges_to_indexes(chargeA, chargeB):
    lcm = math.lcm(chargeA, chargeB)
    return lcm // chargeA, lcm // chargeB

def generate_name_formula_pair():
    posion = random.choice(pos_ions)
    negion = random.choice(neg_ions)
    chemname = posion["name"] + negion["name"].lower()


    # need to ad indexes
    formula = posion["formula"] + negion["formula"]


    # Polyatomic = samengesteld ion

    posion_is_polyatomic = len(re.findall(r'[a-zA-Z]', posion["formula"])) > 1
    negion_is_polyatomic = len(re.findall(r'[a-zA-Z]', negion["formula"])) > 1

    return chemname, formula