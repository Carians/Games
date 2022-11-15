function search_func(){
    let input = document.querySelector('.search')
    let items = document.getElementsByClassName("item")

    let filter = input.value.toUpperCase()
    
    for(let item of items){
        if(item.id.toUpperCase().indexOf(filter) > -1){
            item.classList.remove('d-none')
        }
        else{
            item.classList.add('d-none')
            console.log(item)
        }
    }
    
}