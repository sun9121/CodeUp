# 문제가 엄청 길어서 생략

# 헤르츠 h<48000, 저장비트수 b<32, 채널 수c<5, 녹음 시간 s<6000
h, b, c, s = map(int, input().split())

save = format(h*b*c*s/8/1024/1024, ".1f")
print(save, "MB")