from decimal import Decimal

def parse_line(line:str) ->tuple:
    items = line.split()
    if len(items) < 4:
        raise ValueError("Too short")
    _, *country_name, area, population = items
    area = area.replace('km^2', '')
    area = Decimal(area)
    population = Decimal(population)
    if area < 0:
        raise ValueError("Area lower then zero!")
    if population < 0:
        raise ValueError("Population lower then zero!")

    country_name = ' '.join(country_name).title()
    return country_name, area, population
