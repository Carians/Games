const form = document.querySelector('#addForm')

const btn = document.querySelector('#send')

btn.addEventListener('click', ()=>{
    const csrf_token = document.cookie.split('=')[1]

    game_title = form.children[1].value
    email = form.children[3].value
    url = form.children[5].value
   
    fetch('http://127.0.0.1:8000/api/games', {
        method: 'POST',
        headers: {
            "Content-Type" : "application/json",
            'X-CSRFToken': csrf_token
        },
        body: JSON.stringify({
            title: game_title,
            link: url
        })
    })
    .then(res => console.log(res.json()))
    .catch(err => console.log(err))
})