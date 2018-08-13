var baseurl="https://simondb.herokuapp.com";
var Token=sessionStorage.getItem("Token");
var modal = document.getElementById('myModal');
function get_entries(){
    var myURL=baseurl+'/api/v1/entries';
    var myheaders={'Content-Type': 'application/json','Accept': 'application/json','Token':Token};
    var init={method:'GET',headers:myheaders};
    return fetch(myURL,init)
    .then((response) => response.json())
    .then((responseData) => {
      return responseData;
    })
    .catch(error => console.error(`Fetch Error =\n`, error));
}
// get_entries().then(response => console.log(response));
function show_data(){
    get_entries().then(response =>{
        object=response.entries;
        objectlength=object.length;
        for (var i = 0; i < objectlength; i++){
            //make list of entry titles
            var title=object[i].entry_name;
            var content=object[i].entry_content;
            var d=object[i].entry_date;
            var id=object[i].entry_id;
            var record = document.createElement('li');
            record.setAttribute('id','id'+i);
            record.appendChild(document.createTextNode(title));
            document.getElementById('myUL').appendChild(record);
            
            record.onclick=function(){
                modal.style.display = "block";
                document.getElementById('entry_title').innerHTML=title;
                document.getElementById('entry_content').innerHTML=content;
                document.getElementById('date').innerHTML=d;
            }
                    // Get the modal
            // Get the <span> element that closes the modal
            var span = document.getElementsByClassName("close")[0];
            span.onclick = function() {
                modal.style.display = "none";
            }
            // edit  functionality
            var button = document.getElementsByClassName("action")[0];
            button.onclick =function(){
                console.log('edited');
            }
            // When the user clicks anywhere outside of the modal, close it
            window.onclick = function(event) {
                if (event.target == modal) {
                    modal.style.display = "none";
                }
            }
            var item=document.getElementById('id'+i);
            // item.removeChild(item.parentNode);
            var button = document.getElementsByClassName("action")[1];
            button.onclick =function(){
                console.log('deleted');
                delete_entry(id);
                
            }   
        }
    })
    
}
var links = document.getElementsByClassName("navbar");
//set the html links
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
    .then(function(){
        modal.style.display = "none";
        location.reload();
    })
    .catch(error => console.error(`Fetch Error =\n`, error));
    return false;
}

show_data();