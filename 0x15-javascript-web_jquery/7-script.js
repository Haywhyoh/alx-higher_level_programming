let url = "https://swapi-api.hbtn.io/api/people/5/?format=json"
$(function(){
  $.get(url, function(data){
    $("#character").text(data.name)
  })
}
)
