const wrapper = document.querySelector(".wrapper");
const middle = document.querySelector(".middle");
const upper = document.querySelector(".upper");
const left = document.querySelector(".left");
const right = document.querySelector(".right");
const middleBottom = document.querySelector(".middle-bottom");

console.log('pk from second master.js', pk)

const upperParking = {
  rows: 1,
  cols: 19,
  DOM: upper
}

const middleParking = {
  rows: 2,
  cols: 21,
  DOM: middle
}

const globalArr = []
class Dom {
    constructor(id, DOM, rows, cols) {
        this.id = id
        this.DOM = DOM
        this.rows = rows
        this.cols = cols
        globalArr.push(this)
    }
}

function fillData(parking) {
  for(let row = 1; row <= parking.rows; row++) {
      for(let col = 1; col <= parking.cols ; col++) {
        let newSpot = document.createElement('div');
        newSpot.setAttribute('class', 'parking-place free')
        newSpot.setAttribute('data-grid', `${row}.${col}`)
        parking.DOM.appendChild(newSpot)
      }
  }
}

fillData(upperParking);
fillData(middleParking);


function updateParkingSpaces(dataArr) {
    dataArr.forEach((x)=>{
      switch (x.localization) {
        case 'upper':
            let el = upper.querySelector(`[data-grid="${x.row}.${x.column}"]`)
            if(x.status == "occupied") el.classList.add('occupied')
            else el.classList.remove('occupied')
      }
    })
}

let dataArr;
async function getData(url = '') {
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    },
  })
  .then((response) => response.json())
  .then((data) => {
    console.log(data)
//    updateParkingSpaces(data)
    dataArr = data
  })
}

getData('http://127.0.0.1:8000/api/list/'+pk)

//setInterval(() => {
//    getData('http://127.0.0.1:8000/api/list/1')
//}, 3000)

//dataArr.localization_qs.forEach((localization) => {
//  let locEl = document.querySelector(`.${localization.name}`)
//	console.log(locEl)
//})