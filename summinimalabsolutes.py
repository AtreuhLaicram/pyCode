def solution(a):
    slscomp = {}
    for i in range(len(a)):
        sols = []
        for j in a:
            sols.append((abs(a[i]-j)))
        if a[i] not in slscomp.keys():
            slscomp[a[i]] = sum(sols)
    minimal = min(slscomp.values())
    for sm in slscomp.keys():
        if slscomp[sm] == minimal:
            return sm

if __name__ == '__main__':
	a = [2, 4, 7]
	print(solution(a))