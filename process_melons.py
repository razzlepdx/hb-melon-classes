from harvest import *

melon_types = make_melon_types()
mc = make_melon_type_lookup(melon_types)
melons = []

with open('harvest_log.txt') as file_data:
    for line in file_data:
        tokens = line.rstrip().split()
        #__init__(self, melon_type, shape_rating, color_rating, field_source, harvester):

        melon = Melon(mc[tokens[5]], tokens[1], tokens[3], tokens[-1], tokens[8])
        melons.append(melon)

get_sellability_report(melons)
