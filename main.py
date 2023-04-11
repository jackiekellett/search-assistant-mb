kw = input('Input product key, such as: FGV11600WH00\n')

sites = [
    f'https://www.biggestbook.com/ui#/search?keyword={kw}&rs=96',
    f'https://www.iteminfo.com/search/k_{kw}/ps_48',
    f'https://www.bettymills.com/search?q={kw}',
    f'https://www.grainger.com/search?searchQuery={kw}'
]

for integer in range(0, len(sites)):
    print(sites[integer])
