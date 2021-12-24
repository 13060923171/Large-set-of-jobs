from itertools import groupby
def read_motion(location_name):
    filename = '{}.motion.txt'.format(location_name)
    house_list = []
    with open(filename,'r')as f:
        content = f.readlines()
        for line in content:
            line = line.strip("\n").split(',')
            if line[-1] == 'detected':
                house_list.append(line[0])
        return house_list

def read_emf(location_name):
    filename = '{}.emf.txt'.format(location_name)
    house_list = []
    number_list = []
    avg_list = []
    average_list = []
    room_list = []
    s = ''
    with open(filename,'r')as f:
        content = f.readlines()
        for line in content:
            line = line.strip("\n").split(',')[0]
            s += line
        ss = [''.join(list(g)) for k, g in groupby(s, key=lambda x: x.isdigit())]
        for figure in ss:
            if figure.isdigit() == True:
                number_list.append(number(figure))
                avg_list.append(len(figure))
            else:
                room_list.append(figure)
        for i in range(len(number_list)):
            average = number_list[i]/avg_list[i]
            average_list.append(average)
    for a in range(len(number_list)):
        if average_list[a]>3:
            house_list.append(room_list[a])
    return house_list

def number(j):
    sum = 0
    for i in j:
        sum += int(i)
    return sum

def read_temp(location_name):
    filename = '{}.temp.txt'.format(location_name)
    house_list = []
    house_list2 = []
    valid = []
    room = []
    line_list = []

    with open(filename, 'r')as f:
        content = f.readlines()
        for line in content:
            line = line.strip("\n").split(',')[0]
            line_list.append(line)
            valid.append(is_valid_temp(line))
        for v in range(len(valid)):
            if valid[v] == False:
                room.append(line_list[v])
        bathroom = line_list[1] +"," +line_list[2]+","+line_list[3] +"," +line_list[4]+","+line_list[5] +"," +line_list[6]+","+line_list[7]
        closet = line_list[9] +"," +line_list[10]+","+line_list[11] +"," +line_list[12]+","+line_list[13] +"," +line_list[14]+","+line_list[15]+"," +line_list[16]
        gameroom = line_list[18] +"," +line_list[19]+","+line_list[20]+","+line_list[21]+","+line_list[22] +"," +line_list[23]+","+line_list[24]+"," +line_list[25]+"," +line_list[26]+"," +line_list[27]
        kitchen = line_list[29] +"," +line_list[30]+","+line_list[31] +"," +line_list[32]+","+line_list[33] +"," +line_list[34]+","+line_list[35]+"," +line_list[36]
        breakroom = line_list[38] +"," +line_list[39]+","+line_list[40]+"," +line_list[41]+","+line_list[42]
        b_room = bathroom.split(',')
    try:
        for g in range(len(b_room)):
            if '-' in b_room[g] and '-' in b_room[g + 1] and '-' in b_room[g + 2] and '-' in b_room[g + 3] and '-' in \
                    b_room[g + 4]:
                house_list.append(room[0])
                house_list2 = list(set(house_list))

        c_room = closet.split(',')
        for g in range(len(c_room)):
            if '-' in c_room[g] and '-' in c_room[g + 1] and '-' in c_room[g + 2] and '-' in c_room[g + 3] and '-' in \
                    c_room[g + 4]:
                house_list.append(room[1])
                house_list2 = list(set(house_list))


        g_room = gameroom.split(',')
        for g in range(len(g_room)):
            if '-' in g_room[g] and '-' in g_room[g + 1] and '-' in g_room[g + 2] and '-' in g_room[g + 3] and '-' in g_room[g + 4]:
                house_list.append(room[2])
                house_list2 = list(set(house_list))


        k_room = kitchen.split(',')
        for g in range(len(k_room)):
            if '-' in k_room[g] and '-' in k_room[g + 1] and '-' in k_room[g + 2] and '-' in k_room[g + 3] and '-' in \
                    k_room[g + 4]:
                house_list.append(room[3])
                house_list2 = list(set(house_list))


        br_room = breakroom.split(',')
        for g in range(len(br_room)):
            if '-' in br_room[g] and '-' in br_room[g + 1] and '-' in br_room[g + 2] and '-' in br_room[g + 3] and '-' in \
                    br_room[g + 4]:
                house_list.append(room[4])
                house_list2 = list(set(house_list))
    except:
        pass
    return house_list2

def is_valid_temp(val):
    if '-' in val or '.' in val:
        val = val.strip('-').split('.')
        val = val[0]
    if val.isdigit() == True:
        return True
    else:
        return False

def generate_report(location, motion, emf, temp):
    filename = '{}.ravensnest.txt'.format(location)
    content = ['== Raven Ghost Hunting Society Haunting Report ==','Location: house']
    for m in motion:
        if m in emf and m in temp:
            content.append("Poltergeist in {}".format(m))
        elif m in emf:
            content.append("Oni in {}".format(m))
        elif m in temp:
            content.append("Bansheein in {}".format(m))
    for t in temp:
        if t in emf:
            content.append('Phantom in {}'.format(t))
    with open(filename, 'w')as f:
        for c in content:
            f.write(c+'\n')

if __name__ == '__main__':
    read_motion('house')
    read_emf('house')
    read_temp('house')
    motion = read_motion('house')
    emf = read_emf('house')
    temp = read_temp('house')
    generate_report('ghost_report',motion,emf,temp)
