"""root tests"""

from functions.get_files_info import get_files_info


def tests():
    info = get_files_info("calculator", ".")
    print("Calculator, '.'")
    print(info)
    print()

    info = get_files_info("calculator", "pkg")
    print("Calculator, 'pkg'")
    print(info)
    print()

    info = get_files_info("calculator", "/bin")
    print("Calculator, '/bin'")
    print(info)
    print()

    info = get_files_info("calculator", "../")
    print("Calculator, '../'")
    print(info)
    print()


if __name__ == "__main__":
    tests()
