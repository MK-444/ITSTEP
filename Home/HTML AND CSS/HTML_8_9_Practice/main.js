var tabs = document.getElementsByClassName("tabs");
var tab = document.getElementsByClassName("tab");
for (var i = 0; i < tab.length; i++) {
    tab[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    if (current.length > 0) { 
        current[0].className = current[0].className.replace(" active", "");
    }
    this.className += " active";
    });
}