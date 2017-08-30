
$( document ).ready(function() {
    $.get('/getBestItems', function(results){

      $('#bestItems').html("");
      for(result of results['new_results']){
           var result_image = "<div class='col-md-3 resultBoxhl'><img src='" + result.image + "' class='border' height='200' width='200'></div>";
        $('#bestItems').append(result_image);       
      }


})


$('#searchButton').on('click', function(evt){
  evt.preventDefault();
  console.log("we are running");
    var searchTerm = $('#searchClothing').val();
    console.log(searchTerm);
    $.get('/searchData?searchClothing=' + searchTerm, function(results){
      $('#results').html("");
   /*for (result of results['new_results']){
        var result_div = "<div class='col-md-4 resultBoxhl'><form action='/save' method='post'><input name='product_id' type='hidden' value="+ result.id +"><input type='submit' value='Save Search Results'><input type='hidden' name='search_term' id='search_term' value='" + searchTerm + "'></form>" + result.name + "<img src='" + result.image + "'></div>";
        $('#results').append(result_div);
      }*/

      for (result of results['new_results']){
        var result_div = "<div class='col-md-3 resultBoxhl'><img src='" + result.image + "' class='border' data-result-id='" + result.id +  "' data-search-term='" + searchTerm + "'></div>";
        $('#results').append(result_div);
      }

        $(".resultImg").click(function(evt){

    var resultId = $(this).data("resultId");
    var searchTerm = $(this).data("searchTerm");
    var formData = {'result_id': resultId, 'search_term': searchTerm};

    $.post("/save", formData, function(results){

      //document.location.href = '/display';        
        $('.resultImg').click(function() {
        var id = $('img', this).attr('src');
        //console.log(id);
        $(this).attr('src', '../static/green-check-mark.svg');
        });

    });


  });


      $('#bestItems').html("");
      /*for(result of results['other_results']){
           var result_div = "<div>" + result.name + "<form action='/save' method='post'><input name='product_id' type='hidden' value="+ result.id +"><input type='submit' value='Save Search Results'><input type='hidden' name='search_term' id='search_term' value='" + searchTerm + "'></form></div>";
        $('#bestItems').append(result_div);

      }*/


}) //end of .get
});//end of searchButton on click





$('#seeNextTen').on('click', function(evt){
  evt.preventDefault();
  console.log("we are running");
    //var searchTerm = $('#searchClothing').val();
    $.get('/seeNextTen', function(results){

      $('#myOwnCarousel').html("");
      for(result of results['new_image_results']){
           var result_image = "<img src='" + result.image + "'>";
        $('#myOwnCarousel').append(result_image);       
      }


}) //end of .get
    $("#myOwnCarousel").css("margin-left","0px");

    $("#myOwnCarousel").animate({ 


        marginLeft: "+=150px",
    }, 1000 );

});//end of seeNextTen on click

$("#seeNextTen").click();

});//end of document ready


