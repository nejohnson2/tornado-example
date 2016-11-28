$(document).ready(function () {
	url = '<url>.com/api';

	//get_data();

});  

// example function to get data from api
function get_data() {
  $.getJSON(url, function (data) {
    console.log(data);
  });
}
