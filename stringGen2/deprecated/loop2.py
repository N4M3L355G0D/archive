def p(c,*r):
      for y in(r and p(*r)or[[]]):
             for x in c:yield[x]+y
