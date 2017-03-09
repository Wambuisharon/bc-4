class BinarySearch(list):
    length = 0

    def __init__(self, a, b):
        super(BinarySearch, self).__init__()
        self.length = a
        number = b
        while number <= a * b:
            self.append(number)
            number += b

    def search(self, number):
        count = 0

        element = self

        while len(element) > 1:
            count += 1
            half = len(element) / 2

            if number == element[half]:
              
                element = []
            elif number > element[half - 1]:
                element = element[half:len(element) - 1]
              
            else:
                element = element[0:half]
              
        try:
            index = self.index(number)
        except ValueError:
            index = - 1
        return {'count': count, 'index': index}