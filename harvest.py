############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        if type(pairing) == type(''):
            pairing = [pairing]
        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""
    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')

    muskmelon.add_pairing('mint')
    casaba.add_pairing(['strawberries', 'mint'])
    crenshaw.add_pairing('proscuitto')
    yellow_watermelon.add_pairing('ice cream')

    all_melon_types = [muskmelon, casaba, crenshaw, yellow_watermelon]

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print melon.name, "pairs with"
        for pairing in melon.pairings:
            print "- " + pairing
        print


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # melon_lookup = {}
    # # melon_lookup = 

    # for melon in melon_types:
    #     melon_lookup[melon.code] = melon

    return {melon.code: melon for melon in melon_types}


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



