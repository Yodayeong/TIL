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
function Create(props) {
  return <article>
    <h2>Create</h2>
    <form onSubmit={(event)=>{
      //form 태그는 submit을 하면, 페이지가 reload됨
      event.preventDefault();
      //form태그의 title과 body의 value값을 props를 통해
      //onCreate함수로 넘겨준다.
      const title = event.target.title.value;
      const body = event.target.body.value;
      props.onCreate(title, body);
    }}>
      <p><input type="text" name="title" placeholder="title"/></p>
      <p><textarea name="body" placeholder="body"></textarea></p>
      <p><input type="submit" value="Create"></input></p>
    </form>
  </article>
}
function App() {
  // const _mode = useState('WELCOME'); //useState는 state의 초기값 
  // console.log('_mode', _mode) => 총 두가지의 값이 나옴
  // const mode = _mode[0]; //상태의 값을 읽을 때 쓰는 데이터
  // const setMode = _mode[1]; //상태의 값을 변경할 때 쓰는 함수
  const [mode, setMode] = useState('WELCOME');
  const [id, setId] = useState(null);
  const [nextId, setNextId] = useState(4);
  const [topics, setTopics] = useState([
    {id:1, title:'html', body:'html is ...'},
    {id:2, title:'css', body:'css is ...'},
    {id:3, title:'javascript', body:'javascript is ...'},
  ])
  let content = null;
  if(mode === 'WELCOME') {
    content = <Article title="Welcome" body="Hello, WEB"></Article>
  } else if(mode === 'READ') {
    let title, body = null;
    for(let i=0; i<topics.length; i++) {
      if(topics[i].id === id) {
        title = topics[i].title;
        body = topics[i].body;
      }
    }
    content = <Article title={title} body={body}></Article>
  } else if(mode === 'CREATE') {
    content = <Create onCreate={(title, body)=>{
      const newTopic = {id:nextId, title:title, body:body}
      //바깥쪽이 배열이므로 배열을 복제
      const newTopics = [...topics]
      //복제한 newTopics에 newTopic을 push
      newTopics.push(newTopic)
      //setTopics를 newTopics로 바꿔줌
      setTopics(newTopics);

      //글의 상세페이지로 이동
      setMode('READ');
      setId(nextId);
      setNextId(nextId+1);
    }}></Create>
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
      <a href="/create" onClick={(event)=>{
        event.preventDefault();
        setMode('CREATE');
        }}>Create</a>
    </div>
  );
}

export default App;
