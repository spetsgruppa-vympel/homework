# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE
# I LOVE CHOCOLATE


# energy trapping people who try to climb after you (you are 2km above) is very fun
# n = input("8 digits numbers pls")
# if n < 10000000 or n > 99999999:
#     raise ValueError("Deleting System32...")
# first4 = n[0:4]
# last4 = n[4:]
# if first4 == last4:
#     print("YES")
# else:
#     print("NO")
# print(n)
# print(first4)
# print(last4)





# ⣟⢿⣟⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣒⣒⣂⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀
# ⠻⣄⠹⣯⡀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠉⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⢀⡦
# ⠀⠘⢦⡈⠻⢶⡶⠶⠶⠶⠶⠶⣦⡄⠀⠀⢰⡶⠶⠶⠶⠶⠤⠤⠶⠋⢀⡴⠏⠀
# ⠀⠀⠀⠙⢦⡘⢿⣟⠛⠛⠛⠛⠛⠁⠀⠀⢸⡇⣶⣶⣶⣶⣶⣶⣶⡚⠁⠀⠀⠀
# ⠀⠀⠀⠀⠀⠹⣆⠻⣷⣄⣀⣀⣀⠀⠀⠀⢸⡇⠘⠻⠟⠗⠒⠒⠲⠶⠶⠶⣷⠆
# ⠀⠀⠀⠀⠀⠀⠈⠳⣌⣉⣉⣉⣻⡇⠀⠀⠈⢻⠏⠉⠉⠉⠉⣹⣿⠟⣠⡾⠋⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡟⢹⡇⠀⠀⠀⠀⢀⣀⣀⣠⣾⠟⣡⡶⠋⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⡇⠀⠀⣠⠞⠋⣭⣭⣭⣥⠞⠋⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⣇⣤⠞⢁⡤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠼⠏⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣴⠟⠁⠀⠀⠀⠀⠀
# ⠀⠀⠀
# BigPhish Pha Ze Khan BigPhish ART OF CHOKE BigPhish J Kovv BigPhish Tu Vistzz
# BigPhish Brao Kih BigPhish  Ki Riy Gaon BigPhish Frao Zin BigPhish NEO BigPhish
from time import sleep
print('Whoops! Looks like you have to uncomment everything manually! Meanwhile enjoy this game of bosnia:')
sleep(5)




# this was made by chatgpt lol i aint got enuff time
import random
import sys
from typing import List, Tuple, Set

