import os

# Text Colors
NC = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'


def clear_screen():
    match os.name:
        case "nt":
            return os.system("cls")
        case "posix":
            return os.system("clear")


def get_positive_integer_input(prompt):
    while True:
        str_input = input(prompt)

        try:
            int_input = int(str_input)

            if int_input <= 0:
                print(f"{RED}Error: {NC}Positive input required")
                print("Press Enter to continue...")
                clear_screen()

            else:
                return int_input

        except ValueError:
            print("{RED}Error: {NC}Integer input required")
            print("Press Enter to continue...")
            clear_screen()


def main():
    total_btc = get_positive_integer_input("Total BTC: ")
    mtc_price = get_positive_integer_input("MTC price (BTC): ")
    purchasable_mtc = total_btc // mtc_price

    if purchasable_mtc < 5:
        raise SystemExit(
            f"{RED}Error: {NC}Minimum purchase of 5 MTC required")

    print("Calculating...")

    best = None
    for mtc in range(5, purchasable_mtc + 1):
        tsc = (mtc * 6) // 5
        ts = tsc * 1000
        op = ts // 100
        fanny = op // 10
        dora = fanny // 15
        eoc = dora // 20

        tsc_cost = tsc * 5000
        op_cost = op * 500
        fanny_cost = fanny * 5000
        dora_cost = dora * 5000
        eoc_cost = eoc * 50_000
        total_cost = tsc_cost + op_cost + fanny_cost + dora_cost + eoc_cost

        saved_max = total_btc - mtc * mtc_price
        saved_min = total_btc - (mtc + 1) * mtc_price + 1

        if saved_min < 0:
            saved_min = 0

        required_saved = max(total_cost, saved_min)

        if best is not None and required_saved > best[0]:
            break

        if required_saved <= saved_max:
            if best is None or required_saved < best[0]:
                best = (required_saved, mtc, tsc, ts, op, fanny, dora, eoc, tsc_cost,
                        op_cost, fanny_cost, dora_cost, eoc_cost, total_cost)

    if not best:
        raise SystemExit(f"{RED}Error: {NC}No match found")

    (required_saved, mtc, tsc, ts, op, fanny, dora, eoc, tsc_cost,
     op_cost, fanny_cost, dora_cost, eoc_cost, total_cost) = best

    print(f"{GREEN}Match found!{NC}")
    print(f"MTC: {mtc:,}")
    print(f"TSC: {tsc:,}")
    print(f"TS: {ts:,}")
    print(f"OP: {op:,} ({op_cost:,} BTC)")
    print(f"Fanny: {fanny:,} ({fanny_cost:,} BTC)")
    print(f"Dora: {dora:,} ({dora_cost:,} BTC)")
    print(f"EOC: {eoc:,} ({eoc_cost:,} BTC)")
    print(f"Total cost: {total_cost:,} BTC")


if __name__ == "__main__":
    main()
