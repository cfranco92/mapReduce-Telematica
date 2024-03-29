from mrjob.job import MRJob
from mrjob.step import MRStep

class procesar(MRJob):
# D -> Numero de usuarios que ven una misma pelicula y rating promedio

    def mapper1(self, _, line):
        user_id,movie_id,rating,genre,date = line.split(',')
        yield movie_id, (1, rating)

    def reducer1(self, movie_id, values):
        usersCont = 0
        rating = 0

        for value in values:
            rating+=int(value[1])
            usersCont += 1

        yield movie_id, (usersCont, rating/usersCont)

    def steps(self):
        return [
           MRStep(mapper=self.mapper1, reducer=self.reducer1)]

if __name__ == '__main__':
    procesar.run()
