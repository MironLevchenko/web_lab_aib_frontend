window.onload = function(){
    const HeadContentIMG =['https://ae01.alicdn.com/kf/HTB1nK2dclHH8KJjy0Fbq6AqlpXaZ/fun-Emoji-Face-PVC-football-ball-size-2-play-balls-Cartoon-cute-Soccer-balls-for-kids.jpg',
    'https://shop.art-mark.ru/image/data/fullsize/78590_2.jpg',
    'https://img.staticbg.com/images/oaupload/banggood/images/F1/C8/4a0149e7-6fe7-4aab-8a3d-eeaaafe4a0e0.jpg',
    'https://sc02.alicdn.com/kf/HTB1GiwJjgZC2uNjSZFnq6yxZpXaI/custom-stuffed-plush-animal-toys-giant-dinosaur.jpg',
    'https://ae01.alicdn.com/kf/HTB17Lm5CHSYBuNjSspfq6AZCpXaq.jpg',
    'https://cs3.pikabu.ru/post_img/big/2014/03/18/5/1395119345_1175541869.jpg'];
    const HeadText =['мячик','юла','кукла','динозавр','меч','пистолет'];
    const HeadContentIMG2 =['https://cdn1.ozone.ru/s3/multimedia-g/6084885352.jpg',
    'https://www.superhero-collection.com/wp-content/uploads/2013/06/spiderman-ballz-beanie.jpg',
    'http://g01.s.alicdn.com/kf/HTB16t7ZFFXXXXXCaVXXq6xXFXXXS/220661461/HTB16t7ZFFXXXXXCaVXXq6xXFXXXS.jpg',
    'https://www.kgelectronic.com.au/assets/full/503-6163.jpg?1532570526',
    'https://tehnoteca.ru/img/914/913475/chicco_safari_park_5.jpg',
    'https://ae01.alicdn.com/kf/HTB1vaHmem3PL1JjSZFtxh7lRVXaM/303PCS-Military-Plastic-s-Army-Men-Figures-in-12-Poses-3-Flags-Kids-Toy.jpeg',
    'https://s0.rbk.ru/v6_top_pics/resized/1440xH/media/img/0/54/756215145898540.jpg',
    'https://sc01.alicdn.com/kf/H6c1e141aeea94ed59c152f2e41f53d52Z/230874538/H6c1e141aeea94ed59c152f2e41f53d52Z.jpg',
    'https://avatars.mds.yandex.net/get-mpic/5287705/img_id4591685401970724368.jpeg/orig',
    'https://asia-caravan.ru/wp-content/uploads/2021/03/Detskiye-igrushki-optom.jpg',
    'https://best-shop.su/images/product_images/popup_images/1931_0.jpg',
    'https://avatars.mds.yandex.net/i?id=01886cca897cf8a4efa258f2f2062c74-4589919-images-thumbs&n=13'];
    const HeadText2 =['кактус','человек-паук','трансформер','кунг-фу Павла','Машинка','солдатики','конструктор LEGOBT+','Соска детская','титаник','Набор ребенка','новогодний подарок','Детская лупа'];
    function generatemagazine(mdx,arrImage,arrText,parentElement){
        for(let i=0; i<mdx; i++){
            let contentHead = document.createElement('div');
            contentHead.id = 'contentHead';
            parentElement.appendChild(contentHead);
            let contentHeadImage = document.createElement('img');
            contentHeadImage.id = 'contentHeadImage';
            contentHeadImage.style.cssText = `height: 250px; width:230px`;
            contentHeadImage.src = arrImage[i];
            contentHead.appendChild(contentHeadImage);
            let contentHeadText = document.createElement('p');
            contentHeadText.id = 'contentHeadText';
            contentHeadText.textContent = arrText[i]
            contentHead.appendChild(contentHeadText);
        }
    }
    generatemagazine(6,HeadContentIMG,HeadText,document.getElementById('child-con-head'));
    generatemagazine(12,HeadContentIMG2,HeadText2,document.getElementById('child-con-footer'));
}

