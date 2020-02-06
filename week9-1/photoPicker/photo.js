const current = document.querySelector('#current');
const imgs = document.querySelectorAll('.imgs img');
console.log(imgs);

imgs.forEach(function(img){
  img.addEventListener('click', imgClick)
})

const opacity = .4;

// // set First img opacity
imgs[0].style.opacity = opacity;

// imgs.forEach(function(img){
//   img.addEventListener('click', imgClick)
// });

// function imgClick(e) {

  // // reset opacity
  // imgs.forEach(function(img){
  //   return img.style.opacity = 1
  // });

function imgClick(e){
  imgs.forEach(function(img){
    return img.style.opacity = 1;
  })
  current.src = e.target.src;
  current.classList.add('fade-in')
  setTimeout(function () {
    current.classList.remove('fade-in')
  },.5);
  e.target.style.opacity = opacity
  console.log(e.target.src);
}


//   // Change current image to src of clicked image
//   current.src = e.target.src;
  
//   // Add fade in class
//   

//   // Remove fade-in class after .5seconds
//   
//  
// }