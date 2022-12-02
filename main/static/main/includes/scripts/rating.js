let icons = document.querySelectorAll('.star-icon')
let star_col = document.querySelector('#stars')
let icon_html = '<h1><i class="bi bi-star"></i></h1>'
let fill_icon_html = '<h1><i class="bi bi-star-fill"></i></h1>'

function resetIcons(icons){
    for(let icon of icons){
        icon.innerHTML = icon_html
    }
}


function sendRate(rate){
    let id = window.location.pathname[9]
    let token = '515ce0e46051419e97830acb233a0f945d1e43d5'

    //TODO POST TEZ NIE DZIALA 
    // axios.post('http://127.0.0.1:8000/api/games/6/', {
    // })
    // .then((res) => console.log(res))
    // .catch((err) => console.log(err))
    fetch(`http://127.0.0.1:8000/api/games/${id}/update`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        },
        body: JSON.stringify({
          title: 'Axios is a piece of crap'  
        })
    })
    .then(res => {
        return res.json()
    })
    .then(data => console.log(data))
    .catch(err => console.log(err))
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

// Sending data to api
let views = document.querySelector('#views')
let token = ''


axios.get('/api/games', {
})
.then(function (response) {
    console.log(response);
})


