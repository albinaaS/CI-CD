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

def total_by_population(file_path):
    total = {}
    with open(file_path, "r") as file:
        for line in file:
            country_name, _, population = parse_line(line)
            if country_name in total:
                total[country_name] += float(population)
            else:
                total[country_name] = float(population)
    return total

def total_by_area(file_path):
    total = {}
    with open(file_path, "r") as file:
        for line in file:
            country_name, area, _ = parse_line(line)
            if country_name in total:
                total[country_name] += float(area)
            else:
                total[country_name] = float(area)
    return total

def sort_total(total):
    return dict(sorted(total.items(), key=lambda x: x[1], reverse=True))

def write_file(file_path, total):
    with open(file_path, 'w') as file:
        for key, value in total.items():
            file.write(f'{key}: {value}\n')
