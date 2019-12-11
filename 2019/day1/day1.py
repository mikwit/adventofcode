import math
import argparse


def calculate_fuel(_module_mass):
    _cur_num = int(_module_mass)
    _total_fuel = 0
    _new_fuel = 0
    _extra_fuel = 0
    if ( _cur_num % 3 ) != 0:
        _new_fuel = math.floor( _cur_num / 3 ) - 2
    else:
        _new_fuel = _cur_num / 3 - 2
    _total_fuel += _new_fuel
    _start_fuel = _new_fuel
    while ( math.floor( _new_fuel / 3 ) ) > 2:
        _extra_fuel = ( math.floor( _new_fuel / 3 ) - 2 )
        # print(f"_extra_fuel : {_extra_fuel}")
        if _extra_fuel > 0:
            _total_fuel += _extra_fuel
            _new_fuel = _extra_fuel
        else:
            _total_fuel += 0
            _new_fuel = _extra_fuel
    # if _new_fuel == 2:
    #     _total_fuel += _new_fuel
    # _total_fuel += _new_fuel
    return _total_fuel



def do_the_thing(_input_file, _input_number):

    _total_fuel = 0
    _new_fuel = 0

    if _input_file:
        _data_file = open(_input_file, "r")
        for _line in _data_file:
            _total_fuel += calculate_fuel(int(_line))
    else:
        _total_fuel = calculate_fuel(int(_input_number))

    # if input_file:
    #     _data_file = open(input_file, "r")

    #     for _line in _data_file:
    #         _cur_num = int(_line)
    #         if ( _cur_num % 3 ) != 0:
    #             _new_fuel = math.floor( _cur_num / 3 ) - 2
    #         else:
    #             _new_fuel = _cur_num / 3 - 2
    #         _total_fuel += _new_fuel
    #         while ( math.floor( _new_fuel / 3 ) - 2 ) > 2:
    #             _extra_fuel = ( math.floor( _new_fuel / 3 ) - 2 )
    #             _total_fuel += _extra_fuel
    #             _new_fuel -= _extra_fuel
    #         _total_fuel += _extra_fuel
    #         # _total_fuel += _new_fuel
    # else:
    #     _cur_num = int(input_number)
    #     if ( _cur_num % 3 ) != 0:
    #         _total_fuel = math.floor( _cur_num / 3 ) - 2
    #     else:
    #         _total_fuel = _cur_num / 3 - 2


    print (f"whoa, total fuel is: {_total_fuel}")
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='take input file and calculate total fuel requirement')
    parser.add_argument('--file', '-f', dest='file', help='please give me a file to read')
    parser.add_argument('--number', '-n', dest='number', help='please give me a number')
    args = parser.parse_args()
    
    do_the_thing(args.file, args.number)
