# Output just the prefix from each QSO in a file.
#
# usage:
# python wpx.py| sort | uniq -c | sort -nr
# python wpx.py| sort | uniq -c | wc

with open ('cq wpx cw.txt') as fh:
    for line in fh:
        fields = line.split()
        if len(fields) < 5:
            continue
        call = fields[4]

        # Split call into prefix/suffix
        for i in range(10):
            n = str(i)
            call = call.replace(n, n + " ")

        # print only prefix
        cs = call.split()
        print(cs[0])
