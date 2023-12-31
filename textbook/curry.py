def curry(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry(f):
    def g(x, y):
        return f(x)(y)
    return g
