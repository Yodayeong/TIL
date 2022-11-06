## Axios로 비동기 처리



### 비동기 처리

특정 코드의 연산이 끝날 때까지 코드의 실행을 멈추지 않고 다음 코드를 먼저 실행하는 자바스크립트의 처리



### promise 객체

**promise**는 자바스크립트에서 제공하는 비동기를 간편하게 처리할 수 있게 도와주는 객체



### axios 라이브러리 사용하기

- 라이브러리 로드하기

  ```html
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  ```

- promise 생성하기

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
      <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  </head>
  <body>
      
      <script>
          // Promise 객체 생성
          // resolve, reject는 콜백 함수의 인자
          const promise = new Promise((resolve, reject) => {
              // 비동기 작업 수행
  
              if (/* 비동기 작업 수행 성공 */) {
                  resolve('Success');
              }
              else { /* 비동기 작업 수행 실패 */
                  reject('Failed');
              }
          })
      </script>
  </body>
  </html>
  ```

- promise의 상태

  - **Pending(대기)** : 비동기 처리 로직이 아직 미완료인 상태

    - promise를 호출하면 pending 상태가 됨. 콜백 함수의 인자로 resolve, reject에 접근할 수 있음.

    - ```html
      new Promise(function(resolve, reject) {
      			// ...
              });
      ```

  - **Fulfilled(이행)** : 비동기 처리가 완료되어 promise가 결과 값을 반환해준 상태

    - 콜백 함수의 인자 resolve를 실행하면 fulfilled 상태가 됨. 이후 이행 상태가 되면 .then()을 이용해 처리 결과 값을 받을 수 있음.

    - ```html
      new Promise(function(resolve, reject) {
                  resolve();
              });
      ```

  - **Rejected(실패)** : 비동기 처리가 실패하거나 오류가 발생한 상태

    - 콜백 함수의 인자 reject를 실행하면 rejected 상태가 됨. 이후 실패 상태가 되면 .catch()를 이용해 error를 다룰 수 있음.

    - ```html
      new Promise(function(resolve, reject) {
                  reject();
              });
      ```

  - => Promise는 정해진 기능을 수행했을 때, 정상적으로 이루어지면 성공, 예상치 못한 문제가 발생하면 에러를 전달. 또, 비동기 작업을 하는 함수의 리턴타입으로 쓰이며, 어떤 함수가 비동기적인 작업을 한다고 하면, 그 함수는 프로미스를 반환.

- Promise 사용 방법1

  - ```html
    <script>
            const devide = (num1, num2) => {
                return new Promise((resolve, reject) => {
                    if (num2 != 0) {
                        resolve(num1 / num2);
                    } else {
                        reject(new Error("0으로 나눌 수 없습니다."));
                    }
                })
            }
    
            /* Success: 두번째 인자가 0이 아닐 경우 */
            devide(10, 5)
                .then((value) => console.log("성공:", value))
                .catch((error) => console.log("실패:", error))
    
            /* Failed : 두번째 인자가 0일 경우 */
            devide(10, 0)
                .then((value) => console.log("성공:", value))
                .catch((error) => console.log("실패:", error))
        </script>
    ```

- Promise 사용방법2

  - ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
        <title>Document</title>
    </head>
    <body>
        <script>
            axios.get('https://dog.ceo/api/breeds/image/random').then((Response) => {
                console.log(Response.data);
            }).catch((Error) => {
                console.log(Error);
            })
        </script>
    </body>
    </html>
    ```

- Promise 사용방법3

  - ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
        <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
        <title>Cuttee Dogs</title>
    </head>
    <body>
        <button id="dog">강아지</button>
        <div class="dogs"></div>
    
        <script>
            const button = document.querySelector("#dog")
            const url = 'https://dog.ceo/api/breeds/image/random'
    
            const getDogImages = function() {
                axios.get(url).then((response) => {
                    console.log(response)
                    const imgURL = response.data.message;
                    const dogImage = document.createElement("img")
                    dogImage.src = imgURL;
                    dogImage.style.height = "300px";
                    dogImage.style.width = "300px";
                    document.querySelector(".dogs").appendChild(dogImage);
                })
            }
            button.addEventListener("click", getDogImages)
        </script>
    </body>
    </html>
    ```