def solution(record):
    answer = []
    records = {}
    for i in record:
        a = i.split(" ")
        if len(a) == 3:
            records[a[1]] = a[2]

    for i in record:
        a = i.split(" ")
        if a[0] == "Enter":
            answer.append(records[a[1]] + "님이 들어왔습니다.")
        elif a[0] == "Leave":
            answer.append(records[a[1]] + "님이 나갔습니다.")
            
    return answer