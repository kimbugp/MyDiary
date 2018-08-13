var baseurl="https://simondb.herokuapp.com";
var Token=sessionStorage.getItem("Token");
function get_entries(){
    var myURL=baseurl+'/api/v1/entries';
    var myheaders={'Content-Type': 'application/json','Accept': 'application/json','Token':Token};
    var init={method:'GET',headers:myheaders};
    fetch(myURL,init)
    .then(function(response){
        return response.json();
    })
    .then(function(json){
        var object=json;
        var objectlength=object.entries.length;
        for (var i = 0; i < objectlength; i++) {
            show_data(object.entries[i].entry_name,object.entries[i].entry_date,object.entries[i].entry_content,object.entries[i].entry_id);
        }
    })
    .catch(error => console.error(`Fetch Error =\n`, error));
    return false;
}
function show_data(title,d,content,id){
    var record = document.createElement('li');
    record.appendChild(document.createTextNode(title));
    document.getElementById('myUL').appendChild(record);
    // Get the modal
    var modal = document.getElementById('myModal');
    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];
    record.onclick=function(){
        modal.style.display = "block";
        document.getElementById('entry_title').innerHTML=title;
        document.getElementById('entry_content').innerHTML=content;
        document.getElementById('date').innerHTML=d;
    }
    span.onclick = function() {
        modal.style.display = "none";
    }
    // edit  functionality
    var button = document.getElementsByClassName("action")[0];
    button.onclick =function(){
        console.log('edited');
    }
    //delete  functionality
    var button = document.getElementsByClassName("action")[1];
    button.onclick =function(){
        console.log('deleted');
        delete_entry(id);
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}
var links = document.getElementsByClassName("navbar");
for(var i=0; i<links.length; i++) {
    var text = links[i].textContent;
    links[i].textContent = "";
    var a = document.createElement("a");
    a.href =text.toLowerCase()+".html";
    a.textContent = text;
    links[i].appendChild(a);
}
function delete_entry(entry_id){
    var myURL=baseurl+'/api/v1/entries/'+entry_id;
    var myheaders={'Content-Type': 'application/json','Accept': 'application/json','Token':Token};
    var init={method:'DELETE',headers:myheaders};
    fetch(myURL,init)
    .then(function(response){
        return response.json();
    })
    .then(function(json){
        alert(json);
    })
    .catch(error => console.error(`Fetch Error =\n`, error));
    return false;
}
    
get_entries();