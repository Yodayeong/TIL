## CSS Position

- 문서 상에서 요소의 위치를 지정
- static : 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨



1. relative : 상대위치
   - 자기 자신의 static 위치를 기준으로 이동(normal flow 유지)
2. absolute : 절대위치
   - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)

```html
/*static*/
div{
	height: 100px;
	width: 100px;
}

/*relative*/
.relative{
	position: relative;
	top: 100px;
	left: 100px;
}
=> 기존 위치(normal position) 대비, top, left가 100px offset

/*absolute*/
.parent{
	positon: relative;
}

.absolute-child{
	position: absolute;
	top: 50px;
	left: 50px;
}
=> absolute는 normal flow에서 벗어남. 즉, 다음 블록요소가 좌측 상단으로 붙음.
```

3. fixed : 고정위치
   - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
   - 스크롤 시에도 항상 같은 곳에 위치함



## CSS Layout



### float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜, 텍스트를 포함 인라인요소들이 주변을 wrapping 하도록 함

  ```html
  .left{
  	float: left;
  }
  ```

  

### flexbox

- 축
  - main axis(메인 축)
  - cross asix(교차 축)

- 구성요소

  - flex container(부모 요소)
    - flex item들이 놓여있는 영역
    - display 속성을 flex 혹은 inline-flex로 지정
  - flex item(자식 요소)

  ```html
  #부모 요소에 flex
  .flex-container{
  	display: flex;
  }
  ```

- flex 속성

  - flex-direction
    - main axis 기준 방향 설정
    - | row                | 요소들을 텍스트의 방향과 동일하게 정렬   |
      | ------------------ | ---------------------------------------- |
      | **row-reverse**    | **요소들을 텍스트의 반대 방향으로 정렬** |
      | **column**         | **요소들을 위에서 아래로 정렬**          |
      | **column-reverse** | **요소들을 아래에서 위로 정렬**          |
    
  - flex-wrap
    - 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
    
    - 기본적으로 컨테이너 영역을 벗어나지 않도록 함
    
    - | nowrap           | 모든 요소들을 한 줄에 정렬              |
      | ---------------- | --------------------------------------- |
      | **wrap**         | **요소들을 모든 줄에 걸쳐 정렬**        |
      | **wrap-reverse** | **요소들을 여러 줄에 걸쳐 반대로 정렬** |
    
  - justify-content
    - main axis를 기준으로 공간 배분(row)
    - | flex-start        | 요소들을 컨테이너의 왼쪽으로 정렬       |
      | ----------------- | --------------------------------------- |
      | **flex-end**      | **요소들을 컨테이너의 오른쪽으로 정렬** |
      | **center**        | **요소들을 컨테이너의 가운데로 정렬**   |
      | **space-between** | **요소들 사이에 동일한 간격을 둠**      |
      | **space-around**  | **요소들 주위에 동일한 간격을 둠**      |
    
  - align-items
    - 모든 아이템을 cross axis를 기준으로 정렬(column)
    - | flex-start   | 요소들을 컨테이너의 꼭대기로 정렬                 |
      | ------------ | ------------------------------------------------- |
      | **flex-end** | **요소들을 컨테이너의 바닥으로 정렬**             |
      | **center**   | **요소들을 컨테이너의 세로선 상의 가운데로 정렬** |
      | **baseline** | **요소들을 컨테이너의 시작 위치에 정렬**          |
      | **stretch**  | **요소들을 컨테이너에 맞도록 늘림**               |
    
  - align-content
    
    - 여러 줄 사이의 간격을 지정
    
    - | flex-start        | 여러 줄들을 컨테이너 꼭대기에 정렬        |
      | ----------------- | ----------------------------------------- |
      | **flex-end**      | **여러 줄들을 컨테이너 바닥에 정렬**      |
      | **center**        | **여러 줄들을 세로선 상의 가운데에 정렬** |
      | **space-between** | **여러 줄들 사이에 동일한 간격을 둠**     |
      | **space-around**  | **여러 줄들 주위에 동일한 간격을 둠**     |
      | **stretch**       | **여러 줄들을 컨테이너에 맞도록 늘림**    |
    
  - align-self : 개별 요소에 적용할 수 있는 속성
  
    - 자식요소에 사용 가능
    - align-items가 사용하는 값들을 인자로 받음
  
  - flex-flow
  
    - 공백문자를 이용하여 flex-direction과 flex-wrap의 속성을 대신함
  
  - 기타 속성
  
    - flex-grow : 남은 영역을 아이템에 분배
    
    - order : 배치 순서
    
      

[간단 정리]

1. justify-content : 주축 기준
2. align-items : 보조축 기준
3. align-content : 여러 줄 일때(보조축 )



[활용]

```html
body{
	margin: 0;
}

.nav{
	border: 1px solid black;
	height: 50px;
	position: sticky;
	top: 0
}

.top-btn{
	position: fixed;
	bottom: 1rem;
	right: 1rem;
	border: 1px solid black;
	border-radius: 50%;
	height: 3rem;
	width: 3rem;
}

.section1{
	flex-grow: 1;
}

.section2{
	flex-grow: 4;
}

.section3{
	flex-grow: 1;
}
```
