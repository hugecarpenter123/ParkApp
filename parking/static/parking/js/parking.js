showInfoBtn = document.getElementById('show-info');
showInfoEl = document.querySelector('.popup-info');

showInfoBtn.addEventListener('click', () => {
    if(showInfoEl.style['opacity'] == 1) {
        showInfoEl.style['opacity'] = 0;
        setTimeout(()=>{
            showInfoEl.style.display = 'none';
        }, 500)
    } else {
        showInfoEl.style.display = 'grid';
        setTimeout(()=>{
            showInfoEl.style['opacity'] = 1;
            window.scrollBy(0,150);
        }, 1)
    }
})