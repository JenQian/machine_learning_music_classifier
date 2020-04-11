var button = d3.select("#song-btn");

button.on("click", function() {
 
    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#song_input");
  
    // Get the value property of the input element
    var inputValue = inputElement.property("value");
  
    console.log(inputValue);
  

    
});