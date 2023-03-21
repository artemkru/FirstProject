def subsetSumFinder(A, d):
    def backtrack(B, start_idx, sum):
        if sum == d:
            result.append(B[:])
            return
        for i in range(start_idx, len(A)):
            if sum + A[i] > d:
                break
            B.append(A[i])
            backtrack(B, i + 1, sum + A[i])
            B.pop()

    result = []
    backtrack([], 0, 0)
    return result




if __name__ == '__main__':
    print("Enter an array of numbers")
    array = input().split()
    array = [int(num) for num in array]
    sum_array = int(input("Enter sum \n"))
    print(subsetSumFinder(sorted(array), sum_array))


