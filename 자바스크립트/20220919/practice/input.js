const input = document.querySelector('#input-text')
        input.addEventListener('input', function(e) {
            console.log(e)
            //input의 value를 가져오고 싶음
            console.log(e.target.value)
        })