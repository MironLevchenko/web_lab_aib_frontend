window.onload = function(){
    document.getElementById('Green').addEventListener('input', function() {
        // Если поле input не пустое, изменяем цвет блока на зеленый
        if (this.value != "") {
            document.getElementById('blockColor').style.backgroundColor = 'green';
        } else {
            // Если поле input пустое, возвращаем блоку исходный цвет
            document.getElementById('blockColor').style.backgroundColor = 'white';
        }
   });
   document.getElementById('Red').addEventListener('input', function() {
        // Если поле input не пустое, изменяем цвет блока на зеленый
        if (this.value != "") {
            document.getElementById('blockColor').style.backgroundColor = 'red';
        } else {
            // Если поле input пустое, возвращаем блоку исходный цвет
            document.getElementById('blockColor').style.backgroundColor = 'white';
        }
    });
    document.getElementById('Blue').addEventListener('input', function() {
        // Если поле input не пустое, изменяем цвет блока на зеленый
        if (this.value != "") {
            document.getElementById('blockColor').style.backgroundColor = 'blue';
        } else {
            // Если поле input пустое, возвращаем блоку исходный цвет
            document.getElementById('blockColor').style.backgroundColor = 'white';
        }
    });
    let count =0;
    document.getElementById('button').onclick = function(){
        let miniBlock = document.createElement('div');
        miniBlock.id ='miniBlock';
        miniBlock.innerText = 'Я цветной';
        document.getElementById('ParentBlock').appendChild(miniBlock);
        count++;
        if(count<15){
            miniBlock.style.cssText = `height:200px; width:20%; background: blue;position:absolute;`;
        }else{
            miniBlock.style.cssText = `height:200px; width:20%; background: brown;position:absolute;`;
        }
    }
}
