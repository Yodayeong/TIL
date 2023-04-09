## AOP

<br>

#### AOP가 필요한 상황

- 모든 메소드의 호출 시간을 측정하고 싶다면?
- 공통 관심 사항(cross-cutting concern) vs 핵심 관심 사항(core concern)
- 회원 가입 시간, 회원 조회 시간을 측정하고 싶다면?

<br>

- ex) `MemberService`

  ```java
  @Transactional
  public class MemberService {
  
      /* 회원가입 */
      public Long join(Member member) {
  
          long start = System.currentTimeMillis();
  
          try {
              validateDuplicateMember(member); //중복 회원 검증
              memberRepository.save(member);
              return member.getId();
          } finally {
              long finish = System.currentTimeMillis();
              long timeMs = finish - start;
              System.out.println("join = " + timeMs + "ms");
          }
      }
  
  }
  ```

<br>

​	문제

- 회원가입, 회원조회에 시간을 측정하는 기능은 핵심 관심 사항이 아니다.
- 시간을 측정하는 로직은 공통 관심 사항이다.
- 시간을 측정하는 로직과 핵심 비즈니스의 로직이 섞여서 유지보수가 어렵다.
- 시간을 측정하는 로직을 별도의 공통 로직으로 만들기 매우 어렵다.
- 시간을 측정하는 로직을 변경할 때 모든 로직을 찾아가면서 변경해야 한다.

<br>

#### AOP 적용

- AOP: Aspect Oriented Programming
- 공통 관심 사항(cross-cutting concern) vs 핵심 관심 사항(core concern) 분리
- TimeTraceAop(시간 측정 로직)을 한군데 다 모으고, helloController, memberService, memberRepository 등 원하는 곳에 공통 관심 사항 적용

<br>

- `hello.hellospring - New - Package - hello.hellospring.aop`

- `aop - New - Java Class - TimeTraceAop`

- TimeTraceAop 생성

  ```java
  package hello.hellospring.aop;
  
  import org.aspectj.lang.ProceedingJoinPoint;
  import org.aspectj.lang.annotation.Aspect;
  
  @Aspect
  public class TimeTraceAop {
      
      public Object execute(ProceedingJoinPoint joinPoint) throws Throwable {
          long start = System.currentTimeMillis();
          System.out.println("START: " + joinPoint.toString());
          try {
  //            Object result = joinPoint.proceed(); //다음 메소드 진행
  //            return result;
              //(control + t) => Inline Variable
              return joinPoint.proceed();
          } finally {
              long finish = System.currentTimeMillis();
              long timeMs = finish - start;
              System.out.println("END: " + joinPoint.toString() + " " + timeMs + "ms");
          }
      }
  }
  ```

- 스프링 빈에 등록하거나 (`SpringConfig`)

  ```java
  @Configuration
  public class SpringConfig {
  
      @Bean
      public TimeTraceAop timeTraceAop() {
          return new TimeTraceAop();
      }
  ```

- 컴포넌트 스캔 사용 (`TimeTraceAop`)

  ```java
  @Aspect
  @Component //Component 추가해주기
  public class TimeTraceAop {
  ...
  }
  ```

- `TimeTraceAop`

  ```java
  package hello.hellospring.aop;
  
  import org.aspectj.lang.ProceedingJoinPoint;
  import org.aspectj.lang.annotation.Around;
  import org.aspectj.lang.annotation.Aspect;
  import org.springframework.stereotype.Component;
  
  @Aspect
  @Component
  public class TimeTraceAop {
  
      @Around("execution(* hello.hellospring..*(..))") //어디에 적용할건지 => hello.hellospring 하위에 모두 적용
      public Object execute(ProceedingJoinPoint joinPoint) throws Throwable {
          long start = System.currentTimeMillis();
          System.out.println("START: " + joinPoint.toString());
          try {
  //            Object result = joinPoint.proceed(); //다음 메소드 진행
  //            return result;
              //(control + t) => Inline Variable
              return joinPoint.proceed();
          } finally {
              long finish = System.currentTimeMillis();
              long timeMs = finish - start;
              System.out.println("END: " + joinPoint.toString() + " " + timeMs + "ms");
          }
      }
  }
  ```

- 그리고, MemberService에 추가해주었던 시간 측정 로직을 지워준다.

<br>

- 해결
- 회원가입, 회원조회 등 핵심 관심사항과 시간을 측정하는 공통 관심 사항을 분리한다.
- 시간을 측정하는 로직을 별도의 공통 로직으로 만들었다.
- 핵심 관심 사항을 깔끔하게 유지할 수 있다.
- 변경이 필요하면 이 로직만 변경하면 된다.
- 원하는 적용 대상을 선택할 수 있다.