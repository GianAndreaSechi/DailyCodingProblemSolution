
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(p):
    return p(lambda a, b: a)
def cdr(p):
    return p(lambda a, b: b)

def main():
    v_car = car(cons(3,4))
    v_cdr = cdr(cons(3,4))

    print("car: ", v_car, " - cdr: ", v_cdr)


main()