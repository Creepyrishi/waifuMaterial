var menu = document.getElementById('slide')
//setting menu height to maximum
menu.style.height = `${document.documentElement.scrollHeight-15}px`
//side menu-
console.log(document.documentElement.scrollHeight)
function side(){
  var menuDisplay = window.getComputedStyle(menu, null).getPropertyValue('display')
  var line = document.querySelector('#line_container')
  if (menuDisplay === 'block'){
    menu.style.display = 'none'
    line.style.transform = "rotate(-180deg)";
  }
  else{
    menu.style.display = 'block'
    line.style.transform = "rotate(90deg)";
  }
}