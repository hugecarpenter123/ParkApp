let showStatistics = document.getElementById('show-janus');
let chart = document.getElementById('myChart');

showStatistics.addEventListener('click', () => {
    if(chart.style.opacity == 0) {
        chart.style.display = 'block';
        setTimeout(()=>{
            chart.style.opacity = 1;
        },1)
    } else {
        chart.style.opacity = 0;
        setTimeout(()=>{
            chart.style.display = 'none';
        },500)
    }
})

async function getDataCharts() {
    const url = 'http://127.0.0.1:8000/api/statistics/' + pk
  const response = await fetch(url, {
    method: 'GET',
  })
  .then((response) => response.json())
  .then((data) => {
      console.log(data)
      datesArr = data
      parseData(data)
  })
}

function parseData(data) {
    let yesterday = []
    let today_day = new Date().getDate()
    let today_month = new Date().getMonth()

    data.forEach((obj) => {
        let tmp = new Date (obj.date)
//        if (tmp.getDate == today_day - 1) {
//            yesterday.push(tmp)
//        }
        if (tmp.getDate() == today_day && tmp.getMonth() == today_month) {
            yesterday.push(tmp.getHours())
        }
    })

    let hours_obj = {}
    for(let i = 0; i < 24; i++) {
          hours_obj[i] = yesterday.filter((obj) => {
          if(obj == i) {return true}
        }).length
    }
    buildChart(hours_obj)
}


function buildChart(hoursObject) {
    const keys = Object.keys(hoursObject)
    const values = Object.values(hoursObject)

    const chartData = {
      "type": "vbar",
      "legend": {
        "marker": {
          "cursor": "hand"
        },
        "item": {
          "cursor": "hand"
        },
        "border-color": "none",
        "align": "center",
        "vertical-align": "bottom",
        "max-items": 23,
        "overflow": "page",
        "page-on": {
          "background-color": "black",
          "border-width": 1,
          "border-color": "black"
        },
        "page-off": {
          "background-color": "#ffe6e6",
          "border-width": 1,
          "border-color": "black"
        },
        "page-status": {
          "font-color": "black",
          "font-size": 11,
          "font-family": "Georgia",
          "background-color": "#ffe6e6"
        },
        "toggle-action": "none"
      },
      "plotarea": {
        "margin": "dynamic",
        "border-top": "1px solid grey",
        "border-right": "1px solid grey"
      },
      "scale-x": {
        "auto-fit": true,
        "line-width": 1,
        "items-overlap": true,
        "item": {
          "angle": 0,
          "wrap-text": true
        }
      },
      "scale-y": {
        "ref-line": {
          "visible": true,
          "line-style": "solid",
          "items-overlap": true
        },
        "guide": {
          "line-style": "solid"
        }
      },
      "plot": {
        "value-box": {
          "text": "%vt ",
          "visible": true,
          "font-color": "black",
          "font-size": "10px",
          "decimals": 12,
          "angle": 0,
          "placement": "middle"
        },
        "animation": {
          "effect": "ANIMATION_SLIDE_BOTTOM",
          "speed": "1500"
        }
      },
      "series": [{
        "values": values
      }]
    };

    zingchart.render({
      id: "myChart",
      data: chartData,
      height: '100%',
      width: "100%"
    });
}

const url = 'http://127.0.0.1:8000/api/statistics/' + pk
getDataCharts()