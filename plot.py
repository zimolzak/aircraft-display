from time import sleep

R = 24
C = 80

def long2col(longit, cols=C, min_long=-96, max_long=-95.1):
    m = cols / (max_long - min_long)
    return int(round(m * (longit - min_long)))

def lat2row(lat, rows=R, min_lat=29.6, max_lat=29.9):
    m = -1 * rows / (max_lat - min_lat)
    return int(round(m * (lat - max_lat)))

matrix = []
for r in range(R):
    matrix.append([' '] * C)

def print_mat(m):
    for row in m:
        print(''.join(row))

LAT = 0.0
LON = 0.0
with open('out.txt') as fh:
    for line in fh:
        if 'latitude' in line and '.' in line:
            LAT = float(line[17:26])
            continue
        if 'longitude' in line and '.' in line:
            LON = float(line[17:27])
            myrow = lat2row(LAT)
            mycol = long2col(LON)
            matrix[myrow][mycol] = '*'
            print_mat(matrix)
            sleep(0.02)
