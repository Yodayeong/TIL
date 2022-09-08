## Grid System(web design)

- 요소들의 디자인과 배치에 도움을 주는 시스템
- 기본요소
  - Column : 실제 컨텐츠를 포함하는 부분
  - Gutter : 칼럼과 칼럼 사이의 공간(사이 간격)
  - Container : Column들을 담고 있는 공간



### Bootstrap Grid System

- Bootstrap Grid System은 flexbox로 제작됨

- container, rows, column으로 컨텐츠를 배치하고 정렬

- 반드시 기억해야 할 2가지

  - 12개의 column
  - 6개의 grid breakpoints

- ```
   .col-xs-* 
   항상 가로로 배치 
  
   .col-sm-*
   768px 이하에서 세로로 표시 시작
  
   .col-md-*
   992px 이하에서 세로로 표시 시작
  
   .col-lg-*
   1200px 이하에서 세로로 표시 시작 
  ```

- ```html
  <div class="container">
      <div class="row">
          <div class="col"></div>
          <div class="col"></div>
          <div class="col"></div>
      </div>
  </div>
  ```