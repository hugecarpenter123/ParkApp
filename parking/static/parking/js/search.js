const searchBar = document.querySelector('.search-bar input')
const galleryView = document.getElementById('gallery_view')

async function getData(url) {
  const response = await fetch(url, {
    method: 'GET',
  })
  .then((response) => response.json())
  .then((data) => {
      console.log(data)
      updateGallery(data)
  })
}

//keydown
searchBar.addEventListener("keyup", (e) => {
    if (searchBar.value != '') {
        getData('http://127.0.0.1:8000/api/locations/?search='+searchBar.value)
    } else {
        getData('http://127.0.0.1:8000/api/locations/')
    }
});

function updateGallery(data) {
     console.log('update is called() ---------------------------')
    galleryView.innerHTML = ""
    data.forEach((obj) => {
        console.log(obj)
        let newGalleryEl = document.createElement('div')
        newGalleryEl.classList.add('gallery')

        let aTag = document.createElement('a')
        aTag.setAttribute('href', `/${obj.id}/`)

        let image = document.createElement('img')
        image.setAttribute('src', obj.image_path)

        let title = document.createElement('div')
        title.classList.add('img_title')
        title.textContent = obj.name

        newGalleryEl.appendChild(aTag)
        aTag.appendChild(image)
        newGalleryEl.appendChild(title)

        galleryView.appendChild(newGalleryEl)
    })
}
