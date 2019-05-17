# import sys
# import shortuuid
# import time
# u1 = shortuuid.uuid
# u2 = shortuuid.uuid
# inuse = []
# t0 = time.time()
# t1 = time.time()
# n = 1000000
# for x in range(1, n):
#     inuse.append(u1())


# t1 = time.time()
# newones = inuse.copy()
# for y in range(1, 100):
#     f = u2()
#     if not f in inuse:
#         newones.append(f)

# tf = time.time()

# print('Generate', t1 - t0)
# print('Check dupes', tf - t1)
# print('Total', tf-t0)
# print(len(inuse))
# print(len(newones))


from uuidstore import uuidlist
x = uuidlist()
x.CurrentUUID
x.Seed(10)
x.NextUUID()
y = x.NextUUID()
y
