#!/usr/bin/env python3
# Created by: Joyceline
# Created on: Sept 26 2026
# This program calculates the circumference of a circle using TAU.

import constants


def main():
    # input
    radius = float(input("Enter the radius of the circle (mm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("")
    print("Circumference is {} mm.".format(circumference))
    print("\nDone.")


if __name__ == "__main__":
    main()
