## Bootstrap(추가 공부)



### Form

- 폼 형식은 사용자 교류를 가능하도록 해준다.

- ex) `<input>`,`<select>`, `<textarea>`, `<button>`

  - `<form>`, `<input>` 요소는 `<label>`과 `<button>`과 함께 쓰인다.

  - ```html
    <form>
        /*label 태그는 폼 요소에 이름을 붙이기 위한 것
        label 태그의 for은 input 태그의 id와 같은 것*/
    	<label for="animal">What is your favorite animal?</label>
        <input type="text" id="animal" name="animal">
        <button>Save</button>
    </form>
    ```
