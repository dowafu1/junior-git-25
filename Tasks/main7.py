# def nums_sort(*nums):
#   print(*nums, sep=', ')
#
# nums_list = [3, 2, 1]
# nums_list.sort()
# nums_sort(*nums_list)
#
# def palindrom(word):
#   word_list = list(word)
#   word_list_revers = word_list[:]
#   word_list_revers.reverse()
#   if word_list == word_list_revers:
#     print(True)
#   else:
#     print(False)
#
# palindrom("lol")
# palindrom("hi")
#
#

chess = [
    ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
    ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
    ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
    ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
    ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
    ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
    ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
    ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'],
]

def safe_unsafe(pawn: str):
    for sublist in chess:
        for square in sublist:
            if square == pawn:
                sublist[sublist.index(square)] = 'X'
                print(chess.index(sublist))
                print(True)
                print(sublist)
                if chess.index(sublist)
safe_unsafe('b3')