const loginForm = document.getElementById('login-form')
const contentContainer = document.getElementById('content-container')
const baseEndpoint = 'http://localhost:8001/api'

if (loginForm){
    loginForm.addEventListener('submit', handleLogin)

}

function handleLogin(event){
    console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)
    // console.log(bodyStr)
    const options = {
        method: "post",
        headers: {
            'Content-Type': 'application/json',
        },
        body: bodyStr
    }
    fetch(loginEndpoint, options)
        .then(response=>{
            return response.json()
        })
        .then(authData => {
            handleAuthData(authData, getProductList)
        })
        .catch(err => {
            console.log(err)
        })
}

function handleAuthData(authData, callback) {
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
    if (callback){
        callback()
    }
}

function writeToContainer(data) {
    if (contentContainer){
        contentContainer.innerHTML = '<pre>' + JSON.stringify(data, null, 4 ) + '</pre>'
    }
}

function getFetchData(method, body){
    return {
        method: method === null ? 'GET' : method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('access')}`
        },
        body: body ? body : null
    }
}
function getProductList() {
    const Endpoint = `${baseEndpoint}/products/`
    const options = getFetchData("GET")
    }
    fetch(Endpoint, options)
        .then(response => response.json())
        .then(data => {
        writeToContainer(data)
    })