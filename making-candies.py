# https://www.hackerrank.com/challenges/making-candies/problem?isFullScreen=true

def minimumPasses(m, w, p, n):
    # Write your code here
    if n <= p: return math.ceil(n / (m * w))

    curr = candy = 0
    ans = float('inf')

    while candy < n:
        if candy < p:
            i = math.ceil((p - candy) / (m * w))
            curr += i
            candy += m * w * i
            continue

        buy,candy = divmod(candy , p)
        total = m + w + buy
        half = total // 2

        if m > w :
            m = max(m, half)
            w = total - m
        else:
            w = max(w, half)
            m = total - w

        curr += 1
        candy += m * w
        ans = min(ans, curr + math.ceil((n - candy) / (m * w)))

    return min(ans, curr)
