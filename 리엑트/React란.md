### React란?

- 서로 연관된 코드들을 그룹핑하고 이름을 붙여서 복잡한 코드를 단순한 코드로

- 복잡한 코드를 숨기고 내가 만든 태그를 사용 => 사용자 정의 태그

- class 문법을 사용하거나 function 문법을 사용하여 만들 수 있음



### React app 만들기

```bash
npx create-react-app .
npm start 
```



### 소스코드 수정

- src -> index.js : npm start를 이용하여 create-react-app을 구동시키면, index.js에 적힌대로 동작함

- ```javascript
  //index.js
  
  import React from 'react';
  import ReactDOM from 'react-dom/client';
  import './index.css';
  //여기에서 App 태그가 옴
  import App from './App';
  import reportWebVitals from './reportWebVitals';
  
  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(
    <React.StrictMode>
      //App 태그가 UI 전체임
      <App />
    </React.StrictMode>
  );
  
  // If you want to start measuring performance in your app, pass a function
  // to log results (for example: reportWebVitals(console.log))
  // or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
  reportWebVitals();
  ```

- ```javascript
  //App.js
  
  import logo from './logo.svg';
  import './App.css';
  
  function App() {
    return (
      <div className="App">
        //여기 안의 내용들이 화면을 구성함
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
  
  export default App;
  ```

- ```html
  <!--index.html-->
  
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="utf-8" />
      <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <meta name="theme-color" content="#000000" />
      <meta
        name="description"
        content="Web site created using create-react-app"
      />
      <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
      <!--
        manifest.json provides metadata used when your web app is installed on a
        user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
      -->
      <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
      <!--
        Notice the use of %PUBLIC_URL% in the tags above.
        It will be replaced with the URL of the `public` folder during the build.
        Only files inside the `public` folder can be referenced from the HTML.
  
        Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
        work correctly both with client-side routing and a non-root public URL.
        Learn how to configure a non-root public URL by running `npm run build`.
      -->
      <title>React App</title>
    </head>
    <body>
      <noscript>You need to enable JavaScript to run this app.</noscript>
        <!--index.js가 받아오는 root값임-->
      <div id="root" style="border:10px solid red; height:100vh;"></div>
      <!--
        This HTML file is a template.
        If you open it directly in the browser, you will see an empty page.
  
        You can add webfonts, meta tags, or analytics to this file.
        The build step will place the bundled scripts into the <body> tag.
  
        To begin the development, run `npm start` or `yarn start`.
        To create a production bundle, use `npm run build` or `yarn build`.
      -->
    </body>
  </html>
  ```



### 배포

- 배포판을 만드는 과정

  ```bash
  npm run build
  ```

- build 폴더에 있는 index.html을 서비스하는 웹 서버가 실행

  ```bash
  npx serve -s build
  ```

  