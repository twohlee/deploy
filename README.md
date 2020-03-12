# deploy
deploy

# 세팅 절차 
- 1. git에 새로운 저장소 생성
-    https://github.com/아이디/deploy
- 2. 로컬 PC에서 aws 폴더를 vscode에 오픈
- 3. terminal 오픈
- 4. $git clone https://github.com/twohlee/deploy.git
- 5. cd deploy 


# 파일 세팅(~/aws/deploy)
- 1. fabfile.py, deploy.json 파일을 위치
- 2. 서버 파일 생성 
- 3. wsgi.py(엔트리포인트), run.py 생성 
- 4. wsgi.py와 run.py 에 코드 작성
- 5. 배포 관련 환경변수 파일 수정(deploy.json)
