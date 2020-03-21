import sys


def get_pages(first_page, last_page, pages_on_sheet=1):
    divider = pages_on_sheet * 2

    even = []
    not_even = []

    for i in range(first_page, last_page + 1):
        for rest in range(pages_on_sheet + 1, pages_on_sheet * 2 + 1):
            rest = rest % divider
            if i % divider == rest:
                even.append(str(i))
    for i in range(first_page, last_page + 1):
        for rest in range(1, pages_on_sheet + 1):
            rest = rest % divider
            if i % divider == rest:
                not_even.append(str(i))

    return even, not_even

def main():
    if len(sys.argv) < 3:
        print("Generates page numbers to insert in printing screen when double sided.")
        print("Arguments:")
        print("  first_page")
        print("  last_page")
        print("  pages_on_sheet = 1")
        sys.exit()

    first_page = int(sys.argv[1])
    last_page = int(sys.argv[2])
    pages_on_sheet = 1
    try:
        pages_on_sheet = int(sys.argv[3])
    except IndexError:
        pages_on_sheet = 1

    even, not_even = get_pages(first_page, last_page, pages_on_sheet)

    print(",".join(even))
    print(",".join(not_even))

if __name__ == "__main__":
    main()
