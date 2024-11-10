/* animate toggle menu */

const toggleButton = document.getElementById('toggle-btn')
const sidenav = document.getElementById('toggle-nav')

function toggleSideNav(){
    sidenav.classList.toggle('close')
    toggleButton.classList.toggle('rotate')

    Array.from(sidenav.getElementsByClassName('show')).forEach(ul => {
        ul.classList.remove('show')
        ul.previousElementSibling.classList.remove('rotate')
    })

}

function toggleSubMenu(button){
    button.nextElementSibling.classList.toggle('show')
    button.classList.toggle('rotate')

    if(sidenav.classList.contains('close')){
        sidenav.classList.toggle('close')
        toggleButton.classList.toggle('rotate')
    }
}