import os
import math
import random
from sys import stdout
from time import sleep
from blessings import Terminal
import decimal
import string
import socket

import life
import eliza
import type
import human as h
import color as c

t = Terminal()

ip = "127.0.0.1"
port = 2046 #wkw

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

source = open('program.py', 'r')
paper = open('turing.txt', 'r')
symbols = open('symbols.txt', 'r')
legends = open('legends.txt', 'r')

choice = ""
prompt = "waiting for your input > "

human = h.Human()
red = c.Color()

turing = []
truth_symbols = []
truth_legends = []

def say(w):
    message = w
    sock.sendto(message.encode('utf-8'), (ip, port))

def setup_turing():
    for line in paper:
        turing.append(line.replace('\\n', '\n'))

def setup_truth():
    for symbol in symbols:
        truth_symbols.append(symbol)
    for legend in legends:
        truth_legends.append(legend)


def set_style(st):
    if st == 'reverse':
        print(t.reverse+'', end="")
    elif st == 'red':
        print('{t.red}'.format(t=t), end="")

def reset_style():
    print('{t.normal}'.format(t=t), end="")
    print(t.on_black+"", end="")

def title():
    print('\n')
    type.spell("########################",1)
    sleep(0.1)
    type.set_interval(0.1)
    type.spell('    machine language', 1)
    type.set_interval(0.03)
    sleep(0.1)
    type.spell("########################", 1)
    for x in range(0, 10):
        sleep(0.1)
        print('\n')

def chapter(title):
    sleep(0.5)
    os.system('clear')
    sleep(0.25)
    type.spell('------------------------'+title, 0)
    sleep(0.1)
    print("")
    sleep(0.1)
    print("")
    sleep(0.1)
    print("")

def end_chapter():
    sleep(2)
    for x in range(0, 5):
        sleep(0.1)
        print("")
    # os.system('clear')

def display_turing():
    type.spell("Received 29 May 1936 - Read 12 November 1936, by ", 0)
    set_style('reverse')
    type.spell("Alan Turing", 0)
    reset_style()
    print("")
    sleep(0.1)
    print("")
    sleep(2)

    type.set_interval(0.01)

    turing_index = 0
    global turing

    while turing_index < len(turing):
        if turing_index == 2 or turing_index == 5 or turing_index == 8 or turing_index == 10 or turing_index == 12 or turing_index == 15 or turing_index == 17:
            set_style('reverse')
        else:
            reset_style()
        type.spell(turing[turing_index], 0)
        reset_style()
        turing_index += 1
    type.set_interval(0.03)
    print("")
    print("")

def print_error():
    r = random.random()

    if r < 0.2:
        type.spell('excuse me?', 1)
    elif r < 0.4:
        type.spell('i didn\'t quite understand.', 1)
    elif r < 0.6:
        type.spell('can you say that again?', 1)
    elif r < 0.8:
        type.spell('what did you say?', 1)
    else:
        type.spell('i\'m sorry?', 1)

def display_truth():
    index = 0
    # type.set_interval(0.04)
    for index in range(0, len(truth_symbols)):
        set_style("reverse")
        type.spell(" "+truth_symbols[index], 1)
        reset_style()
        type.spell(truth_legends[index], 0)
        sleep(1)
        print("\n\n")
        index += 1
    print("")
    # type.set_interval(0.04)

def read_process_write():
    t = 0
    while t < 15:
        type.spell("READ", 1)
        type.spell("PROCESS", 1)
        type.spell("WRITE", 1)
        t += 1
    message = "end"
    sock.sendto(message.encode('utf-8'), (ip, port))

