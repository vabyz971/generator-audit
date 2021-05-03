/* ==== SHOW NAVBAR ==== */

const showNavBar = (toggleId, navId, bodyId, headerId) => {
    const toggle = document.getElementById(toggleId),
      nav = document.getElementById(navId),
      bodypd = document.getElementById(bodyId),
      headerpd = document.getElementById(headerId)
  
    if (toggle && nav && bodypd && headerpd) {
      toggle.addEventListener("click", () => {
  
          // Show navBar
          nav.classList.toggle('show');
          
          // Change Icon
          toggle.classList.toggle('bx-x');
  
          //add padding to body
          bodypd.classList.toggle('body-pd');
          
          //add padding to header
          headerpd.classList.toggle('body-pd');
      });
    }
  };
  
  
  showNavBar('header-toggle','nav-bar', 'body-pd', 'header');