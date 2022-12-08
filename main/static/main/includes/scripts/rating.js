let icons = document.querySelectorAll('.star-icon')
let star_col = document.querySelector('#stars')
let icon_html = '<h1><i class="bi bi-star"></i></h1>'
let fill_icon_html = '<h1><i class="bi bi-star-fill"></i></h1>'


// at load
getRate()

// reloading rate at interval
document.addEventListener('DOMContentLoaded', updateRateLive)


function getRate(){
    const id = window.location.pathname[9]
    let rate_element = document.querySelector('#rate')

    fetch(`http://127.0.0.1:8000/api/games/${id}/`, {
        method: 'GET',
    })
    .then(res => {
        return res.json()
    })
    .then(data =>{
        let rate = data.review_ratio
        if(rate == null){ // TODO post jezeli nie istnieje gamereview
            postRate(0)
        }

        rate_element.textContent += rate
    })
    .catch(err => console.log(err))
}



function resetIcons(icons){
    for(let icon of icons){
        icon.innerHTML = icon_html
    }
}

// TODO
function getAuthToken(){
    const csrf_token = document.cookie.split('=')[1]
    let credentials = {
        username: 'michal',
        password: 'michal'
    }

    fetch(`http://127.0.0.1:8000/api/auth/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token
        },
        body: credentials
    })
    .then(response => console.log(response))
}



function sendRate(rate){
    const id = window.location.pathname[9]
    // const token = '515ce0e46051419e97830acb233a0f945d1e43d5'
    
    const csrf_token = document.cookie.split('=')[1]


    fetch(`http://127.0.0.1:8000/api/gamesreview/${id}/update`, {
        method: 'PUT',
        headers: {
            "Content-Type" : "application/json",
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify({
            rate: rate
        })
    })
    .then(res => {
        return res.json()
    })
    .catch(err => console.log(err))
}


function postRate(rate){
    const id = window.location.pathname[9]
    const title = document.querySelector('#title')
    const csrf_token = document.cookie.split('=')[1]


    fetch(`http://127.0.0.1:8000/api/gamesreview`, {
        method: 'POST',
        headers: {
            "Content-Type" : "application/json",
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify({
            gameName: title,
            rate: rate
        })
    })
    .then(res => {
        return res.json()
    })
    .catch(err => console.log(err))
}


function updateRateLive(){
    const id = window.location.pathname[9]
    let rate_element = document.querySelector('#rate')

    setInterval(() =>{
        fetch(`http://127.0.0.1:8000/api/gamesreview/${id}/`, {
            method: 'GET',
        })
        .then(res => {
            return res.json()
        })
        .then(data =>{
            let rate = data.rate
            rate_element.textContent = 'Ocena: ' + rate
        })
        .catch(err => console.log(err))
    }, 2000)
}


let rects = { // positions of stars
    left: icons[0].getBoundingClientRect().left,
    right: icons[4].getBoundingClientRect().right,
    top: icons[0].getBoundingClientRect().top,
    bottom: icons[0].getBoundingClientRect().bottom
}

// Adding icons on hover
for(let icon of icons){
    icon.addEventListener('mouseover', (e)=>{
        resetIcons(icons)
        let icon_id = icon.id[4]
        
        for(let i=0; i<=icon_id; i++){
            icons[i].innerHTML = fill_icon_html
        }
        // click check
        if(e.buttons == 1){
            let rate = parseInt(icon_id) + 1
            sendRate(rate)
        }
    })
}

star_col.addEventListener('mouseover', (e) =>{
    if(e.clientX < rects.left || e.clientX > rects.right){
        resetIcons(icons)
    }
    if(e.clientY < rects.top || e.clientY > rects.bottom){
        resetIcons(icons)
    }
})



// axios.get('/api/games', {
// })
// .then(function (response) {
//     console.log(response);
// })


