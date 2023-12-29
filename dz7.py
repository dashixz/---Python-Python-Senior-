class IterWithGen:
    def __iter__(self):
        return self
    def __next__(self):
        return (x for x in range(5))

iterator = IterWithGen()

for gen in iterator:
    for num in gen:
        print(num)