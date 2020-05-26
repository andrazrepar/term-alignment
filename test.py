import math

len_src = 59295
len_tar = 6117

ceil_src = int(math.ceil(len_src / 100))
ceil_tar = int(math.ceil(len_tar / 100))
#print('ceil_tar', ceil_tar)
c = 0
for i in range(1, ceil_src + 1):
    for j in range(1, ceil_tar + 1):
        for src_term in range((i-1) * 100, i * 100):
            for tar_term in range((j-1) * 100, j * 100):
                c = c + 1

print(c)
