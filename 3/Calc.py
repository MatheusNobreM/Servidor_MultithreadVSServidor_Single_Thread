class Calc:
    @staticmethod
    def add(op1: float, op2: float) -> float:
        return op1 + op2

    @staticmethod
    def sub(op1: float, op2: float) -> float:
        return op1 - op2

    @staticmethod
    def mult(op1: float, op2: float) -> float:
        return op1 * op2

    @staticmethod
    def div(op1: float, op2: float) -> float:
        if op2 == 0:
            raise ValueError("Divisão por zero não permitida")
        return op1 / op2
