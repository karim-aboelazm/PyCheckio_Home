def safe_pawns(pawns: set) -> int:
    safe_no = 0
    for pawn in pawns:
        p1 = chr(ord(pawn[0])-1)+str(int(pawn[1])-1)
        p2 = chr(ord(pawn[0])+1)+str(int(pawn[1])-1)
        safe_no += p1 in pawns or p2 in pawns
    return safe_no

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
