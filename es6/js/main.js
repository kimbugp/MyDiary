var fetch = require("node-fetch");
var myURL='http://127.0.0.1:5000';
var myheaders={'Content-Type': 'application/json'};
var init={method:'get',headers:myheaders};
var mybody=JSON.stringify({a: 7, str: 'Some string: &=&'})
fetch(myURL,init,mybody)
.then(res=>res.json()).then(res=>console.log(res));

// function to post signup info


//function to post signin info

// function to post an entry

//function to get all entries

// function to et individula entry

//function to delete an entry

//function to edit entry


//function to view profile
