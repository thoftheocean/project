#1
a='1234'
for ge in a:
    for shi in a:
        for bai in a:
            if (ge!=shi)and (ge!=bai) and (shi!=bai):
                a=bai+shi+ge
                print(a)
#2
for ge in range(1,5):
    for shi in range(1,5):
        for shi in range(1,5):
            if ge!=shi and ge!=bai and shi!=bai:
                print(bai,shi,ge)
