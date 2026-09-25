def main():
    sales_file = open('sales.txt', 'r')
    for line in sales_file:
        amont = float(line)
        print '' % amont
    sales_file.close()
main()