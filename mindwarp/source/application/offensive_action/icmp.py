import sys
from ping3 import ping, verbose_ping



def main():
    print("ICMP ping")
    print("=========")
    verbose_ping("10.0.0.175")
    print("\n")


if __name__ == "__main__":
    sys.exit(main())

