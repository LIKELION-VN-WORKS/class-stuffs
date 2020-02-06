# while + conditionals
# String formatting(문자열 포매팅)


treeHit = 0
while treeHit < 10:
    treeHit += 1 #treeHit = treeHit + 1
    print("나무가 %d번 찍혔습니다." % treeHit) #String formatting(문자열 포매팅 : 문자열 안에 값을 넣고 싶을 경우에 사용)
    if treeHit == 10:
        print("나무 넘어갑니다!!")