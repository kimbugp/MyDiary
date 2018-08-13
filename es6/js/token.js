var links = document.getElementsByClassName("navbar");
for(var i=0; i<links.length; i++) {
    var text = links[i].textContent;
    links[i].textContent = "";
    var a = document.createElement("a");
    a.href =text+".html";
    a.textContent = text;
    links[i].appendChild(a);
}