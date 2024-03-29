const form = document.querySelector('#addForm');
const btn = document.querySelector('#send');
let website_url = window.location.protocol +'//'+ window.location.host;
const loaderIcon = '<i class="fas fa-spinner fa-spin"></i>'; // ikona ładowania
const errorIcon = '<i class="fas fa-exclamation-triangle"></i>'; // ikona błędu
const sendIcon = '<i class="fas fa-paper-plane"></i>'; // ikona wysłania

btn.addEventListener('click', ()=>{
    const csrf_token = document.cookie.split('=')[1];

    const game_title = form.children[1].value;
    const url = form.children[3].value;

    btn.disabled = true; // blokowanie przycisku
    btn.innerHTML = `${loaderIcon} Wysyłanie...`; // zmiana tekstu przycisku na ikonę ładowania

    fetch(`${website_url}/api/games`, {
        method: 'POST',
        headers: {
            "Content-Type" : "application/json",
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            title: game_title,
            link: url
        })
    })
    .then(res => {
        //console.log(res.json());
        // odblokuj przycisk i usuń ikonę ładowania po pomyślnym wykonaniu żądania POST
        if(res.status === 201) {
            btn.disabled = false;
            btn.innerHTML = `${sendIcon}Dodaj grę`;
            window.close();
            window.location.reload()
        } else {
            btn.disabled = true;
            btn.style.backgroundColor = 'red';
            btn.innerHTML = `${errorIcon} Błąd`;
        }
    })
    .catch(err => {
        console.log(err);
        // odblokuj przycisk i usuń ikonę ładowania w przypadku błędu
        btn.disabled = true;
        btn.style.backgroundColor = 'red';
        btn.innerHTML = `${errorIcon} Błąd`;
    });
});

//TODO: add popup animation to add.js
//
// function showPopup() {
//         document.getElementById("popup").classList.add("show");
//       }
//
//       function hidePopup() {
//     document.getElementById("popup").classList.remove("show");
// }
