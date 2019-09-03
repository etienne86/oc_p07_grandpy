

var pElt = document.createElement("p");
pElt.setAttribute("class", "bot_reply");


titreLien.textContent = {{ bot.welcome_message() }};
titreLien.href = unLien.url;
titreLien.setAttribute("style", "color: #428bca; font-weight: bold; text-decoration: none;");
pElt.appendChild(titreLien);

var spanElt = document.createElement("span");
spanElt.style.color = "black";
spanElt.style.fontWeight = "normal";

var brElt = document.createElement("br");

spanElt.appendChild(document.createTextNode(" " + unLien.url));
spanElt.appendChild(brElt);
spanElt.appendChild(document.createTextNode("Ajouté par " + unLien.auteur));
pElt.appendChild(spanElt);

document.getElementById("contenu").appendChild(pElt);

