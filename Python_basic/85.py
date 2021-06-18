# 문제가 엄청 길어서 생략

w, h, b = map(int, input().split())

save = format(w*h*b/8/1024/1024, ".2f")
print(save, "MB")