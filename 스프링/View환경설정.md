## View 환경설정

- **Welcome Page 만들기**

  `resources/static/index.html`

  ```html
  //index.html
  
  <!DOCTYPE html>
  <html>
  <head>
      <title>Hello</title>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8 /">
  </head>
  <body>
      Hello
      <a href="/hello">hello</a>
  </body>
  </html>
  ```

- 스프링 부트가 제공하는 Welcome Page 기능

- `static/index.html`을 올려두면 Welcome Page 기능을 제공한다.

  

- **thymeleaf 템플릿 엔진**
  - thymeleaf 공식 사이트 : https://thymeleaf.org/



- `hello.hellospring - Package - hello.hellospring.controller `

- `controller - Java class - HelloController`

  ```java
  //HelloController
  
  package hello.hellospring.controller;
  
  import org.springframework.stereotype.Controller;
  import org.springframework.ui.Model;
  import org.springframework.web.bind.annotation.GetMapping;
  
  @Controller
  public class HelloController {
      
      @GetMapping("hello") //Get 방식으로 hello url과 매칭이 됨. 웹 '/hello'로 들어가면 아래의 메서드를 호출함.
      public String hello(Model model) {
        //스프링이 model을 만들어서 넣어줌.
          model.addAttribute("data", "hello!!"); //이 모델에, key가 'data'이고, value가 'hello!!'인 속성을 추가해줌.
          return "hello"; //resources/templates 의 hello를 반환해줌
      }
  }
  ```

- `resources/templates/hello.html`

  ```html
  //hello.html
  
  <!DOCTYPE html>
  <html xmlns:th="http://www.thymeleaf.org"> //타임리프 템플릿 엔진이 선언되어 있음 => 타임리프 문법 사용 가능
  <head>
      <title>Hello</title>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  </head>
  <body>
      <p th:text="'안녕하세요. ' + ${data}" >안녕하세요. 손님</p>
    //key인 'data'가 가지는 'value'를 출력
  </body>
  </html>
  ```

- 컨트롤러에서 리턴 값으로 문자를 반환하면, viewResolver가 화면을 찾아서 처리한다.

  - `resources:templates/` + {ViewName} + `.html`



- 참고) `spring-boot-devtools` 라이브러리를 추가하면, html 파일을 컴파일만 해주면, 서버 재시작 없이 View 파일 변경이 가능하다.

