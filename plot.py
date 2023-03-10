# dump1090-mutability 2> /dev/null | python plot.py

from time import sleep
import sys
import curses

R = 24
C = 80

def long2col(longit, cols=C, min_long=-96, max_long=-95.1):
    m = cols / (max_long - min_long)
    return int(round(m * (longit - min_long)))

def lat2row(lat, rows=R, min_lat=29.6, max_lat=30.0):
    m = -1 * rows / (max_lat - min_lat)
    return int(round(m * (lat - max_lat)))

def put_one_char(lat, lon, char, scr):
    myrow = lat2row(lat)
    mycol = long2col(lon)
    scr.addstr(myrow, mycol, char)
    scr.refresh()

def setup_map(scr):
    put_one_char(29.703, -95.411, 'X', scr)
    put_one_char(29.987, -95.342, 'I', scr)
    put_one_char(29.646, -95.278, 'H', scr)

def main(stdscr):
    # persist these for later
    lat = 0.0
    lon = 0.0
    last_icao = ''
    last_ident = ''
    icao_ident = {}

    curses.initscr()  # not sure if needed
    setup_map(stdscr)

    for line in sys.stdin:
        if 'ICAO Addr' in line:
            last_icao = line[17:]
        if 'Ident:' in line:
            last_ident = line[17:]
            icao_ident[last_icao] = last_ident
        if 'latitude' in line and '.' in line:
            lat = float(line[17:26])
            continue
        if 'longitude' in line and '.' in line:
            lon = float(line[17:27])
            try:
                id_str = '.' + icao_ident[last_icao]
            except KeyError:  # When ICAO has no Ident yet
                id_str = '.'
            #if 0 <= myrow <= R and 0 <= mycol <= C:
            try:
                put_one_char(lat, lon, id_str, stdscr)
                setup_map(stdscr)
            except Exception:
                pass
    sleep(10)

curses.wrapper(main)
