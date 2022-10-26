let url = "https://swapi-api.hbtn.io/api/films/?format=json"
$(function() {
    $.get(url, function(data) {
        for (result in data.results){
          let movie = data.results
          for (let i = 0; i < movie.length; i++) {
            $('UL#list_movies').append('<li>' + movie[i].title + '</li>');
            }
        
         }
        }
        )

    }

)
