from os import getenv
from os import path
from time import sleep
import json

def read_file(filepath_var):
    Locations = []
    Items_found = []
    Time_found = []
    Locations_missing = []
    Locations_found = []
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
    filepath = getenv('LocalAppData') + 'Low\\Acid Nerve\\DeathsDoor\\SAVEDATA\\' + filepath_var.get() + '-ItemChanger.json'

    if path.isfile(filepath):
        try:
            f = open(filepath, 'r')
            data = json.load(f)

            for i in data['Placements']:
                Locations.append(i)
                match data['Placements'][i]:
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
                        
            for i in data['TrackerLog']:
                Locations_found.append(i['LocationName'])
                match i['ItemName']:
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
                        Items_found.append(i['ItemName'])
            f.close()
            
            Locations_missing = [x for x in Locations if x not in Locations_found]
            Items_found.reverse()
        except:
            sleep(0.2)
            print('err1')
        
    filepath = getenv('LocalAppData') + 'Low\\Acid Nerve\\DeathsDoor\\SAVEDATA\\Randomizer Helper Log.txt'
    Locations_accessable = {}
    current = ''
    if path.isfile(filepath):
        try:
            f = open(filepath, 'r')
            for line in f.readlines():
                if ':' in line and line.strip() and not 'UNCHECKED REACHABLE LOCATIONS' in line:
                    Locations_accessable[line.replace(':', '').strip()] = []
                    current = line.replace(':', '').strip()
                elif not ':' in line and line.strip():
                    if not line in Locations_accessable:
                        Locations_accessable[current].append(line.strip())
        except:
            sleep(0.2)
            print('err2')
            
    filepath = getenv('LocalAppData') + 'Low\\Acid Nerve\\DeathsDoor\\SAVEDATA\\Randomizer Settings.json'
    IncludeBelltowerKey = True;
    if path.isfile(filepath):
        try:
            f = open(filepath, 'r')
            for line in f.readlines():
                if 'IncludeBelltowerKey' in line:
                    if ('false' in line):
                        IncludeBelltowerKey = False
                if 'GreenTabletDoorCost' in line:
                    y = line.split(': ')
                    y = y[1].strip()
                    seeds_count = (int)(y[:-1])
        except:
            sleep(0.2)
            print('err3')
        
        
    return Items_found, Time_found, Locations, Locations_missing, Locations_accessable, souls_found, seeds_found, vitality_found, magic_found, souls_count, seeds_count, vitality_count, magic_count, pink_key_found, yellow_key_found, green_key_found, pink_key_count, yellow_key_count, green_key_count, IncludeBelltowerKey
  