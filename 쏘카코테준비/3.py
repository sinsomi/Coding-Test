def solution(r, delivery):
    visited = [[0 for _ in range(r)] for _ in range(r)]
    # convert to matrix
    delivery_matrix = []
    pre_matrix = []
    for i in range(r*r):
        pre_matrix.append(delivery[i])
        if len(pre_matrix)%r == 0:
            delivery_matrix.append(pre_matrix)
            pre_matrix = []