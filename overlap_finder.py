# input file should be lists of gene_name and transcripts coordinates.

print 'dictionaries imported'


def get_widest_coordinate(coordinate_list):
    lefts = []
    rights = []
    for co in coordinate_list:
        lefts.append(int(co[1]))
        rights.append(int(co[2]))
    return (co[0], min(lefts), max(rights), co[3])


def elongate_coordinate(interval, coordinate_temp):
    return (coordinate_temp[0], coordinate_temp[1] - interval, coordinate_temp[2] + interval, coordinate_temp[3])


def find_cands(previous_position, target_coordinate):
    # find overlapped mrna candidate xlocs roughly. if ant='yes', only returns mrnas that are in the opposite strand.
    if previous_position < 0:
        previous_position = 0
    found_flag = 0
    found_position = 0
    overlapped_list = []
    for n, pos in enumerate(base_positions[previous_position:]):
        if (pos[0], pos[2]) > (target_coordinate[0], target_coordinate[1]) and n == 0:
            # check if problems arising from the first coordinate can occur
            print "error!!!"
        if (pos[0], pos[1]) > (target_coordinate[0], target_coordinate[2]):
            # when mrna overruns target_coordinate
            if found_flag == 0:
                return previous_position + n - 1, 0
            elif found_flag == 1 and overlapped_list == []:
                return found_position, 0
            elif found_flag == 1 and overlapped_list != []:
                return found_position, overlapped_list
        elif (pos[0], pos[2]) >= (target_coordinate[0], target_coordinate[1]):
            if found_flag == 0:
                found_position = previous_position + n - 1
                found_flag = 1
                overlapped_list.append(pos)
        else:
            continue


def sort_key(co_list):
    return (co_list[0], int(co_list[2]))


if __name__ == '__main__':
    list1 = []
    list2 = []
    position = 0
    base_positions = sorted(list2, key=sort_key)
    for target_pos in sorted(list1, key=sort_key):
        position, overlapped = find_cands(position, target_pos)
