preferedLanguage = getCookie("preferedTranslation");

if(preferedLanguage!=null){
	/*console.log("Cookies");
	console.log(preferedLanguage);*/
}
else{
	var userLang = navigator.language || navigator.userLanguage; 
	preferedLanguage = userLang.split('-')[0];
	//console.log(preferedLanguage);
}
moveToLanguage(preferedLanguage);

function translateWeb(flag){
	console.log(flag);
	setCookie("preferedTranslation",flag,365);
	moveToLanguage(flag);
}

function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  var expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return null;
}

function moveToLanguage(lang){
	//console.log("Redirect");
	url = window.location.href
	if((lang=='en' && url.includes('/en/')) || ((lang=='es' && !url.includes('/en/')))) 
		return;
	else if(lang=='en'){
		url = url.replace(".io/",".io/en/")
	}
	else{
		url = url.replace(".io/en/",".io/")
	}
	//console.log(url);
	window.location.href = url;
}