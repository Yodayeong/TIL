## CSS 기본 스타일



### 크기 단위

- px(픽셀)

  - 모니터 해상도의 한 화소인 '픽셀' 기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위

- %

  - 백분율 단위

  ```html
  <style>
      .box{
          width: 100px;
          height: 10px;
          background-color: bisque;
      }
      .box2{
          width: 50%;
          height: 10px;
          background-color: red;
      }
  </style>
  
  <body>
  	<div class="box"></div>
      <div class="box2"></div>
  </body>
  
  #px는 고정된 크기이지만, %는 전체 중에서의 비중이므로 화면의 크기가 변하면 크기도 변함.
  ```

- em

  - (바로 위, 부모 요소에 대한) 상속의 영향을 받음

- rem

  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐

  ```html
  #기본 font-size 는 16이다.
  
  <style>
      .em{
          font-size: 2em;
      }
      .rem{
          font-size: 2rem;
      }
  </style>
  
  <body>
  	<h2 class="em">2em</h2> #font-size : 16 * 2 = 32
      <ul class="em">
          <li class="em">2em</li> #font-size: 32 * 2 = 64
      </ul>
      
      <h2 class="rem">2rem</h2> #font-size : 16 * 2 = 32
      <ul class="rem">
          <li class="rem">2rem</li> #font-size : 16 * 2 = 32
      </ul>
  </body>
  ```

  

### 선택자 유형

- 기본 선택자
  - 전체 선택자, 요소 선택자
    - 요소 선택자 : HTML 태그를 직접 선택
  - 클래스 선택자, 아이디 선택자, 속성 선택자
    - 클래스 선택자 : 마침표(.) 문자로 시작하며, 해당 클래스가 적용된 항목을 선택
    - 아이디 선택자 : # 문자로 시작하며, 해당 아이디가 적용된 항목을 선택



### CSS 박스 모델

- 모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.
- Margin : 테두리 바깥의 외부 여백 / 배경색을 지정할 수 없다.
- Border : 테두리 영역
- Padding : 테두리 안쪽의 내부 여백 요소에 적용된 배경색 / 이미지는 padding까지 적용
- Content : 글이나 이미지 등 요소의 실제 내용

```html
<style>
    .box{
        margin: 1rem;
        padding: 1rem;
        background-color: bisque;
        border: 1px solid black;
    }
    .circle{
        width: 5rem;
        height: 5rem;
        background-color: brown;
        border-radius: 50%;
    }
</style>

<body>
    <div class="box">hello</div>
</body>
```



- box model 구성(margin/padding)

  - ```html
    .margin-1{
    	margin: 10px;
    }
    
    #margin-left: 10px;
    #margin-right: 10px;
    #margin-top: 10px;
    #margin-botom: 10px;
    ```

  - ```html
    .margin-2{
    	margin: 10px 20px;
    }
    
    #margin-left: 20px;
    #margin-right: 20px;
    #margin-top: 10px;
    #margin-botom: 10px;
    ```

  - ```html
    .margin-3{
    	margin: 10px 20px 30px;
    }
    
    #margin-left: 20px;
    #margin-right: 20px;
    #margin-top: 10px;
    #margin-botom: 30px;
    ```

  - ```html
    .margin-4{
    	margin: 10px 20px 30px 40px;
    }
    
    #margin-left: 40px;
    #margin-right: 20px;
    #margin-top: 10px;
    #margin-botom: 30px;
    ```



- display에 따라 크기와 배치가 달라진다.
- display: block
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지한다.
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.
- display: inline
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지한다.
  - width, height, margin-top, margin-bottom을 지정할 수 없다.
  - 상하 여백은 line-height로 지정한다.

```html
<style>
    .box{
        margin: 1rem;
        width: 5rem;
        height: 5rem;
        background-color: bisque;
    }
</style>

<body>
    <div class="box"></div>
    <div class="box"></div>
    <div class="box"></div>
    <span class="box"></span>
    <span class="box"></span>
    <span class="box"></span>
</body>
```

