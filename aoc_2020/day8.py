from typing import List, Tuple

Cmd = Tuple[str, int]


def parse_data(data: str) -> List[Cmd]:
    lines = []
    for line in data.splitlines():
        parts = line.split(" ")

        op = parts[0]
        sign = parts[1][0]
        inc = int(parts[1][1:])

        lines.append((op, inc if sign == "+" else -inc))

    return lines


def run_command(command: Cmd, acc: int, ln: int) -> Tuple[int, int]:
    cmd, inc = command
    if cmd == "acc":
        acc += inc
        ln += 1
    elif cmd == "jmp":
        ln += inc
    else:
        ln += 1

    return acc, ln


def run_prog(prog: List[Cmd]) -> Tuple[int, int, int]:
    proc_lines = []
    ln = 0
    acc = 0
    while True:
        if ln in proc_lines:
            return acc, ln, 0
        elif ln > len(prog) - 1:
            return acc, ln, 1

        proc_lines.append(ln)
        acc, ln = run_command(prog[ln], acc, ln)

    return acc, ln, 2


def part1(data: str) -> Tuple[int, int]:
    print("Running day 8 part 1")

    cmds = parse_data(data)
    acc, ln, out = run_prog(cmds)

    print(acc)
    return acc, out


def switch_cmd(cmd: Cmd) -> Cmd:
    if cmd[0] == "nop":
        return ("jmp", cmd[1])
    elif cmd[0] == "jmp":
        return ("nop", cmd[1])
    else:
        return cmd


def part2(data: str) -> Tuple[int, int]:
    print("Running day 8 part 2")

    cmds = parse_data(data)
    out = 0
    for i, cmd in enumerate(cmds):
        if cmd[0] in ["nop", "jmp"]:
            cmds[i] = switch_cmd(cmds[i])
        acc, ln, out = run_prog(cmds)

        if out == 1:
            break
        else:
            cmds[i] = switch_cmd(cmds[i])

    print(acc)
    return acc, out
