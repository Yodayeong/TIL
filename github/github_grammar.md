# 🎄GitHub

- 원격저장소(Remote Repository)

  : 네트워크를 활용한 저장소

- 버전(커밋)을 관리함

  : 절대 파일 관리가 아님!



## *원격저장소 기본 흐름

- **$ git push**

  : 로컬저장소의 버전(커밋)을 원격저장소로 보낸다.

- **$ git pull**

  : 원격저장소의 버전(커밋)을 로컬저장소로 가져온다.



## *원격저장소 경로 설정

- 원격저장소 정보를 로컬저장소에 추가
- 로컬저장소에는 한번만 설정 해주면 된다.

**🦴 $ git remote(원격저장소) add(추가해) origin(이름으로) https://github.com/yodayeong(유저네임)/test.git(저장소 이름)**

​         

## *원격저장소 정보 확인

원격저장소의 정보를 확인함

🦴 **$ git remote -v**



## *원격저장소 활용 명령어

### $ git push <원격저장소이름> <브랜치이름>

- 원격저장소로 로컬저장소 변경 사항(커밋)을 올림
- 로컬 폴더의 파일/폴더가 아닌 저장소의 버전(커밋)이 올라감

**🦴 $ git push origin master**



## *원격저장소에 업로드

1. GitHub    ->    +    ->    New Repository
2. Create Repository
3. git 설정 ($ git config --global core.editor "code --wait")
4. git으로 버전정리
5. git에 원격저장소 경로 설정
6. git에 push 해주기



## *gitignore

숨기고 싶은 파일/폴더 ... 