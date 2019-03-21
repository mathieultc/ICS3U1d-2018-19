cigars = int(input("Please enter the number of cigars here: "))
is_weekend = True
def cigar_party(cigars,is_weekend):
    if is_weekend:
        if cigars>=40:
            return True
        else:
            return False
    elif cigars>=40 and cigars<=60:
        return True
    else:
        return False
def main():
    print(cigar_party(cigars,is_weekend))

main()