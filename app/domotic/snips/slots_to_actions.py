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
        "PLAY": ["play"],
        "VOLUME": ["volume", "volumes"]
    }, "quantity": {
    "MAX": ["max", "maximum", "fond"],
    "SLIGHTLY": ["légèrement", "un peu"],
    "SIGNIFICANTLY": ["beaucoup", "énormément"],
    "LOUDER": ["plus fort"],
    "LOWER": ["moins fort"]
    }, "location": {
    "ROOM": ["chambre", "chambres"],
    "LIVING": ["salon", "salons"],
    "LINVING_CORNER": ["coin", "coins"],
    "KITCHEN": ["cuisine", "cuisines"]
    }
}


def get_slots(slots):
    """ Returns a dictionnary with slots as keys.
    Args:
        slots (list): List of slots got from snips

    Returns:
        understood_slots_dict (dict): dictionnary with slots as keys

    get_slots([
        {
            'rawValue': 'eteins',
            'value': {'kind': 'Custom', 'value': 'Eteins'},
            'range': {'start': 0, 'end': 6},
            'entity': 'snips/default--action',
            'slotName': 'action',
            'confidenceScore': 0.93576235
        },
        {
            'rawValue': 'télé',
            'value': {'kind': 'Custom', 'value': 'télé'},
            'range': {'start': 7, 'end': 11},
            'entity': 'snips/default--objet',
            'slotName': 'objet',
            'confidenceScore': 0.8145191
        }])

    >>>     {'action': {'rawValue': 'eteins',
                        'value': {'kind': 'Custom', 'value': 'Eteins'},
                        'range': {'start': 0, 'end': 6},
                        'entity': 'snips/default--action',
                        'slotName': 'action',
                        'confidenceScore': 0.93576235},
             'object':  {'rawValue': 'télé',
                        'value': {'kind': 'Custom', 'value': 'télé'},
                        'range': {'start': 7, 'end': 11},
                        'entity': 'snips/default--objet',
                        'slotName': 'object',
                        'confidenceScore': 0.8145191}}
    """

    understood_slots_dict = {}
    for slot in slots:
        understood_slots_dict[slot["slotName"]] = slot
    return understood_slots_dict


def normalize_slots(understood_slots_dict, order_mapping_dict, logger):
    """ Returns dictionnary with normalized intents.
    Args:
        understood_slots_dict (dict): dictionnary with slots as keys
        order_mapping_dict (dict): mapping from normalize order to possibly understood words
        logger (utils.logger.Logger): log handler

    Returns:
        normalized_command (dict): dictionnary with normalized commands

    normalize_slots({'action': {'rawValue': 'eteins',
                        'value': {'kind': 'Custom', 'value': 'Eteins'},
                        'range': {'start': 0, 'end': 6},
                        'entity': 'snips/default--action',
                        'slotName': 'action',
                        'confidenceScore': 0.93576235},
             'object':  {'rawValue': 'télé',
                        'value': {'kind': 'Custom', 'value': 'télé'},
                        'range': {'start': 7, 'end': 11},
                        'entity': 'snips/default--objet',
                        'slotName': 'object',
                        'confidenceScore': 0.8145191}})

    >>>                 {'action': 'TURN_OFF', 'object': 'TV'}

    """
    normalized_command = {}
    if ("action" in understood_slots_dict):
        for understood_slot_name, understood_slot in understood_slots_dict.items():
            word = understood_slots_dict[understood_slot_name]["rawValue"].lower()
            found = False
            for defined_slot_possibility_name, defined_slot_possibilities in order_mapping_dict[understood_slot_name].items():
                if word in defined_slot_possibilities:
                    normalized_command[understood_slot_name] = defined_slot_possibility_name
                    found = True
            if not found:
                logger.warning("Not found '{word}' in vocab of {slot}"
                               .format(word=word,
                                       slot=understood_slot_name))

    return normalized_command


def snips_slots_to_actions(snips_slots, logger, order_mapping_dict=order_mapping_dict):
    """ Returns dictionnary with normalized intents.
    Args:
        snips_slots (list): List of slots got from snips
        order_mapping_dict (dict): mapping from normalize order to possibly understood words
        logger (utils.logger.Logger): log handler

    Returns:
        normalized_command (dict): dictionnary with normalized commands
    """
    understood_slots_dict = get_slots(snips_slots)
    return normalize_slots(understood_slots_dict, order_mapping_dict, logger)


def execute_order(snips_slots, logger):
    # actions_to_execute = snips_slots_to_actions(snips_slots, logger)
    return