def compute(complexity_level):
    add = ""
    sub = ""
    mult = ""
    div = ""

    read = " "
    write = " "

    if complexity_level == 1:
        add = "+ "
        sub = "- "
        mult = "* "
        div = "/ "
    elif complexity_level == 2:
        add = ""+bin(ord('a'))[2:]+bin(ord('d'))[2:]+bin(ord('d'))[2:]+" "
        sub = ""+bin(ord('s'))[2:]+bin(ord('u'))[2:]+bin(ord('b'))[2:]+" "
        mult = ""+bin(ord('m'))[2:]+bin(ord('u'))[2:]+bin(ord('l'))[2:]+" "
        div = ""+bin(ord('d'))[2:]+bin(ord('i'))[2:]+bin(ord('v'))[2:]+" "
        read = ""+bin(ord('r'))[2:]+bin(ord('e'))[2:]+bin(ord('a'))[2:]+bin(ord('d'))[2:]+" "
        write = ""+bin(ord('w'))[2:]+bin(ord('r'))[2:]+bin(ord('i'))[2:]+bin(ord('t'))[2:]+bin(ord('e'))[2:]+" "
    elif complexity_level == 3:
        add = "ADD "
        sub = "MIN "
        mult = "MUL "
        div = "DIV "
        read = "READ "
        write = "WRITE "


    a = 0
    b = 0
    t = 0
    while t < 4:
        if(complexity_level == 2):
            type.spell(read+str(bin(int(a))[2:]), 1)
        else:
            type.spell(read+str(a), 1)

        sleep(0.5)
        b = random.randint(0, 256)
        r = random.random()
        if r < 0.25:
            if(complexity_level == 2):
                type.spell(add+str(bin(b)[2:]), 1)
            else:
                type.spell(add+str(b), 1)
            sleep(0.5)
            a += b
        elif r < 0.5:
            if(complexity_level == 2):
                type.spell(sub+str(bin(b)[2:]), 1)
            else:
                type.spell(sub+str(b), 1)
            sleep(0.5)
            a -= b
        elif r < 0.75:
            if(complexity_level == 2):
                type.spell(mult+str(bin(b)[2:]), 1)
            else:
                type.spell(mult+str(b), 1)
            sleep(0.5)
            a *= b
        else:
            if(complexity_level == 2):
                type.spell(div+str(bin(b)[2:]), 1)
            else:
                type.spell(div+str(b), 1)
            sleep(0.5)
            a /= b
        t += 1

        if complexity_level == 2:
            if a < 0:
                a *= -1
                dec_a = float(a)
                hex_a = int(a)
                type.spell(write+'-'+str(bin(hex_a)[2:]), 1)
            else:
                dec_a = float(a)
                hex_a = int(a)
                type.spell(write+str(bin(hex_a)[2:]), 1)
        else:
            type.spell(write+str(a)[2:], 1)

def display_datatypes():
    type.spell("a ", 0)
    set_style("reverse")
    type.spell("boolean", 0)
    reset_style()
    type.spell(" is a datatype which represents the value true or false.", 2)

    sleep(1)

    type.spell("a ", 0)
    set_style("reverse")
    type.spell("floating point", 0)
    reset_style()
    type.spell(" is a datatype which represents rational numbers.", 2)

    sleep(1)

    type.spell("a ", 0)
    set_style("reverse")
    type.spell("integer", 0)
    reset_style()
    type.spell(" is a datatype which represents whole numbers.", 2)

    sleep(1)

    type.spell("a ", 0)
    set_style("reverse")
    type.spell("fixed point", 0)
    reset_style()
    type.spell(" is a datatype which represents a monetary value.", 2)

    sleep(1)

    type.spell("an ", 0)
    set_style("reverse")
    type.spell("array", 0)
    reset_style()
    type.spell(" is a datatype which stores a number of elements of the same type in a specific order.", 2)

    sleep(1)

    type.spell("an ", 0)
    set_style("reverse")
    type.spell("object", 0)
    reset_style()
    type.spell(" is a datatype which contains a number of data fields, as well as a number of subroutines for accessing or modifying them, called methods.", 2)

    sleep(1)

    type.spell("an ", 0)
    set_style("reverse")
    type.spell("object", 0)
    reset_style()
    type.spell(" is a datatype which can be ", 0)
    set_style("reverse")
    type.spell("anything", 0)
    reset_style()
    type.spell(".", 2)

def dislay_object_skeleton():
    type.spell("Object(){", 1)
    type.spell("\t be_something = ''", 1)
    type.spell("\t store_something = 0", 1)
    type.spell("\t do_something(arg){", 1)
    type.spell("\t\t ...", 1)
    type.spell("\t }", 1)
    type.spell("}", 2)
    type.spell("let o = new Object()", 3)

def generate_string():
    output = ''
    length = random.randint(3, 14)
    index = 0
    while index < length:
        output += random.choice(string.ascii_letters)
        index += 1
    return output

