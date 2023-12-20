//Первое задание level stone
console.log("Первое задание level stone: ");
let Number_One = prompt('First_digit');
let Number_Two = prompt('Out_digit');
if (Number_One === Number_Two) {
    console.log('Введенные переменные равны');
}else{
    console.log('Введенные переменные НЕ равны');
}
let Word = 'world';
let sum = Number_One + Word;
console.log('Конкотенация переменных: ',sum);
console.log("_________________________________________");
//Задание второе level iron
console.log("Второе задание level iron: ");
let arr = ['apple', 'strawberry', 'blueberry', 'raspberry', 'lemon'];
for(let i=0;i<arr.length;i++){
    console.log('Фрукт: ',arr[i]);
}
for(let i=0;i<arr.length;i++){
    switch(arr[i]){
        case 'apple':
            console.log(arr[i],':'," apple green");
        break;
        case 'strawberry':
            console.log(arr[i],':',"strawberry red");
        break;
        case 'blueberry':
            console.log(arr[i],':',"blueberry blue");
        break;
        case 'raspberry':
            console.log(arr[i],':',"raspberry light red");
        break;
        case 'lemon':
            console.log(arr[i],':',"lemon yellow");
        break;
    }
}
console.log("_________________________________________");
// Третье задание level gold
console.log('Третье задание level gold');
let quantiyPeople = parseInt(prompt('Введите количество человек на работе', undefined));
let PricePeople = parseInt(prompt('Введите зарплату на человека', undefined));
let PriceALLPeople = 0;
if (PricePeople == null || quantiyPeople == null){
    alert('Вы отмениили ввод двух или одного значения, пожалуйста перезагрузите страницу и повторите попытку');
}
else if(/[a-z,A-Z,\u0400-\u04FF]/.test(PricePeople) || /[a-z,A-Z,\u0400-\u04FF]/.test(quantiyPeople)){
    alert('Вы вставили букву в одно из полей ввода или пустым (с буквой не считается)');
}
else{
    for(let i=0; i<quantiyPeople;i++){
        PriceALLPeople = PriceALLPeople + PricePeople;
    }
    console.log(PriceALLPeople);
    alert(`Зарплата сотрудников: ${PriceALLPeople}`);
}
console.log("_________________________________________");
// Четвертое задание вывести среднюю оценку и список плохих студентов
console.log('Четвертое задание level gold');
let klassSoStudentami = [
    {FIO:'Петров А.А.',
    Ocenka:5},
    {FIO:'Иванов Б.Б.',
    Ocenka:3.4},
    {FIO:'Сидоров Г.Г.',
    Ocenka:9},
    {FIO:'Немолодой Д.Д',
    Ocenka:2},
    {FIO:'Молодой Е.Е',
    Ocenka:3.4}];
    let sredniaOcenka = 0;
    let BADstudent = [];
    // console.log('Средння оценка студентов: ',klassSoStudentami[1].Ocenka);
    for(let i=0;i<klassSoStudentami.length;i++){
        sredniaOcenka = sredniaOcenka +  klassSoStudentami[i].Ocenka;
    }
    sredniaOcenka = sredniaOcenka / klassSoStudentami.length;
    console.log('Средння оценка студентов: ',sredniaOcenka);
    for(let i=0;i<klassSoStudentami.length;i++){
        if (klassSoStudentami[i].Ocenka < sredniaOcenka){
            BADstudent.push(klassSoStudentami[i]);
        }
    }
    console.log('ПЛОХИЕ студенты: ',BADstudent);
console.log("_________________________________________");
// да не может быть там ошибок