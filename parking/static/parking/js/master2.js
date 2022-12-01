const globalSet = {}
const wrapper = document.querySelector('.wrapper')
freeSpotCounter = document.getElementById('free-spot-input');
occupiedSpotCounter = document.getElementById('occupied-spot-input');
let dataArr;

async function getData(url, update=false) {
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    },
  })
  .then((response) => response.json())
  .then((data) => {
    if(update) {
      console.log('update')
      updateParkingSpaces(data)
    } else {
      getDom(data)
      console.log(data)
//      dataArr = data
//        setInterval(() => {
//            getData('http://127.0.0.1:8000/api/list/'+pk, true)
//        }, 3000)
    }
  })
}


function getDom(dataArr) {
    dataArr.section_qs.forEach((section) => {
        console.log('section:', section)
        globalSet[section.name] = document.querySelector(`.${section.name}`)
    })
}

function updateParkingSpaces(dataArr) {
    let free = 0;
    let occupied = 0;
    console.log('update')
    dataArr.section_qs.forEach((section) => {
        section.spot_qs.forEach((spot) => {
            let el = globalSet[section.name].querySelector(`[data-grid="${spot.row}.${spot.column}"]`)
            console.log(el)
            el.setAttribute('class', spot.status)
            if (spot.status[0] === 'f') free += 1;
            else occupied += 1;
        })
    })
    freeSpotCounter.textContent = free;
    occupiedSpotCounter.textContent = occupied;
}

getData('http://127.0.0.1:8000/api/list/'+pk)
