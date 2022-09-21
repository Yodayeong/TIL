//초기값
let countNum = 0

const btn1 = document.querySelector('#btn1')
btn1.addEventListener('click', function() {
    countNum -= 1
    const p = document.querySelector('p')
    p.innerText = countNum
})

const btn2 = document.querySelector('#btn2')
btn2.addEventListener('click', function() {
    countNum += 1
    const p = document.querySelector('p')
    p.innerText = countNum
})