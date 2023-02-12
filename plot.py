from time import sleep

R = 24
C = 80
REF_LAT = 29.703
REF_LON = -95.411

def long2col(longit, cols=C, min_long=-96, max_long=-95.1):
    m = cols / (max_long - min_long)
    return int(round(m * (longit - min_long)))

def lat2row(lat, rows=R, min_lat=29.6, max_lat=29.9):
    m = -1 * rows / (max_lat - min_lat)
    return int(round(m * (lat - max_lat)))

class Map:
    def __init__(self):
        self.matrix = []
        for r in range(R):
            self.matrix.append([' '] * C)
    def update(self, lat, lon):
        myrow = lat2row(lat)
        mycol = long2col(lon)
        self.matrix[myrow][mycol] = '*'
        for row in self.matrix:
            print(''.join(row))

LAT = 0.0
LON = 0.0
mymap = Map()
with open('out.txt') as fh:
    for line in fh:
        if 'latitude' in line and '.' in line:
            LAT = float(line[17:26])
            continue
        if 'longitude' in line and '.' in line:
            LON = float(line[17:27])
            mymap.update(LAT, LON)
            sleep(0.02)
