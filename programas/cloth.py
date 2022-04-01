def solution(clothes):
    clothesTypeMap = {}

    for clothe, clothesType in clothes:
        print(clothe)
        print("clothesType:", clothesType)

        # 옷 종류마다 값을 1씩 더하기
        clothesTypeMap[clothesType] = clothesTypeMap.get(clothesType, 0) + 1

        print(clothesTypeMap)

        answer = 1
    for clothesType in clothesTypeMap:
        answer *= (clothesTypeMap[clothesType] + 1)


    return answer - 1
