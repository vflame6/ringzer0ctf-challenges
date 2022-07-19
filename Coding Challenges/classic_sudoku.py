import os
import pty
from sudoku import Sudoku

HOST = 'challenges.ringzer0team.com'
PORT = '10143'
USER = "sudoku"
PASS = "dg43zz6R0E"
ssh_command = [
    "/usr/bin/sshpass",
    "-p",
    PASS,
    "ssh",
    "-p",
    PORT,
    f"{USER}@{HOST}",
]

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
    pid, child_fd = pty.fork()

    if not pid:
        os.execv(ssh_command[0], ssh_command)

    # Skip pty message
    output = os.read(child_fd, 1024)

    raw_challenge = os.read(child_fd, 1024).decode()
    challenge = "\n".join(raw_challenge.split("\n")[3:22])

    board = parse_sudoku(challenge)
    puzzle = Sudoku(3, 3, board=board)
    solution = puzzle.solve().board
    answer = []
    for line in solution:
        line_ = map(str, line)
        answer.append(",".join(line_))
    answer = ",".join(answer) + "\n"   

    os.write(child_fd, answer.encode())
    # Skip our written answer
    os.read(child_fd, 1024)

    flag = os.read(child_fd, 1024).decode()
    print(flag)



if __name__ == "__main__":
    main()
