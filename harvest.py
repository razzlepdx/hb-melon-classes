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

        if isinstance(pairing, str):
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

    return {melon.code: melon for melon in melon_types}


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    def __init__(self, melon_type, shape_rating, color_rating, field_source, harvester):
        """Initialize a harvested melon"""
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_source = field_source
        self.harvester = harvester

    def is_sellable(self):
        """Returns boolean of whether melon is sellable.

        Melons are only sellable if not from field 3,
        and both shape and rating over 5

        >>> is_sellable(Melon(MelonType('musk', 1998, 'green',
                                        True, True, 'Muskmelon'),
                              6, 6, 6, 'Sheila'))
        True

        >>> is_sellable(Melon(MelonType('musk', 1998, 'green',
                                        True, True, 'Muskmelon'),
                              2, 6, 6, 'Sheila'))
        False

        >>> is_sellable(Melon(MelonType('musk', 1998, 'green',
                                        True, True, 'Muskmelon'),
                              6, 2, 6, 'Sheila'))
        False

        >>> is_sellable(Melon(MelonType('musk', 1998, 'green',
                                        True, True, 'Muskmelon'),
                              6, 6, 3, 'Sheila'))
        False

        """
        if self.field_source == 3 or self.shape_rating <= 5 or self.color_rating <= 5:
            return False

        return True


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    mc = make_melon_type_lookup(melon_types)

    melons = [Melon(mc['yw'], 8, 7, 2, 'Sheila'),
              Melon(mc['yw'], 3, 4, 2, 'Sheila'),
              Melon(mc['yw'], 9, 8, 3, 'Sheila'),
              Melon(mc['cas'], 10, 6, 35, 'Sheila'),
              Melon(mc['cren'], 8, 9, 35, 'Michael'),
              Melon(mc['cren'], 8, 2, 35, 'Michael'),
              Melon(mc['cren'], 2, 3, 4, 'Michael'),
              Melon(mc['musk'], 6, 7, 4, 'Michael'),
              Melon(mc['yw'], 7, 10, 3, 'Sheila')]
    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        print "{} harvested {} from field {}.".format(melon.harvester,
                                                      melon.melon_type.name,
                                                      melon.field_source)
        if melon.is_sellable():
            print "This melon is sellable.\n"
        else:
            print "This melon is not sellable.\n"
