def solution(citations):

    print(citations)
    print(type(citations))
    citations.sort(revers=True)

    print(citations)





    for idx, citation in enumerate(citations):

        print("idx :",idx)
        print("citation :",citation)


        if idx>= citation:
            return idx

    return  len(citations)