# -*- coding: utf-8 -*-

import re
from braille_data import *


braille_dic_invert = create_invert_dic()
braille_dic_90 = create_turn90_dic()


def invert(input_str, dot_for_blank=False):
    if dot_for_blank:
        braille_dic_invert['⣿'] = '⠄'
        braille_dic_invert['⠄'] = '⣿'

    result_str = ""
    for i in range(0, len(input_str), 1):
        try:
            result_str += braille_dic_invert[input_str[i]]
        except KeyError:
            result_str += input_str[i]

    return result_str


def turn_90(input_str, dot_for_blank=False):
    line_arr = re.split(" |\n", input_str)
    longest_line = len(max(line_arr, key=len))
    new_line_arr = [' '] * (int(longest_line/2) + longest_line % 2)

    for line in line_arr:
        line_chunks = [line[i:i + 2] for i in range(0, len(line), 2)]
        for j in range(0, len(line_chunks), 1):
            try:
                new_chunk = braille_dic_90[line_chunks[j]]
            except KeyError:
                if j == len(line_chunks)-1:
                    new_chunk = ''
                else:
                    new_chunk = line_chunks[j]
            new_line_arr[j] = new_chunk + new_line_arr[j]

    if dot_for_blank:
        return ' '.join(new_line_arr).replace('⠀', '⠄')
    else:
        return ' '.join(new_line_arr)


def turn_180(input_str, dot_for_blank=False):
    return turn_90(turn_90(input_str, dot_for_blank), dot_for_blank)


def turn_270(input_str, dot_for_blank=False):
    return turn_90(turn_180(input_str, dot_for_blank), dot_for_blank)