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

function get_entries(){
    var myURL='http://127.0.0.1:5000/api/v1/entries';
    var myheaders={'Content-Type': 'application/json','Accept': 'application/json','Token':getQueryVariable('Token')};
    var init={method:'GET',headers:myheaders};
    fetch(myURL,init)
    .then(function(response){
        return response.json();
    })
    .then(function(json){
        var object=json;
        for(var[value] of Object.entries(object)){
            console.log(value);
         }
        return json
    })
    .catch(error => console.error(`Fetch Error =\n`, error));
    return false;
}
