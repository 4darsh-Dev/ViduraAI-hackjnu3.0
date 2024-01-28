console.log('I am working!')

const author = 'Adarsh Maurya!'

console.log(`Developer ${author}`)

let menuBtnCond = true
let checkLabel = document.getElementById('check-label')

const menuBtnChanger = function () {
  if (menuBtnCond) {
    checkLabel.innerHTML = `<i class='bx bx-x'></i>`
    menuBtnCond = false
  } else {
    checkLabel.innerHTML = `<i class='bx bx-menu'></i>`

    menuBtnCond = true
  }
}

let menuBtn = document.getElementById('check')
menuBtn.addEventListener('click', menuBtnChanger)

//   card animation
let boxes = document.querySelectorAll('.box')
let currentIndex = 0

function animate() {
  // Remove 'active' class from all boxes
  boxes.forEach((box) => box.classList.remove('active'))

  // Add 'active' class to the current box
  boxes[currentIndex].classList.add('active')

  // Update currentIndex for the next box, or reset to 0 if we've reached the end
  currentIndex = (currentIndex + 1) % boxes.length
}

// Start the animation initially
animate()

// Change the active div every 2 seconds
// setInterval(animate, 2000)
