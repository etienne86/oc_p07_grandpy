///////////////////////////////////////////////////////////////////////////////
//                        WELCOME MESSAGE FROM THE BOT                       //
///////////////////////////////////////////////////////////////////////////////

var divElt = document.createElement("div");
divElt.setAttribute("class", "bot_reply");
var welcome = document.getElementById("js_01").getAttribute("wlcmMsg");
divElt.textContent = welcome;
document.getElementById("dialogue").appendChild(divElt);


///////////////////////////////////////////////////////////////////////////////
//         MANAGE THE EVENT 'SUBMIT' WHEN CLICKING ON BUTTON 'Envoyer'       //
///////////////////////////////////////////////////////////////////////////////

var map_number = 0;

var form = document.querySelector("form");
form.addEventListener("submit", function (e) {
    e.preventDefault();
    // add the user question into the dialogue (i.e. display the user question)
    var question = form.elements.user_input.value;
    var divElt = document.createElement("div");
    divElt.setAttribute("class", "user_question");
    divElt.textContent = question;
    document.getElementById("dialogue").appendChild(divElt);
    // empty the textarea (inside the form)
    var formElt = document.getElementById("form");
    formElt.reset();
    // send data to the server
    $.post( "/postmethod", {
        entered_data: JSON.stringify(question)
    }, function (err, req, resp) {
        var phrases = resp["responseJSON"]["phrases"];
        // display either the address (if the question was understood)
        // or the reason why the bot did not understand the question
        divElt = document.createElement("div");
        divElt.setAttribute("class", "bot_reply");
        // divElt.textContent = phrases;
        divElt.textContent = phrases[0];
        document.getElementById("dialogue").appendChild(divElt);
        // if the question was understood by the bot
        if (phrases.length !== 1) {
            // display the map
            var divElt = document.createElement("div");
            divElt.setAttribute("class", "map");
            document.getElementById("dialogue").appendChild(divElt);
            var myMap = resp["responseJSON"]["map"];
            var myLat = myMap.lat;
            var myLng = myMap.lng;
            var myTitle = myMap.title;
            var myZoom = myMap.zoom;
            displayMap(myLat, myLng, myZoom, myTitle);
            map_number = map_number + 1;
            // display the short story (from wikipedia)
            divElt = document.createElement("div");
            divElt.setAttribute("class", "bot_reply");
            divElt.textContent = phrases[1];
            document.getElementById("dialogue").appendChild(divElt);
        }
    });
});

function displayMap(myLat, myLng, myZoom, myTitle) {
    var myLatLng = {lat: myLat, lng: myLng};

    var map = new google.maps.Map(document.getElementsByClassName('map')[map_number], {
        zoom: myZoom,
        center: myLatLng
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: myTitle
    });
}

// function getData(question) {
//     $.post( "/postmethod", {
//         entered_data: JSON.stringify(question)
//     });
// }




///////////////////////////////////////////////////////////////////////////////
//                              DISPLAY THE MAP                              //
///////////////////////////////////////////////////////////////////////////////

// var divElt = document.createElement("div");
// divElt.setAttribute("class", "map");
// document.getElementById("dialogue").appendChild(divElt);

// // passing the python variables to the map
// var myLat = Number(document.getElementById("js_01").getAttribute("lat"));
// var myLng = Number(document.getElementById("js_01").getAttribute("lng"));
// var myZoom = Number(document.getElementById("js_01").getAttribute("zoom"));
// var myTitle = document.getElementById("js_01").getAttribute("markerTitle");

// function initMap() {
//     var myLatLng = {lat: myLat, lng: myLng};

//     var map = new google.maps.Map(document.getElementsByClassName('map')[0], {
//         zoom: myZoom,
//         center: myLatLng
//     });

//     var marker = new google.maps.Marker({
//         position: myLatLng,
//         map: map,
//         title: myTitle
//     });
// }

