with open ('cq-wpx-ssb.txt') as fh:
    for line in fh:
        fields = line.split()
        if len(fields) < 5:
            continue
        call = fields[4]
        for i in range(10):
            n = str(i)
            call = call.replace(n, n + " ")
        cs = call.split()
        print(cs[0])