def generate_int():
    output = ''
    length = random.randint(3, 14)
    index = 0
    while index < length:
        output += str(random.randint(0, 9))
        index += 1
    return output

def elaborate_object():
    index = 0

    while index < 30:
        r = random.random()

        new_string = generate_string()
        new_int = generate_int()

        if r < 0.33:
            set_style("reverse")
            type.spell("be", 0)
            reset_style()
            type.spell("_something = '"+new_string+"'", 2)
        elif r < 0.66:
            set_style("reverse")
            type.spell("store", 0)
            reset_style()
            type.spell("_something = "+new_int+"", 2)
        else:
            set_style("reverse")
            type.spell("do", 0)
            reset_style()
            type.spell("_something(else)", 2)

        index += 1

def extrapolate_human():
    type.spell(str(human), 2)
    sleep(1)
    property_names = vars(human)
    for key in property_names:
        type.spell("%s: %s" % (key, property_names[key]), 2)
        sleep(0.5)

    print("--")
    sleep(3)

def enumerate_red():
    type.spell(str(red), 2)
    sleep(1)
    property_names = vars(red)
    for key in property_names:
        print("%s: %s" % (key, property_names[key]))

def blood_rain():
    ind = 0
    threshold = -0.0001
    while threshold < 1.3:
        if random.random() < threshold:
            print(t.on_red+"  ", end="")
        else:
            print(t.normal+" ", end="")
        ind+=1
        stdout.flush()
        sleep(0.001)
        threshold += 0.00005


def run_life():
    step = 0
    while step < 22:
        print("\n", end="")
        say(str('step '+str(step)))
        print(t.normal+"   life and death at step %i" % step)
        for char in life.my_game.display():
            if char == '1':
                print(t.normal+char.format(t=t), end="")
            else:
                print(t.dim_red+char.format(t=t), end="")
        sleep(2.8)

        life.my_game.step(step)
        step += 1
    sleep(1)
    reset_style()


def show_source():
    for line in source:
        type.spell(line, 0)
        sleep(0.001)

def main():
    choice = ""
    while choice != 'q':
        type.spell('waiting for input> ', 0)
        choice = input()

        if "add" in choice:
            say('add')

        elif "turing" in choice:
            chapter('TURING')
            display_turing()
            end_chapter()

        elif "truth" in choice:
            chapter('TRUTH')
            display_truth()
            end_chapter()

        elif "cycle" in choice or "read" in choice:
            say('read')

            type.set_interval(0.08)
            chapter('CYCLE')
            read_process_write()
            type.set_interval(0.03)
            end_chapter()

        elif "binary" in choice:
            chapter('BINARY')
            type.set_interval(0.02)
            compute(2)
            type.set_interval(0.03)
            end_chapter()

        elif "word" in choice:
            chapter('WORDS')
            compute(3)
            end_chapter()

        elif "data" in choice or "type" in choice:
            chapter('DATATYPES')
            display_datatypes()
            end_chapter()

        elif "object" in choice:
            chapter('OBJECTS')
            dislay_object_skeleton()
            elaborate_object()
            end_chapter()

        elif "human" in choice:
            chapter('HUMAN')
            type.set_interval(0.01)
            extrapolate_human()
            type.set_interval(0.03)
            end_chapter()

        elif "color" in choice:
            chapter('RED')
            enumerate_red()
            end_chapter()

        elif "red" in choice:
            chapter('RED')
            blood_rain()
            end_chapter()

        elif "eliza" in choice:
            chapter('ELIZA')
            set_style('reverse')
            eliza.converse()
            reset_style()
            end_chapter()

        elif "life" in choice:
            chapter('LIFE')
            run_life()
            end_chapter()

        elif "source" in choice:
            chapter('SOURCE')
            show_source()
            end_chapter()

        elif "enough" in choice:
            reset_style()
            type.spell("until next time", 1)
            quit()

        elif 'thank' in choice:
            say('thanks')
        else:
            print_error()


os.system('clear')
setup_turing()
setup_truth()
title()
reset_style()

try:
    main()
except KeyboardInterrupt:
    say('thanks')
    reset_style()
    print("\n\n\n")
    print('...thank you.\t\t\t pierredepaz.net', end="\n\n\n\n\n\n\n\n\n\n")
