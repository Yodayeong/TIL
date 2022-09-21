const h1 = document.querySelector('h1')
        h1.addEventListener('copy', function(event) {
            //event의 기본 동작을 막음
            event.preventDefault()
            alert('제목은 복사가 되지 않습니다.')
        })