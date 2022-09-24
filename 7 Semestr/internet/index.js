let cars = [
    {
        'carName': "Ford Fiesta Mk6",
        'image' : "https://avatars.mds.yandex.net/get-verba/787013/2a000001609d3fbc6931ae886f5e2e671f6e/cattouchret",
        'price': 649000,
        'year': 2009,
        'mileage': 68200,
        'town': 'Самара',
        'drive': 'Передний'
    },
    {
        'carName': "Ford Mondeo IV",
        'image' : "https://s0.rbk.ru/v6_top_pics/media/img/0/18/756493243588180.jpg",
        'price': 699000,
        'year': 2011,
        'mileage': 161863,
        'town': 'Тамбов',
        'drive': 'Передний'
    },
    {
        'carName': "Ford Focus III",
        'image' : "https://avatars.mds.yandex.net/get-verba/787013/2a000001609ce7896ac5152bb37fa41b380a/cattouch",
        'price': 589900,
        'year': 2013,
        'mileage': 170000,
        'town': 'Таганрог',
        'drive': 'Передний'
    },
    {
        'carName': "Subaru Forester II",
        'image' : "https://avatars.mds.yandex.net/get-verba/216201/2a000001609ce4937244e79149500f89ff85/cattouch",
        'price': 685000,
        'year': 2005,
        'mileage': 263900,
        'town': 'Москва',
        'drive': 'Полный'
    },
    {
        'carName': "Subaru Outback II",
        'image' : "https://avto-russia.ru/autos/subaru/photo/subaru_outback_ii_1.jpg",
        'price': 249700,
        'year': 1999,
        'mileage': 300000,
        'town': 'Санкт-Петербург',
        'drive': 'Полный'
    },

]

function id(id){
    return document.getElementById(id);
}
function qs(selector){
    return document.querySelector(selector);
}
function qsa(selector){
    return document.querySelectorAll(selector);
}

window.onload = function(){
    generateList(cars)
}

function generateList(cars) {
    for (let i = 0; cars.length; i++) {

        let card = document.createElement('div');
        card.classList.add('card')

        let image = document.createElement('img')
        image.classList.add('card_image')        
        image.src = cars[i]['image']
        card.appendChild(image)
        // Первая Колонка 
        let firstCollum = document.createElement('div');
        firstCollum.classList.add('card_block_200')

        let nameText = document.createElement('p')
        nameText.classList.add('font_name')
        nameText.textContent= cars[i]['carName']        

        let townText = document.createElement('p')
        townText.classList.add('font_town')
        townText.textContent= cars[i]['town']

        firstCollum.appendChild(nameText)
        firstCollum.appendChild(townText)

        // Вторая Колонка 
        let secondCollum = document.createElement('div');
        secondCollum.classList.add('card_block_200')

        let priceText = document.createElement('p')
        priceText.classList.add('font_name')
        priceText.textContent= cars[i]['price'] + "₽" 

        let driveText = document.createElement('p')
        driveText.classList.add('font_info')
        driveText.textContent= cars[i]['drive'] + " привод" 


        secondCollum.appendChild(priceText)
        secondCollum.appendChild(driveText)

        // Третья Колонка 
        let thirdCollum = document.createElement('div');
        thirdCollum.classList.add('card_block_200')

        let yearText = document.createElement('p')
        yearText.classList.add('font_name')
        yearText.textContent= cars[i]['year'] + "г" 

        let mileageText = document.createElement('p')
        mileageText.classList.add('font_name')
        mileageText.textContent= cars[i]['mileage'] + "км" 


        thirdCollum.appendChild(yearText)
        thirdCollum.appendChild(mileageText)


        card.appendChild(firstCollum)
        card.appendChild(secondCollum)
        card.appendChild(thirdCollum)

        id('car-list').appendChild(card)
    }
}