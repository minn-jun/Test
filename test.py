print('hello world!')
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} X {j} = {i*j}")



# github experinece ++

# git status

# git add .   # 전체를 업로드
# or
# git add file/temp.py  # 원하는 파일만 업로드

# git commit -m "first commit"

# git push origin main

# ----------------------------

# git log   # commit 로그 확인

# git reset --hard HEAD^  # 가장 최근 commit 로그 삭제
# git reset --hard HEAD~n  # n 만큼 최근 commit 로그 삭제

# git push -f origin master  # -f 를 이용해서 혹시 모를 충돌방지. 강제 업데이트