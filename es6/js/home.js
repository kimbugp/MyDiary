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
        var objectlength=object.entries.length;
        for (var i = 0; i < objectlength; i++) {
            show_data(object.entries[i].entry_name);
            // for (const [key, value] of Object.entries(object.entries[i])) {
            //     // console.log(key,value);
            //     show_data(value);
            //   }
        }
    })
    .catch(error => console.error(`Fetch Error =\n`, error));
    return false;
}
function show_data(value){
    var record = document.createElement('li');
    record.appendChild(document.createTextNode(value));
    document.getElementById('myUL').appendChild(record);
}

get_entries();
var arrayVariable = ["one", "two", "three"];
var arrayLength = arrayVariable.length;
var temp;

// for (i = 0; i < arrayLength; i++) {
//   temp = document.createElement('div');
//   temp.className = 'results';
//   temp.innerHTML = arrayVariable[i];
//   document.getElementsByTagName('body')[0].appendChild(temp);
// }

