# def good(w, h, a, b, d, n):
#     return (w // (a + d)) * (h // (b + d)) >= n or (w // (b + d)) * (h // (a + d)) >= n
#
#
# n, a, b, w, h = map(int, input().split())
# l = 0
# r = 1
# while not good(w, h, a, b, r, n):
#     r *= 2
# print(r)
# # while r - l > 1:
