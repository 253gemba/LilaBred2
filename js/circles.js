const buttons = document.querySelectorAll('#services .services__wrapper-icons .icon');
const buttons_hidden = document.querySelectorAll('#services .services__wrapper-icons .icon_hidden');
const circles = document.querySelectorAll('#services .services__wrapper-icons .circle')

function reset() {
    for (let j = 0; j < 4; j++) {
        buttons[j].style.display = 'inline-block';
        buttons_hidden[j].style.display = 'none;'
        circles[j].style.display = 'none';
    }
}

for (let i = 0; i < 4; i++) {
    buttons[i].addEventListener('click', function () {
        reset();
        let index = i;
        buttons[index].style.display = 'none';
        buttons_hidden[index].style.display = 'inline-block';
        circles[index].style.display = ''; 
    });
}

for (let i = 0; i < 4; i++) {
    buttons_hidden[i].addEventListener('click', function () {
        reset();
        let index = i;
        buttons[index].style.display = 'inline-block';
        buttons_hidden[index].style.display = 'none';
        circles[index].style.display = 'none'; 
    });
}