**'리엑트는 사용자 정의 태그를 만드는 기술이다'**



### 컴포넌트(사용자 정의 태그)

- function의 이름은 무조건 대문자로 시작!

- ex) 

  ```javascript
  //App.js
  
  import logo from './logo.svg';
  import './App.css';
  
  function App() {
    return (
      <div className="App">
        <header>
        	<h1><a href="/">React</a></h1>
        </header>
        <nav>
          <ol>
            <li><a href="/read/1">html</a></li>
            <li><a href="/read/2">css</a></li>
            <li><a href="/read/3">js</a></li>
          </ol>
        </nav>
        <article>
          <h2>Welcome</h2>
          Hello, WEB
        </article>
      </div>
    );
  }
  
  export default App;
  ```

  => 이 곳에서 header 부분을 더 효율적인 코드로 바꾸고 싶다면,

  ```javascript
  //App.js
  
  import logo from './logo.svg';
  import './App.css';
  function Header() {
    return <header>
    <h1><a href="/">React</a></h1>
  </header>
  }
  function App() {
    return (
      <div className="App">
        <Header></Header>
        <Header></Header>
        <Header></Header>
        <nav>
          <ol>
            <li><a href="/read/1">html</a></li>
            <li><a href="/read/2">css</a></li>
            <li><a href="/read/3">js</a></li>
          </ol>
        </nav>
        <article>
          <h2>Welcome</h2>
          Hello, WEB
        </article>
      </div>
    );
  }
  
  export default App;
  ```



### props(컴포넌트의 입력값)

- 리엑트는 속성을 prop 이라 부름

- 우리가 만든 컴포넌트에 prop을 장착해보자!

- ex)

  ```javascript
  //App.js
  
  import logo from './logo.svg';
  import './App.css';
  function Header(props) {
    return <header>
      <h1><a href="/">{props.title}</a></h1>
    </header>
  }
  function Nav(props) {
    const lis = []
    for(let i=0; i<props.topics.length; i++){
      let t = props.topics[i];
      lis.push(<li key={t.id}><a href={'/read/'+t.id}>{t.title}</a></li>)
    }
    return <nav>
      <ol>
        {lis}
      </ol>
    </nav>
  }
  function Article(props) {
    return <article>
      <h2>{props.title}</h2>
      {props.body}
    </article>
  }
  function App() {
    const topics = [
      {id:1, title:'html', body:'html is ...'},
      {id:2, title:'css', body:'css is ...'},
      {id:3, title:'javascript', body:'javascript is ...'},
    ]
    return (
      <div className="App">
        <Header title="WEB"></Header>
        <Nav topics={topics}></Nav>
        <Article title="Welcome" body="Hello, WEB"></Article>
      </div>
    );
  }
  
  export default App;
  ```

  => 속성들을 props로 넘겨주고 이를 function 안에서 사용