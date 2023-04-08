## 회원 관리 예제 - 웹 MVC 개발

<br>

#### 회원 웹 기능 - 홈 화면 추가

- `controller - HomeController`

  ```java
  package hello.hellospring.controller;
  
  import org.springframework.stereotype.Controller;
  import org.springframework.web.bind.annotation.GetMapping;
  
  @Controller
  public class HomeController {
  
      @GetMapping("/") //제일 첫 도메인 화면과 연결
      public String home() {
          return "home"; //home.html이 호출됨
      }
  }
  ```

- `templates - New - File - home.html`

  ```html
  <!DOCTYPE html>
  <html xmlns:th="http://www.thymeleaf.org">
  <body>
  
  <div class="container">
      <div>
          <h1>Hello Spring</h1>
          <p>회원 기능</p>
          <p>
              <a href="/members/new">회원 가입</a>
              <a href="/members">회원 목록</a>
          </p>
      </div>
  </div>
  
  </body>
  </html>
  ```

<br>

#### 회원 웹 기능 - 등록

- `MemberController`

  ```java
  @Controller
  public class MemberController {
    //members:new 추가
      @GetMapping("/members/new")
      public String createForm() {
          return "members/createMemberForm";
      }
  }
  ```

- `templates - New - Directory - members`

- `members - createMemberForm.html`

  ```java
  <!DOCTYPE HTML>
  <html xmlns:th="http://www.thymeleaf.org">
  <body>
  
  <div class="container">
  
      <form action="/members/new" method="post">
          <div class="form-group">
              <label for="name">이름</label>
              <input type="text" id="name" name="name" placeholder="이름을 입력하세요">
          </div>
          <button type="submit">등록</button>
      </form>
  
  </div>
  
  </body>
  </html>
  ```

- `controller - MemberForm`

  ```java
  package hello.hellospring.controller;
  
  public class MemberForm {
      private String name;
  
      public String getName() {
          return name;
      }
  
      public void setName(String name) {
          this.name = name;
      }
  }
  ```

- `MemberController`

  ```java
  @Controller
  public class MemberController {
  
    //PostMapping 추가
      @PostMapping("/members/new")
      public String create(MemberForm form) {
          Member member = new Member();
          member.setName(form.getName());
  
          memberService.join(member);
  
          return "redirect:/";
      }
  }
  ```

- MemberController를 통해 members/new에 접속하면 members:createMemberForm.html로 넘어감

- 이때, createMemberForm.html의 input태그에서 name은 서버로 넘어올 때 key의 역할을 함

- input 값들이 post 방식으로 넘어가면, MemberController의 PostMapping으로 넘어감

- 이때, PostMapping의 create가 받는 MemberForm 객체 form의 name으로 input name 값이 들어감 (setName을 통해)

- form의 getName을 통해 이 name을 꺼내고, 새로운 member를 join함

<br>

#### 회원 웹 기능 - 조회

- `MemberController`

  ```java
  @Controller
  public class MemberController {
  
      @GetMapping("/members")
      public String list(Model model) {
          List<Member> members = memberService.findMembers();
          model.addAttribute("members", members);
          return "members/memberList";
      }
  }
  ```

- `templates - members - New - File - memberList.html`

  ```html
  <!DOCTYPE HTML>
  <html xmlns:th="http://www.thymeleaf.org">
  <body>
  
  <div class="container">
      <div>
          <table>
              <thead>
              <tr>
                  <th>#</th>
                  <th>이름</th>
              </tr>
              </thead>
              <tbody>
              <tr th:each="member : ${members}">  <!--달러 표시는 model 안에서 꺼낸다는 표시-->
                  <td th:text="${member.id}"></td>
                  <td th:text="${member.name}"></td>
              </tr>
              </tbody>
          </table>
      </div>
  </div>
  
  </body>
  </html>
  ```

- model에 addAttribute를 통해 members를 담는다.

- 타임리프를 돌면서, members를 하나씩 member에 담는다.

- member의 id와 name을 출력한다. (getId와 getName을 사용)

<br>

*메모리에 정보가 저장되어 있어서 서버를 끄면 정보가 사라진다!*

