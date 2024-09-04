from collections import deque

def memory(buffer_cap, operations, data):
    que = deque(maxlen=buffer_cap)  # [start, end, 内容]
    for operation in operations:
        if operation[0] == 1:
            que, data = write(operation, data, que, buffer_cap)

        elif operation[0] == 2:
            que, data = read(operation, data, que, buffer_cap)

        else:
            que, data = synchronous(operation, data, que, buffer_cap)

    return data


def write(operation, data, que, buffer_cap):
    start, l, tmp = operation[1], operation[2], operation[3]
    t = l // 8
    r = l % 8
    tmp_16 = hex(tmp)[2:].upper()
    for i in range(t):
        if len(que) == buffer_cap:
            val = que.popleft()
            s = val[2] * (val[1] - val[0])
            data = data[:val[0]*2] + s + data[val[1]*2:]
            que.append([start+8*i, start+8*(i+1), tmp_16])

        else:
            que.append([start + 8 * i, start + 8 * (i+1), tmp_16])

    if len(que) == buffer_cap:
        val = que.popleft()
        s = val[2] * (val[1] - val[0])
        data = data[:val[0] * 2] + s + data[val[1] * 2:]
        que.append([start+l-r, start+l, tmp_16])
    else:
        que.append([start+l-r, start+l, tmp_16])

    return que, data


def read(operation, data, que, buffer_cap):
    start, l = operation[1], operation[2]
    end = start+l
    new_que = que.copy()
    is_coincide = False
    j = 0
    for j in range(len(new_que)-1, -1, -1):
        val = new_que.pop()
        if val[0] <= start <= val[1] or val[0] <= end <= val[1]:
            is_coincide = True
            break

    if is_coincide:
        for i in range(j+1):
            val = que.popleft()
            s = val[2] * (val[1] - val[0])
            data = data[:val[0] * 2] + s + data[val[1] * 2:]
    return que, data


def synchronous(operation, data, que, buffer_cap):
    for i in range(len(que)):
        val = que.popleft()
        s = val[2] * (val[1] - val[0])
        data = data[:val[0] * 2] + s + data[val[1] * 2:]
    return que, data


# b = 4
# o = [[1,1,3,255],
#      [3,0,0,0],
#      [1,2,11,120],
#      [2,11,1,0]
#      ]
# d = "1DA0820000000000000901ABCDEF00"

# b = 5
# o = [[1,35,2,100],
#      [1,0,40,255],
#      [1,11,10,81],
#      [1,16,12,173],
#      [2,16,3,0],
#      [2,0,3,0]
#      ]
# d = "00"*40

# print(memory(b, o, d))