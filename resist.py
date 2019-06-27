class Resistance:
    def __init__(self, r):
        self.resistance = r

    def __str__(self):
        return str(self.resistance)


class SeriesCircuit(Resistance):
	def __init__(self, *res):
		self.resistance = sum([r.resistance for r in res])

class ParallelCircuit(Resistance):
    def __init__(self, *res):
        self.resistance = 1.0 / sum([1.0 / r.resistance for r in res])


if __name__ == '__main__':
    R1 = Resistance(10)
    R2 = Resistance(8)
    R_  = SeriesCircuit(R1, R2)
    R3 = Resistance(12)
    print(R_)
    R__ = ParallelCircuit(R_, R3)
    print(R__)