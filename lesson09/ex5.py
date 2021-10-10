class Stationery:
    def __init__(cls, title):
        cls.title = title

    def draw(self):
        print(f'{self.title} has drawn')


class Pen(Stationery):

    def draw(self):
        print(f'{self.title} has drawn with pen')


class Pencil(Stationery):

    def draw(self):
        print(f'{self.title} has drawn with pencil')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} has drawn with handle')


pen = Pen('Face')
pen.draw()

pen = Pen('Eyes')
pen.draw()

pencil = Pencil('Nose')
pencil.draw()

handle = Handle('Mouth')
handle.draw()
