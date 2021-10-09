
class Stationery:
    def __init__(cls, title):
        cls.title = title
        print(f'{title} project')

    @staticmethod
    def draw(obj, tool):
        print('Start rendering')
        print(f'{tool} has drawn {obj}')


class Pen(Stationery):
    tool = 'Pen'

    def __init__(cls, title):
        super().__init__(title)

    def use_tool(self, obj, tool=tool):
        super().draw(obj, tool)


class Pencil(Stationery):
    tool = 'Pencil'

    def __init__(cls, title):
        super().__init__(title)

    def use_tool(self, obj, tool=tool):
        super().draw(obj, tool)


class Handle(Stationery):
    tool = 'Handle'

    def __init__(cls, title):
        super().__init__(title)

    def use_tool(self, obj, tool=tool):
        super().draw(obj, tool)


print('-' * 100)

pen = Pen('Face')
pen.use_tool('circle')

print('-' * 100)

pen = Pen('Eyes')
pen.use_tool('circle')
pen.use_tool('circle')

print('-' * 100)

pencil = Pencil('Nose')
pencil.use_tool('triangle')

print('-' * 100)

handle = Handle('Mouth')
handle.use_tool('arc')