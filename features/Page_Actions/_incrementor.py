def incrementor(stride: int):
    def f(x: int):
        return stride + x
    return f
