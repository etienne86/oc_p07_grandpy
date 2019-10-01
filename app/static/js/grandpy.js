///////////////////////////////////////////////////////////////////////////////
//                        WELCOME MESSAGE FROM THE BOT                       //
///////////////////////////////////////////////////////////////////////////////

var divElt = document.createElement("div");
divElt.setAttribute("class", "bot_reply");
var welcome = document.getElementById("js_02").getAttribute("wlcmMsg");
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
    var divQuestElt = document.createElement("div");
    divQuestElt.setAttribute("class", "user_question");
    divQuestElt.textContent = question;
    document.getElementById("dialogue").appendChild(divQuestElt);
    // empty the textarea (inside the form)
    var formElt = document.getElementById("form");
    formElt.reset();
    // show the 'loader' image
    var divLoaderElt = document.createElement("div");
    divLoaderElt.id = "loader";
    divLoaderElt.innerHTML = "<img src='../static/img/loader.gif' alt='chargement...' />";
    document.getElementById("dialogue").appendChild(divLoaderElt);
    // send data to the server
    $.post( "/postmethod", {
        entered_data: JSON.stringify(question)
    }, function (err, req, resp) {
        var phrases = resp["responseJSON"]["phrases"];
        // display either the address (if the question was understood)
        // or the reason why the bot did not understand the question
        var divBotElt = document.createElement("div");
        divBotElt.setAttribute("class", "bot_reply");
        divBotElt.textContent = phrases[0];
        document.getElementById("dialogue").appendChild(divBotElt);
        // if the question was understood by the bot
        if (phrases.length !== 1) {
            // display the map
            var divMapElt = document.createElement("div");
            divMapElt.setAttribute("class", "map");
            document.getElementById("dialogue").appendChild(divMapElt);
            var myMap = resp["responseJSON"]["map"];
            var myLat = myMap.lat;
            var myLng = myMap.lng;
            var myTitle = myMap.title;
            var myZoom = myMap.zoom;
            displayMap(myLat, myLng, myZoom, myTitle);
            map_number = map_number + 1;
            // display the short story (from wikipedia)
            var divBotElt = document.createElement("div");
            divBotElt.setAttribute("class", "bot_reply");
            divBotElt.textContent = phrases[1];
            document.getElementById("dialogue").appendChild(divBotElt);
        }
        // hide the 'loader' image
        var divEmptyLoaderElt = document.createElement("div");
        divEmptyLoaderElt.innerHTML = "";
        document.getElementById("dialogue").replaceChild(divEmptyLoaderElt, divLoaderElt);
    });
});

// the following function is provided in the Google API documentation
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
