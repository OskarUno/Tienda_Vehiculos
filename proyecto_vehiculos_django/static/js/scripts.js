document.addEventListener("DOMContentLoaded", function(){
var nav_links = document.querySelectorAll("nav a");

//Cambiar color de fondo de los links
nav_links.forEach(function(link){
    link.addEventListener("mouseover", function(){
        link.style.backgroundColor = "blue";
        link.style.color = "white"
        console.log("aqui");
        
    });

    link.addEventListener("mouseout", function(){
        link.style.backgroundColor = "";
        link.style.color = "black"
    });

});


const showAlertButton = document.getElementById('show-alert');
if(showAlertButton){
    showAlertButton.addEventListener('click', function(){
        alert("Presionaste el boton");
    })
}

});





