def nor(a, b):
    return int(not (a or b))


def nand(a, b):
    return int(not (a and b))


def exit_check(inputs, prev_states):
    values = tuple([inputs[k] for k in inputs])
    inputs_str = "".join(f"{k}: {v},\t" for k, v in inputs.items())[:-2]
    if values == prev_states[-1]:
        print("✔ Stable state reached")
        return True
    elif values in prev_states:
        for i in range(len(prev_states)):
            if prev_states[i] == values:
                print(f"✗ Cycle detected: {inputs_str}")
                return True
        return True
    else:
        return False


# And-Nor Gates
def and_nor_loop(x=1, y=1):
    print("***And-Nor Circuit w/ Loop***")
    prev_states = [(x, y)]
    for i in range(5):
        print(f"time: {i},\tx: {x},\ty: {y}")

        x, y = y & 1, nor(x, 0)

        if exit_check({"x": x, "y": y}, prev_states):
            break

        prev_states.append((x, y))


def sr_latch(r, s, q=1, qc=0):
    print(f"***SR Latch: s={s}, r={r}, q={q}, qc={qc}***")
    prev_states = [(q, qc)]
    for i in range(100):
        print(f"time: {i},\tq: {q},\tqc: {qc}")
        q, qc = nor(r, qc), nor(s, q)

        if exit_check({"q": q, "qc": qc}, prev_states):
            break

        prev_states.append((q, qc))


def sr_nand_latch(a, b, q=1, qc=0):
    print(f"***SR NAND Latch: a={a}, b={b}, q={q}, qc={qc}***")
    prev_states = [(q, qc)]
    for i in range(100):
        print(f"time: {i},\tq: {q},\tqc: {qc}")
        q, qc = nand(a, qc), nand(b, q)

        if exit_check({"q": q, "qc": qc}, prev_states):
            break

        prev_states.append((q, qc))


def nand_nor_latch(a, b, q=1, qc=0):
    print(f"***NAND-NOR Latch: a={a}, b={b}, q={q}, qc={qc}***")
    prev_states = [(q, qc)]
    for i in range(100):
        print(f"time: {i},\tq: {q},\tqc: {qc}")
        q, qc = nand(a, qc), nor(b, q)

        if exit_check({"q": q, "qc": qc}, prev_states):
            break

        prev_states.append((q, qc))


def gated_d_latch(d, e, q=1, qc=0):
    print(f"***Gated D-Latch: d={d}, e={e}, q={q}, qc={qc}***")
    prev_states = [(q, qc)]
    for i in range(100):
        print(f"time: {i},\tq: {q},\tqc: {qc}")
        q, qc = nor(int(not d) & e, qc), nor(d & e, q)

        if exit_check({"q": q, "qc": qc}, prev_states):
            break

        prev_states.append((q, qc))


def enumerate_sr_latch():
    for r, s in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        print(f"Enumerating: s={s}, r={r}")
        for q, qc in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            sr_latch(r, s, q, qc)
            print()


def enumerate_sr_nand_latch():
    for a, b in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        print(f"Enumerating: a={a}, b={b}")
        for q, qc in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            sr_nand_latch(a, b, q, qc)
            print()


def enumerate_gated_d_latch():
    for d, e in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        print(f"Enumerating: d={d}, e={e}")
        for q, qc in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            gated_d_latch(d, e, q, qc)
            print()


def enumerate_nand_nor_latch():
    for a, b in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        print(f"Enumerating: a={a}, b={b}")
        for q, qc in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            nand_nor_latch(a, b, q, qc)
            print()


if __name__ == "__main__":
    # and_nor_loop()
    # print('\n')
    # enumerate_sr_latch()
    # print('\n')
    # enumerate_gated_d_latch()
    # enumerate_sr_nand_latch()
    enumerate_nand_nor_latch()
