const modalToggle = function() {
    document.querySelector('#modal').classList.toggle('active')
}

const loginBtn = document.querySelector('#login-btn')
loginBtn.addEventListener('click', modalToggle)

const loginDelete = document.querySelector('#login-delete')
loginDelete.addEventListener('click', modalToggle)