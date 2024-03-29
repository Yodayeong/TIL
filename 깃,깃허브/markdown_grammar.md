# 🎄마크다운

## 제목/소제목 (Heading)

#의 개수에 따라 h1 ~ h6까지 표현 가능하다.

### h3

#### h4

##### h5

###### h6

## 목록 (List)

목록 활용시 단계를 tab과 shift + tab으로 조절한다.

### 순서가 없는 리스트 : -, \*

- 사과

- 바나나

  - 미니 바나나
  - Dole 바나나

- 딸기

  - 산딸기

- 복숭아

  - 백도 복숭아

  - 천도 복숭아

### 순서가 있는 리스트 : 1.

아침에 일어나서 KDT 교육 듣기

    1. 세수하고 양치
    2. 산책
    3. Syllaverse 홈페이지 접속한다.
    	1. 로그인
    	2. 대시보드 확인
    4. 유튜브 라이브에 접속한다.
    	1. 인사를 남긴다.

## 코드 블록

### Fenced Code Block

- `(backtick) 기호 3개를 활용하여 작성한다.
- 특정 언어를 명시하면 Syntax highlighting 기능이 적용된다.

```python
print('hello')

if True:
    print('t')
else
	print('f')
# 주석
```

```html
print('hello') # 주석?
<h1>제목</h1>
<!-- 주석 -->
```

### Inline Code Block

`(backtick) 기호 1개를 활용하여 작성한다.

`print` 는 파이썬에서 출력하는 함수이다.

## 링크

`[문자열](url)` 을 통해 링크를 작성 가능

[네이버](www.naver.com)

## 이미지

- `![문자열](url)` 을 통해 작성 가능 / 이미지 그냥 끌어오기

- 절대경로 (C 드라이브 ~)는 이미지가 나오지 않음

- 상대경로는 마크다운.assets 폴더를 같이 공유하면 이미지가 나옴

![루피](https://postfiles.pstatic.net/MjAyMTA4MTFfMzkg/MDAxNjI4NjY1NjgwNTUw.K2a44KxCgskoaKSw8cH5ySnsEuadVA8wphcrBOrDwBQg.R4GfkzCRdTa1jdicp9p4Ph8A4THJ8tX1mZO-uTqzgygg.JPEG.bbekimha/%EB%A3%A8%ED%94%BC.jpg?type=w966)

## 인용문

`>`를 통해 인용문을 작성

> We live only once.

## 표

타이포라 기능을 적극 활용하자.

본문 > 표 > 표 삽입 (ctrl + t)

| 이름 | 댓글                               |
| ---- | ---------------------------------- |
| 다영 | 노션이랑 비슷하네요                |
| 요다 | 빨간색 노란색 프로그램 무엇인가요? |

## 텍스트 강조

**굵게(볼드체)** : `**`

_기울림(이탤릭체)_ : `*`

~~취소선~~ : `~~`

❤이모지 : `window + .`

수평선 : `---`

---
