let icons = document.querySelectorAll('.star-icon')
let star_col = document.querySelector('#stars')
let icon_html = '<h1><i class="bi bi-star"></i></h1>'
let fill_icon_html = '<h1><i class="bi bi-star-fill"></i></h1>'
const rateText = 'Ocena: '

// set 0 if no update
setRate()


function sendRate(rate){
    const id = window.location.pathname[9]
    let rate_element = document.querySelector('#rate')
    
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

    fetch(`http://127.0.0.1:8000/api/games/${id}/`, {
        method: 'GET',
        headers: {
            "Content-Type" : "application/json",
        },
    })
    .then(res => {return res.json()})
    .then(data =>{
        rate_element.textContent = rateText + data.review_ratio
    })
    
}



function setRate(){
    let rate_element = document.querySelector('#rate')
    const id = window.location.pathname[9]
    const csrf_token = document.cookie.split('=')[1]


    fetch(`http://127.0.0.1:8000/api/games/${id}/`, {
        method: 'GET',
        headers: {
            "Content-Type" : "application/json",
        },
    })
    .then(res => {return res.json()})
    .then(data =>{
        console.log(data.review_ratio)
        if(!data.review_ratio){
            rate_element.textContent = rateText + '0'
            fetch(`http://127.0.0.1:8000/api/gamesreview`, {
                method: 'POST',
                headers: {
                    "Content-Type" : "application/json",
                    'X-CSRFToken': csrf_token
                },
                body: JSON.stringify({
                    gameName: id,
                    rate: 1
                })
            })
            .then(res => console.log(res.json()))
            .catch(err => console.log(err))
        }
        else{
            rate_element.textContent = rateText + data.review_ratio
        }

    })
    .catch(err => console.log(err))
    //.catch(console.log("Can't get reviews"))


}


function resetIcons(icons){
    for(let icon of icons){
        icon.innerHTML = icon_html
    }
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