class Board:
    def __init__(self, rows: int, cols: int, mines: int):
        if mines >= rows * cols:
            raise ValueError("Too many mines for board size")
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.mines_set: Set[Tuple[int,int]] = set()
        self.revealed: List[List[bool]] = [[False]*cols for _ in range(rows)]
        self.flagged: List[List[bool]] = [[False]*cols for _ in range(rows)]
        self.numbers: List[List[int]] = [[0]*cols for _ in range(rows)]
        self._place_mines()
        self._compute_numbers()
        self.first_move = True

    def _place_mines(self):
        all_cells = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        mines = set(random.sample(all_cells, self.mines))
        self.mines_set = mines

    def _compute_numbers(self):
        for (r, c) in self.mines_set:
            self.numbers[r][c] = -1
        for r in range(self.rows):
            for c in range(self.cols):
                if self.numbers[r][c] == -1:
                    continue
                count = 0
                for rr in range(r-1, r+2):
                    for cc in range(c-1, c+2):
                        if (rr,cc) in self.mines_set:
                            count += 1
                self.numbers[r][c] = count

    def in_bounds(self, r:int, c:int) -> bool:
        return 0 <= r < self.rows and 0 <= c < self.cols

    def reveal(self, r:int, c:int) -> Tuple[bool, str]:
        if not self.in_bounds(r,c):
            return True, "out of bounds"
        if self.flagged[r][c]:
            return True, "cell is flagged"
        if self.revealed[r][c]:
            return True, "already revealed"

        # reveal it
        self.revealed[r][c] = True
        if (r,c) in self.mines_set:
            # reveal all mines
            for (mr,mc) in self.mines_set:
                self.revealed[mr][mc] = True
            return False, "skill issue little man."

        # if zero, flood fill neighbors
        if self.numbers[r][c] == 0:
            self._flood_fill(r,c)
        return True, "yes."

    def _flood_fill(self, r:int, c:int):
        stack = [(r,c)]
        while stack:
            cr, cc = stack.pop()
            for rr in range(cr-1, cr+2):
                for cc2 in range(cc-1, cc+2):
                    if not self.in_bounds(rr, cc2):
                        continue
                    if self.revealed[rr][cc2] or self.flagged[rr][cc2]:
                        continue
                    self.revealed[rr][cc2] = True
                    if self.numbers[rr][cc2] == 0 and (rr,cc2) not in self.mines_set:
                        stack.append((rr,cc2))

    def toggle_flag(self, r:int, c:int) -> str:
        if not self.in_bounds(r,c):
            return "out of bounds."
        if self.revealed[r][c]:
            return "can't flag a revealed cell."
        self.flagged[r][c] = not self.flagged[r][c]
        return "flagged." if self.flagged[r][c] else "unflagged."

    def check_win(self) -> bool:
        # win if all non-mine cells are revealed
        for r in range(self.rows):
            for c in range(self.cols):
                if (r,c) in self.mines_set:
                    continue
                if not self.revealed[r][c]:
                    return False
        return True

    def display(self, reveal_all=False) -> str:
        header = "    " + " ".join(f"{c:2}" for c in range(self.cols))
        lines = [header, "   " + "--" * self.cols + "-"]
        for r in range(self.rows):
            row_cells = []
            for c in range(self.cols):
                if reveal_all:
                    if (r,c) in self.mines_set:
                        ch = "*"
                    else:
                        ch = str(self.numbers[r][c]) if self.numbers[r][c] > 0 else " "
                else:
                    if self.flagged[r][c]:
                        ch = "F"
                    elif not self.revealed[r][c]:
                        ch = "#"
                    else:
                        if (r,c) in self.mines_set:
                            ch = "*"
                        else:
                            ch = str(self.numbers[r][c]) if self.numbers[r][c] > 0 else " "
                row_cells.append(f"{ch:2}")
            lines.append(f"{r:2} | " + " ".join(row_cells))
        return "\n".join(lines)


def prompt_int(prompt: str, default: int) -> int:
    try:
        s = input(prompt + f" [{default}]: ").strip()
        if s == "":
            return default
        v = int(s)
        return v
    except Exception:
        print("invalid input, using default")
        return default

def print_help():
    help_text = """
controls:
  r row col    -> reveal cell at (row, col)
  f row col    -> toggle flag at (row, col)
  q            -> quit
  h            -> help

notes:
  - Rows and columns are 0-indexed.
  - Example: 'r 3 5' reveals row 3 column 5.
"""
    print(help_text)


def main():
    print("welcome to bosnia simulator!\n")
    rows = prompt_int("how many rows broski", 9)
    cols = prompt_int("how many columns broski", 9)
    max_mines = rows*cols - 1
    default_mines = min(10, max_mines)
    mines = prompt_int(f"mines? (max {max_mines})", default_mines)
    mines = max(1, min(mines, max_mines))

    board = Board(rows, cols, mines)
    alive = True
    print_help()

    while True:
        print(board.display())
        if board.check_win():
            print("good job at being a good UN minesweeper boy!")
            print(board.display(reveal_all=True))
            break
        if not alive:
            print("you got bosnianed")
            print(board.display(reveal_all=True))
            break

        cmd = input("\nenter command (h for help): ").strip().lower()
        if not cmd:
            continue
        parts = cmd.split()
        if parts[0] == "q":
            print("coward")
            break
        if parts[0] == "h":
            print_help()
            continue
        if parts[0] not in ("r","f"):
            print("shut up")
            continue
        if len(parts) < 3:
            print("not enough arguments. Example: r 3 5")
            continue
        try:
            r = int(parts[1])
            c = int(parts[2])
        except ValueError:
            print("coordinates must be integers.")
            continue

        if parts[0] == "f":
            msg = board.toggle_flag(r,c)
            print(msg)
            continue
        elif parts[0] == "r":
            alive, msg = board.reveal(r,c)
            print(msg)
            continue


if __name__ == "__main__":
    main()

