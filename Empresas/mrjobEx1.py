from mrjob.job import MRJob
from mrjob.step import MRStep

class procesar(MRJob):
# A -> Dia de mayor valor de la accion

    def mapper1(self, _, line):
        enterprise, stock, date = line.split(',')
        yield date, stock

    def reducer1(self, date, values):
        cont = 0
        prom = 0

        for value in values:
            prom+=int(value)
            cont += 1

        yield 1, (prom/cont, date)

    def reducer2(self, date, values):
        max_day = max(values)
        print max_day

    def steps(self):
        return [
           MRStep(mapper=self.mapper1, reducer=self.reducer1), MRStep(reducer=self.reducer2)]

if __name__ == '__main__':
    procesar.run()
