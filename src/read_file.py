from os import getenv
from os import path

def read_file(filepath_var):
    Locations = []
    Items_found = []
    Time_found = []
    Locations_missing = []
    souls_found = 0
    seeds_found = 0
    vitality_found = 0
    magic_found = 0
    souls_count = 0
    seeds_count = 0
    vitality_count = 0
    magic_count = 0
    pink_key_found = 0
    green_key_found = 0
    yellow_key_found = 0
    pink_key_count = 0
    green_key_count = 0
    yellow_key_count = 0
    filepath = getenv('LocalAppData') + 'Low\Acid Nerve\DeathsDoor\SAVEDATA\\' + filepath_var.get() + '-ItemChanger.json'

    if path.isfile(filepath):
        f = open(filepath, 'r')
        content = f.read()
        if len(content)>0:
            # found items
            for x in content.split('"LocationName"'):
                y = x.split('"')
                if not y[1] == 'Placements' and len(y)>5:
                    Locations.append(y[1])
                    # Items_found.append(y[5])
                    match y[5]:
                        case '100 Souls':
                            souls_found += 1
                        case 'Life Seed':
                            seeds_found += 1
                        case 'Vitality Shard':
                            vitality_found += 1
                        case 'Magic Shard':
                            magic_found += 1
                        case 'Pink Key':
                            pink_key_found += 1
                        case 'Green Key':
                            green_key_found += 1
                        case 'Yellow Key':
                            yellow_key_found += 1
                        case _:
                            Items_found.append(y[5])
                    if len(y)>12:
                        z = y[12].split(':')
                        Time_found.append(float(z[1][:-3]))
            # missing items
            x = content.split('"TrackerLog"')
            loc = True
            insert = False
            go = False
            for y in x[0].split('"'):
                if go and y not in [',',':','},']:
                    if loc:
                        if not y in Locations:
                            Locations.append(y)
                            Locations_missing.append(y)
                            insert = True
                        loc = False
                    else:
                        if insert:
                            insert = False
                        loc = True
                        match y:
                            case '100 Souls':
                                 souls_count += 1
                            case 'Life Seed':
                                 seeds_count += 1
                            case 'Vitality Shard':
                                 vitality_count += 1
                            case 'Magic Shard':
                                 magic_count += 1
                            case 'Pink Key':
                                pink_key_count += 1
                            case 'Green Key':
                                green_key_count += 1
                            case 'Yellow Key':
                                yellow_key_count += 1
                else:
                    if ':{' in y:
                        go = True
        f.close()
        Items_found = [x for _, x in sorted(zip(Time_found, Items_found), reverse=True)]
        
    filepath = getenv('LocalAppData') + 'Low\Acid Nerve\DeathsDoor\SAVEDATA\\Randomizer Helper Log.txt'
    Locations_accessable = {}
    current = ''
    if path.isfile(filepath):
        f = open(filepath, 'r')
        for line in f.readlines():
            if ':' in line and line.strip() and not 'UNCHECKED REACHABLE LOCATIONS' in line:
                Locations_accessable[line.replace(':', '').strip()] = []
                current = line.replace(':', '').strip()
            elif not ':' in line and line.strip():
                if not line in Locations_accessable:
                    Locations_accessable[current].append(line.strip())
        
    return Items_found, Time_found, Locations, Locations_missing, Locations_accessable, souls_found, seeds_found, vitality_found, magic_found, souls_count, seeds_count, vitality_count, magic_count, pink_key_found, yellow_key_found, green_key_found, pink_key_count, yellow_key_count, green_key_count
  