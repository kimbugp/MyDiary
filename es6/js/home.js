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
        document.body.onload=create_div;
        // document.getElementById("data").innerHTML =object.entries[0].entry_content;
    })
    .catch(error => console.error(`Fetch Error =\n`, error));
    return false;
}
function create_div(){
    var record = document.createElement("div");
    record.classList.add('column');

    var name = document.createElement("h3");
    var date = document.createElement("div");
    var content = document.createElement("p");

    var textnode = document.createTextNode("fghhgfdfgh");
    var test = document.createTextNode("cvbnmvcxcvbnvcx");
    var tests = document.createTextNode("cvbnmvcxcvbnvcx");

    name.appendChild(textnode);
    date.appendChild(test);
    content.appendChild(tests);

    record.appendChild(name);
    record.appendChild(date);
    record.appendChild(content);

    document.getElementById('row').appendChild(record);

    return false;
}
create_div();