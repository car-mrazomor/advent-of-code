import sys

draws, *blocks = sys.stdin.read().strip().split("\n\n")
boards = [[row.split() for row in block.splitlines()] for block in blocks]
marked = set()


def won(board):
    return any(all(n in marked for n in row) for row in board) or any(all(n in marked for n in col) for col in zip(*board))


for number in draws.split(","):
    marked.add(number)
    winners = [b for b in boards if won(b)]
    if winners:
        print(sum(int(n) for row in winners[0] for n in row if n not in marked) * int(number))
        break
