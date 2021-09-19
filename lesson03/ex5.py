from random import choice,randrange
def get_jokes(n, uniq = False):
    result = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    for i in range(n):
        joke = []
        for ilist in [nouns, adverbs, adjectives]:
            if len(ilist) == 0:
                return result
            if uniq:
                joke.append(ilist.pop(randrange(len(ilist))))
            else:
                joke.append(ilist[randrange(len(ilist))])
        result.append(" ".join(joke))
    return result

print(get_jokes(10,True))