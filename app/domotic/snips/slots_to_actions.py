order_mapping_dict = {
   "action": {
        "TURN_OFF": ["eteins", "eteindre", "eteint", "eteignez",
                     "arrete", "arretes", "arreter", "arretez",
                     "éteins", "éteindre", "éteint", "éteignez", "arrête",
                     "arrêtes", "arrêter", "arrêtez", "coupe", "coupes",
                     "coupez", "couper"],
        "TURN_ON": ["allume", "allumer", "allumes", "allumez"],
        "INCREASE": ["augmente", "augmentes", "augmentez", "augmenter",
                     "monte", "montez", "monter", "montes"],
        "DECREASE": ["baisse", "baisses", "baissez", "baisser"],
        "PUT": ["mets", "mettez", "mettre"],
        "OPEN": ["ouvre", "ouvres", "ouvrez", "ouvrir"],
        "CLOSE": ["ferme", "fermez", "fermes", "fermer"],
        "PLAY": ["joues", "joue", "jouer", "jouez"],
        "CHANGE": ["change", "changes", "changer", "changez", "passe",
                   "passez", "passer", "passes"],
    }, "object": {
        "SOUND": ["son", "sons"],
        "LAMP": ["lampe", "lampes"],
        "LIGHT": ["lumière", "lumières"],
        "SHUTTER": ["volets", "volet"],
        "MUSIC": ["musique", "musiques"],
        "TV": ["télé", "télévision"],
        "DAMSO": ["damso"],
        "MUTE": ["mute"],
        "PAUSE": ["pause"],
        "VOLUME": ["volume", "volumes"]
    }, "quantity": {
    "MAX": ["max", "maximum", "fond"],
    "SLIGHTLY": ["légèrement", "un peu"],
    "SIGNIFICANTLY": ["beaucoup", "énormément"],
    }, "location": {
    "ROOM": ["chambre", "chambres"],
    "LIVING": ["salon", "salons"],
    "LINVING_CORNER": ["coin", "coins"],
    "KITCHEN": ["cuisine", "cuisines"]
    }
}


def get_slots(slots):
    understood_slots_dict = {}
    for slot in slots:
        understood_slots_dict[slot["slotName"]] = slot
    return understood_slots_dict


def normalize_slots(understood_slots_dict, order_mapping_dict):
    """
    corrects slots raw values if necessary
    """
    normalized_order = {}
    if ("action" in understood_slots_dict) and ("objet" in understood_slots_dict):
        for understood_slot_name, understood_slot in understood_slots_dict.items():
            for defined_slot_name, defined_slot_possibilities_dict in order_mapping_dict.items():
                for defined_slot_possibility_name, defined_slot_possibilities in defined_slot_possibilities_dict.items():
                    if understood_slots_dict[understood_slot_name]["rawValue"].lower() in defined_slot_possibilities:
                        normalized_order[defined_slot_name] = defined_slot_possibility_name

    return normalized_order


def snips_slots_to_actions(snips_slots, order_mapping_dict=order_mapping_dict):
    understood_slots_dict = get_slots(snips_slots)
    return normalize_slots(understood_slots_dict, order_mapping_dict)
