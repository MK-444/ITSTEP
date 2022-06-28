// tabs

var tabLinks = document.querySelectorAll(".tablinks");
var tabContent = document.querySelectorAll(".tabcontent");


tabLinks.forEach(function(el) {
el.addEventListener("click", openTabs);
});


function openTabs(el) {
var btnTarget = el.currentTarget;
var country = btnTarget.dataset.country;

tabContent.forEach(function(el) {
    el.classList.remove("active");
});

tabLinks.forEach(function(el) {
    el.classList.remove("active");
});

document.querySelector("#" + country).classList.add("active");

btnTarget.classList.add("active");
}





const items = document.querySelectorAll(".accordion button");

function toggleAccordion() {
  const itemToggle = this.getAttribute('aria-expanded');
  
  for (i = 0; i < items.length; i++) {
    items[i].setAttribute('aria-expanded', 'false');
  }
  
  if (itemToggle == 'false') {
    this.setAttribute('aria-expanded', 'true');
  }
}

items.forEach(item => item.addEventListener('click', toggleAccordion));














(function () {
	'use strict';
	var slides = document.querySelectorAll('.testimonial-item'),
		 button = document.getElementById('button'),
		 arrows = document.querySelectorAll('.lnr'),
		 carouselCount = 0,
		 scrollInterval,
		 interval = 5000;

	arrows[0].addEventListener('click', function (e) {
		e = e || window.event;
		e.preventDefault();
		carouselCount -= 100;
		slider();
		if (e.type !== 'autoClick') {
			clearInterval(scrollInterval);
			scrollInterval = setInterval(autoScroll, interval);
		}
	});
	arrows[1].addEventListener('click', sliderEvent);
	arrows[1].addEventListener('autoClick', sliderEvent);
	
	function sliderEvent(e) {
		e = e || window.event;
		e.preventDefault();
		carouselCount += 100;
		slider();
		if (e.type !== "autoClick") {
			clearInterval(scrollInterval);
			scrollInterval = setInterval(autoScroll, interval);
		}
	}
	
	function slider() {
		switch (carouselCount) {
			case -100:
				carouselCount = 0;
				break;
			case 300:
				carouselCount = 0;
				break;
			default:
				break;
		}
		console.log(carouselCount);
		for (var i = 0; i < slides.length; i += 1) {
			slides[i].setAttribute('style', 'transform:translateX(-' + carouselCount + '%)');
		}
	}
	
	// create new Event to dispatch click for auto scroll
	var autoClick = new Event('autoClick');
	function autoScroll() {
		arrows[1].dispatchEvent(autoClick);
	}
	
	// set timing of dispatch click events
	scrollInterval = setInterval(autoScroll, interval);
	
})();












var el_default = document.querySelectorAll('.js-carousel');
for (var i = 0, l = el_default.length; i < l; i++) {
  new Flickity(el_default[i] , {
    arrowShape: {
      x0: 0,
      x1: 60, y1: 50,
      x2: 65, y2: 45,
      x3: 10
    },
    lazyLoad: 2,
    wrapAround: true,
    pageDots: true,
    selectedAttraction: 0.01,
    friction: 0.15,
    contain: true
  });
}


var el_testimonials = document.querySelector('.js-testimonials');
var testimonials = new Flickity(el_testimonials, {
  arrowShape: {
    x0: 0,
    x1: 60, y1: 50,
    x2: 65, y2: 45,
    x3: 10
  },
  lazyLoad: 1,
  pageDots: false,
  selectedAttraction: 0.01,
  friction: 0.15,
  contain: false
});










