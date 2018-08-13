function getQueryVariable(variable)
{
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return pair[1]
}
var links = document.getElementsByClassName("navbar");
for(var i=0; i<links.length; i++) {
    var text = links[i].textContent;
    links[i].textContent = "";
    var a = document.createElement("a");
    a.href =text+".html?token=" + getQueryVariable('Token');
    a.textContent = text;
    links[i].appendChild(a);
}