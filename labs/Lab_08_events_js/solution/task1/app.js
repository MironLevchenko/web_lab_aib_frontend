window.onload = function(){
    let Button1 = document.createElement('button');
    Button1.id = "Button1";
    let Button2 = document.createElement('button');
    Button2.id = "Button3";
    let Button3 = document.createElement('button');
    Button3.id = "Button3";
    Button1.innerHTML = "Я ЧЕРНЫЙ";
    Button2.innerHTML = "Я ЖЕЛТЫЙ";
    Button3.innerHTML = "Я КРАСНЫЙ";
    document.body.appendChild(Button1);
    document.body.appendChild(Button2);
    document.body.appendChild(Button3);
    Button1.addEventListener('click', function() {
        document.body.style.backgroundColor = 'black';
    });
    Button2.addEventListener('click', function() {
        document.body.style.backgroundColor = 'yellow';
    });
    Button3.addEventListener('click', function() {
        document.body.style.backgroundColor = 'red';
    });
}
