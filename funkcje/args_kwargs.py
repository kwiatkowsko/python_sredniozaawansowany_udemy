def calculate_paint(efficency_ltr_per_m2, *args):
    area = sum(args)
    result = efficency_ltr_per_m2 * area
    print(result)
calculate_paint(3,0,5,6)
args = [2,4,6,59]
calculate_paint(2, *args)

def log_it(*tekst):
    path = r'c:\temp\log_it.txt'
    with open(path, "a") as f:
        for line in tekst:
            f.write(line)
            f.write(' ')

        f.write("\n")


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')