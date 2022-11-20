let icons = document.querySelectorAll('.star-icon')
let icon_html = '<h1><i class="bi bi-star"></i></h1>'
let fill_icon_html = '<h1><i class="bi bi-star-fill"></i></h1>'



for(let icon of icons){
    icon.addEventListener('mouseover', (e)=>{
        let icon_id = icon.id[4]
        //console.log(icon)
        
        for(let i=0; i<=icon_id; i++){
            icons[i].innerHTML = fill_icon_html
        }
    })
    icon.addEventListener('mouseout', (e)=>{
        for(let icon of icons){
            icon.innerHTML = icon_html
        }
    })

}

let views = document.querySelector('#views')
let token = ''

axios.post('/api/auth/', {
    username: 'michal',
    password: 'michal'
})
.then(function (response) {
    console.log(response)
    token = response.data.token
    console.log(token)
    axios.get('/api/games', {
        headers: {
            Authorization: `Bearer ${token}`
        }
    })
    .then(function (response) {
        console.log(response);
    })
})

