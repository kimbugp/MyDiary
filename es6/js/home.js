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

    // Get the modal
    var modal = document.getElementById('myModal');
    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    record.onclick=function(){
        modal.style.display = "block";
    }
    span.onclick = function() {
        modal.style.display = "none";
    }
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}
get_entries();