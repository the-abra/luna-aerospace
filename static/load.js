const iframe = document.getElementById('iframe');
  
  // Event listener to check when the iframe content is loaded
iframe.onload = function() {
    // Hide the loading animation once iframe content is loaded
    document.querySelector('.thing').style.display = 'none';
    
    // Show the content and the iframe
    document.querySelector('.content').style.display = 'block';
    iframe.style.display = 'block';
  };
