from sudoku import Sudoku

HOST = 'challenges.ringzer0team.com'
PORT = '10143'
USER = "sudoku"
PASS = "dg43zz6R0E"

def parse_sudoku(plain_text):
    result = []
    lines = plain_text.split("\n")
    lines = lines[1::2]

    for line in lines:
        res_line = []
        for num in line.split("|"):
            if num == " " * 3:
                res_line.append(0)
            elif num.strip().isdigit():
                num_ = int(num.strip())
                res_line.append(num_)
        result.append(res_line)
    return result

def main():
    board = ""
    board = parse_sudoku(board)
    puzzle = Sudoku(3, 3, board=board)
    solution = puzzle.solve().board
    answer = []
    for line in solution:
        line_ = map(str, line)
        answer.append(",".join(line_))
    answer = ",".join(answer)    

    print(answer)



if __name__ == "__main__":
    main()
