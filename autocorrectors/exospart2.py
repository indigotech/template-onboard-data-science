def part2exo2(rows, columns):
    rightrows = 344
    rightcolumns = 6

    if rows == rightrows and columns == rightcolumns:
        print("Good job! The number of rows is 344 and the number of columns is 6")
    else:
        if rows != rightrows:
            print("Oups, the number of rows is wrong!")
        if columns != rightcolumns:
            print("Oh no, the number of columns is wrong!")
        print("Please, try again")


def part2exo4(answer):
    rightanswer = 43.90552325581396
    if answer > rightanswer - 0.1 and answer < rightanswer + 0.1:
        print("Good job!")
    else:
        print("Oups, try again!")


def part2exo10(hcorr, lcorr):
    righthcorr = 'body_mass_g'
    rightlcorr = 'culmen_depth_mm'
    
    if hcorr == righthcorr and lcorr == rightlcorr:
        print("Good job!")
    else:
        print("Oh no! Please check again the correlation matrix")
