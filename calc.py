#!/usr/bin/env python3

import re
import sys
import readline
from typing import Optional, Match, List


def main(argc: int, argv: List[str]) -> None:
    try:
        user_input = " ".join(argv[1:])
        user_input = user_input.strip()
        pattern: str = "\({0,}\s{0,}-{0,1}\d{1,}\.*\d{0,}\s{0,}[<>\+\-\*/%]{1,2}\s{0,}-{0,1}\d{1,}\.*\d{0,}\s{0,}\){0,}(\s{0,}[<>\+\-\*/%]{1,2}\s{0,}\({0,}\s{0,}-{0,1}\d{1,}\.*\d{0,}\){0,}\s{0,}){0,}"
        match_object: Optional[Match[str]] = re.match(pattern, user_input)
        if match_object is not None and  match_object.group() == user_input:
            print(eval(user_input))
        else:
            print("Sums not recognized")
    except SyntaxError:
        print("Syntax error")
    except ZeroDivisionError:
        print("Zero division not allow")


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
