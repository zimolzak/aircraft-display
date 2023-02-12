# dump1090-mutability 2> /dev/null | python plot.py

from time import sleep
import sys
import curses

R = 24
C = 80
REF_LAT = 29.703
REF_LON = -95.411

def long2col(longit, cols=C, min_long=-96, max_long=-95.1):
    m = cols / (max_long - min_long)
    return int(round(m * (longit - min_long)))

def lat2row(lat, rows=R, min_lat=29.6, max_lat=30.0):
    m = -1 * rows / (max_lat - min_lat)
    return int(round(m * (lat - max_lat)))

def main(stdscr):
    lat = REF_LAT
    lon = REF_LON
    myrow = lat2row(lat)
    mycol = long2col(lon)
    last_icao = ''
    last_ident = ''
    icao_ident = {}
    curses.initscr()  # not sure if needed
    stdscr.addstr(myrow, mycol, "H")
    stdscr.refresh()

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
            myrow = lat2row(lat)
            mycol = long2col(lon)
            try:
                id_str = '.' + icao_ident[last_icao]
            except KeyError:  # When ICAO has no Ident yet
                id_str = '.'
            #if 0 <= myrow <= R and 0 <= mycol <= C:
            try:
                stdscr.addstr(myrow, mycol, id_str)
                stdscr.refresh()
            except Exception:
                pass
    sleep(10)

curses.wrapper(main)
