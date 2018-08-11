
// var fetch = require("node-fetch");
function submitForm(e, form){
    e.preventDefault();
    var body={
        method: 'post',
        body: JSON.stringify({name: form.username.value, password: form.password.value})};
    fetch(body)
    .then(function(response){return response.json();})
    .then(function(data) {alert('form submited')});
        // var mybody=JSON.stringify({
        //     "username": "petersimn",
        //     "password": "12345678"
        // })
    //   return data;
}
function hello_world(){
    var base='http://127.0.0.1:5000';
    var myheaders={'Content-Type': 'application/json'};
    var init={method:'get',headers:myheaders};
    fetch(base,init)
    .then(res=>res.json())
    .then(res=>console.log(res));
}

// function to post signup info
function create_user(){
    var mybody=JSON.stringify({
        "username": "petersimn",
        "name": "Simon Peter",
        "email": "kimbuge@gmail.com",
        "password": "12345678"
    })
    var myURL='http://127.0.0.1:5000/api/v1/auth/signup';
    var myheaders={'Content-Type': 'application/json'};
    var init={method:'POST',headers:myheaders,body:mybody};
    fetch(myURL,init)
    .then(res=>res.json()).then(res=>console.log(res))
    .catch(error => console.error(`Fetch Error =\n`, error));
}
function login(){
    var mybody=submitForm();
    var myURL='http://127.0.0.1:5000/api/v1/auth/login';
    var myheaders={'Content-Type': 'application/json'};
    var init={method:'POST',headers:myheaders,body:mybody};
    fetch(myURL,init)
    .then(res=>res.json()).then(res=>console.log(res))
    .catch(error => console.error(`Fetch Error =\n`, error));
}
//function to post signin info

// function to post an entry

//function to get all entries

// function to et individula entry

//function to delete an entry

//function to edit entry


//function to view profile
