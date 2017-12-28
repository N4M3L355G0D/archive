import string

charset=str(string.printable).replace('\v','').replace('\f','').replace('\t','').replace('\r','').replace('\n','')


def letters(insert=""):
    for i in range(len(insert)):
        yield insert[i]
        for h in letters(insert[:i]+insert[i+1:]):
            yield (insert[i]+h)

def status(sta=""):
    for i in range(len(sta)): ## get str len
        yield sta[i]
        for h in status(sta[:i] + sta[i+1:]):
                yield(sta[i] +h)
