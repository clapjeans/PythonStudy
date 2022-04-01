def solution(array,commands):
    answer= []

    cmd_length = len(commands)

    for i in range(cmd_length):




        array_list = array[commands[i][0]-1:commands[i][1]]

        array_list.sort();

        answer.append(array_list[commands[i][2]-1])

    return  answer
