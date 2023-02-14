## State



- ```javascript
  import logo from './logo.svg';
  import './App.css';
  //State를 쓰기 위해서는 import 해줘야함
  import {useState} from 'react';
  
  function Header(props) {
    return <header>
      <h1><a href="/" onClick={(event)=>{
        event.preventDefault(); //기본동작 방지 => 클릭해도 reload 일어나지 않음
        props.onChangeMode();
      }}>{props.title}</a></h1>
    </header>
  }
  function Nav(props) {
    const lis = []
    for(let i=0; i<props.topics.length; i++){
      let t = props.topics[i];
      lis.push(<li key={t.id}>
        <a id={t.id} href={'/read/'+t.id} onClick={(event)=>{
          event.preventDefault();
          props.onChangeMode(Number(event.target.id)); //event를 발생시키는 target(a태그)의 id
        }}>{t.title}</a>
        </li>)
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
    // const _mode = useState('WELCOME'); //useState는 state의 초기값 
    // console.log('_mode', _mode) => 총 두가지의 값이 나옴
    // const mode = _mode[0]; //상태의 값을 읽을 때 쓰는 데이터
    // const setMode = _mode[1]; //상태의 값을 변경할 때 쓰는 함수
    const [mode, setMode] = useState('WELCOME');
    const [id, setId] = useState(null);
    const topics = [
      {id:1, title:'html', body:'html is ...'},
      {id:2, title:'css', body:'css is ...'},
      {id:3, title:'javascript', body:'javascript is ...'},
    ]
    let content = null;
    if(mode === 'WELCOME') {
      content = <Article title="Welcome" body="Hello, WEB"></Article>
    } else if(mode === 'READ') {
      let title, body = null;
      for(let i=0; i<topics.length; i++) {
        if(topics[i].id == id) {
          title = topics[i].title;
          body = topics[i].body;
        }
      }
      content = <Article title={title} body={body}></Article>
    } 
    return (
      <div className="App">
        <Header title="WEB" onChangeMode={()=>{
          setMode('WELCOME');
        }}></Header>
        <Nav topics={topics} onChangeMode={(id)=>{
          setMode('READ');
          setId(id);
        }}></Nav>
        {content}
      </div>
    );
  }
  
  export default App;
  ```

  