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
- 6. git 주소, 서버의 IP, 도메인은 향후 IP와 연결(호스팅쪽), 리눅스 접속 계정 ID 등 설정 
- 7. requirements.txt : 본 서비스를 구동하기 위해 사용된 모든 파이썬 패키지를 기술한다.

# 구동 
- python3 버전 기반으로 수행
- 운영체계 및 서버 세팅 및 배포, 업테이트 관리 등등을 자동화하는 모듈 => fabric3  
- $ pip3 install fabric3 // 이거 안되면 $ pip install fabric3
- git에 최종 소스 반영 
- fabfile.py에 env.key_filename 부분 env.key_filename = '../hwanheelee.pem'로 바꿔주기 
- terminal 창에 $ fab new_server
- 중간에 y, git로그인 등등이 나올 수 있다
- 브라우저 가동 
- 52.79.250.132 접속
- 접속로그 확인(리눅스에서 진행)
- $ tail -f /var/apache2/access.log  # 크롬창에서 새로고침 누르면 cmd 에 업데이트 된 기록 뜸 
- 모니터링하다가
- 빠져나가기 -> ctrl + c
- 에러로그
- $ tail -f /var/apache2/error.log 


# 이후 작업 
- 코드 수정
- git 최신 반영
- 서버 업데이트
    $ fab deploy



# 잘 안된다!
- 소스 코드 상에 파일명, 설정값 등 오타가 없어야함 
- git에 최종 소스가 모두 반영되어야함 
- 리눅스에서 기존의 흔적을 모두 제거
    현재 위치 : /home/ubuntu
    프로젝트 삭제 : $ rm -r -f deploy 
    숨김 파일 확인 : $ ls -a  
    가상환경 삭제 : $ rm -r -f .virtualenvs 
    로컬 PC
    $ fab new_server 

# 가상 호스트가 설정된 부분
- deploy는 프로젝트명 (deploy.json)
- /etc/apache2/site-available/deploy.conf
- 파일 읽기
    $ cat /etc/apache2/sites-available/deploy.conf 
    


