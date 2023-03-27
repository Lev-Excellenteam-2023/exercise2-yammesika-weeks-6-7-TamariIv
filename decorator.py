from functools import wraps


class IncorrectType(Exception):
    """Raised when the type is incorrect"""
    pass


def type_check(correct_type):
    def compare_type(func):
        @wraps(func)
        def inner(param):
            try:
                if correct_type != type(param):
                    raise IncorrectType
                else:
                    print("correct")
                    func(param)
            except IncorrectType:
                print("Exception occurred: Incorrect type")
        return inner
    return compare_type


@type_check(int)
def times2(num):
    return num * 2


def main():
    times2(2)
    times2('2')
    times2(2.34)


if __name__ == '__main__':
    main()
