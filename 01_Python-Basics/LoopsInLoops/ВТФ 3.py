import json
holder = 0
count_s = 0
count_m = 0

with open('bigf.json') as json_file:
    data = json.load(json_file)
    for p in data['disc']:

        if holder != p['s_num']:
            count_s += 1
        elif holder == p['s_num']:
            count_m += 1
        holder = p
