let icons = document.querySelectorAll('.star-icon')
let star_col = document.querySelector('#stars')
let icon_html = '<h1><i class="bi bi-star"></i></h1>'
let fill_icon_html = '<h1><i class="bi bi-star-fill"></i></h1>'

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


