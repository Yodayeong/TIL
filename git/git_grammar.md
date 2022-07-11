# 🎄GIT(분산 버전 관리 시스템)

<u>버전 관리?</u>

- '컴퓨터 소프트웨어의 특정 상태'를 관리 하겠다. (동일한 정보에 대해 여러 버전으로 관리)

- 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율



## 기본흐름

Git은 파일을 modified, staged, committed로 관리



✔ **작업을 하고**

-working directory

✔ **변경된 파일을 모아** ($ git add) 

-staging area라는 중간 공간으로

-내가 버전으로 기록하기 위한 파일들을 staging area에 모음

✔ **버전으로 남긴다.** ($ git commit)

-repository



## 기본 명령어

### 👌 git init

저장소를 처음 생성

### 👌 $ git add <파일명>

working directory상의 변경 내용을 staging area에 추가하기 위해 사용

- untracked 상태의 파일을 staged로 변경
- modified 상태의 파일을 staged로 변경

($ git add . : 모든 파일을 add)

### 👌 $ git commit -m '<커밋메시지>'

staged 상태의 파일들을 커미을 통해 버전으로 기록

- Git은 데이터를 파일 시스템의 스냅샷으로 관리

### 👌 $ git log

현재 저장소에 기록된 커밋(버전)을 조회

- 다양한 옵션을 통해 로그를 조회할 수 있음
  - $ git log -1 : 최근의 하나의 커밋을 보여줘.
  - $ git log --oneline : 한줄로 보여줘.
  - $ git log -2 --oneline : 최근 두개를 한줄로 보여줘.

### 👌 $ git status

Git 저장소에 있는 파일의 상태를 확인하기 위하여 활용

- 파일의 상태를 알 수 있음
  - Untracked files
  - Changes not staged for commit
  - Changed to be committed



## 간단정리

**<u>저장소 처음 만들때</u>** 

$ git init 

**<u>버전을 기록할 때</u>** 

$ git add . 

$ git commit -m '커밋메시지' 

**<u>상태 확인할 때</u>** 

$ git status : 1통, 2통 

$ git log : 커밋 확인



## Git Status

### a.txt 파일을 만든 직후

```bash
$ git status
On branch master

# 트래킹이 되고 있지 않은 파일?
# => 1통 (working directory)
# => 한번도 git으로 관리되고 있지 않은 파일!
Untracked files:
# git add 사용해봐...
# 포함시키기 위해서 / 커밋이 될 것 => 2통에 넣으려면
	(use "git add <file>..." to include in what will be committed)
		a.txt
			
# 커밋할 것은 없어 => 2통이 비어있어
# 하지만(but) 트래킹되지 않은 파일은 존재한다.
# (git add 사용해서 트래킹해)
nothing added to commit but untracked files present (use "git add" to track)
```

### b.txt 파일을 만들고 add한 이후

> 초록 글씨 => 2통

```bash
$ git status
On branch master
# (커밋될) 변경사항들 => 2통
Changes to be committed:
	(use "git resotre --staged <file>..." to unstage)
		#새로운 파일: b.txt
		new file:	b.txt

Untracked files:
	(use "git add <file>" to include in what will be committed)
		a.txt
```

### a.txt 파일과 b.txt 파일을 모두 add한 이후 커밋까지

```bash
$ git status
On branch master
# 2통, 1통 모두 클린~!
nothing to commit, working tree clean
```

