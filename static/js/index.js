var formElement = document.querySelector("form")
var request = new XMLHttpRequest();
request.open('POST', "suibmitform.php");
request.send(new FormData(formElement));