$(document).ready(function(){
  $("#RechercheForm").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#MaTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

function openNav() {
    document.getElementById("mySidenav").style.width = "330px";
    document.getElementById("conteneur").style.marginLeft = "0px";
    document.getElementById("entete").style.backgroundColor = "white";
    document.getElementById("conteneur").style.width = "75%";
    document.getElementById("lien").style.backgroundColor  = "white";
    document.getElementById("lien").style.color = "#036873";
    document.getElementById("lien").onmouseover = function() {
    this.style.backgroundColor = "white";
}

}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("conteneur").style.marginLeft= "auto";
    document.getElementById('conteneur').style.width= '90%';
    document.getElementById("entete").style.backgroundColor = "#036873";
    document.getElementById("lien").style.color = "lightblue";
    document.getElementById("lien").style.backgroundColor = "#036873";
    document.getElementById("lien").onmouseover = function() {
    this.style.backgroundColor = "#036873";
}

}