def solution(numbers):


    #초기 데이터 타입
    print(type(numbers)) #List 구조
    print(type(numbers[0])) #List<int> 구조

    #List안의 값을 String타입으로 변경하기
    #List<ing> => List<String>
    #str => 문자열  (String 타입으로 변경해주는함수
    #list => Lis 구조를 만들어주는함수
    numbers = list(map(str,numbers))

    # 변경된 데이터 타입 조회하기
    print(type(numbers)) #List 구조
    print(type(numbers[0])) # List<String>  구조


    #람다를 이용하여 정렬 numbers 변수에 들ㅇ거나느 숫자는 최대 1000RKwldlamfh
    #정렬을 위한 반복횟누는 최대 3자리 수로 맞춤
    #내림차순을 위해 revers=True
    numbers.sort(key=lambda x:x*3,reverse=True)
    return str(int(''.join(numbers)))