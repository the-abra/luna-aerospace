const iframe = document.getElementById('iframe');
  
  // Event listener to check when the iframe content is loaded
  iframe.onload = function() {
    // Hide the loading animation once iframe content is loaded
    document.getElementById('thing').style.display = 'none';
    
    // Show the content and the iframe
    iframe.style.display = 'block';
  };