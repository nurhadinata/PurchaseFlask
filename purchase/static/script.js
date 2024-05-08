var isNavbarExpanded = sessionStorage.getItem('navbarExpanded')=="true";
console.log(sessionStorage.getItem('navbarExpanded'));
if(isNavbarExpanded && window.innerWidth >= 768){
    const showNavbar = (toggleId, navId, bodyId, headerId) =>{
        const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId),
        bodypd = document.getElementById(bodyId),
        headerpd = document.getElementById(headerId)
        
        // Validate that all variables exist
        if(toggle && nav && bodypd && headerpd){    
            // show navbar
            const isNavbarExpanded = nav.classList.toggle('show')
            sessionStorage.setItem('navbarExpanded', isNavbarExpanded);
            console.log(sessionStorage.getItem('navbarExpanded'));
            // change icon
            toggle.classList.toggle('bx-x')
            // add padding to body
            bodypd.classList.toggle('body-pd')
            // add padding to header
            headerpd.classList.toggle('body-pd')
        }
    }
        
    showNavbar('header-toggle','nav-bar','body-pd','header')
}

var selectedMenu = document.getElementById('selected-menu').innerText

if(selectedMenu=="farmer-list"){
    const filterBtn = document.getElementById("input-filter")

    if(filterBtn){
        filterBtn.addEventListener('click', ()=>{
            const toggleInput= document.querySelectorAll('.toggle-input')
            if(toggleInput){
                toggleInput.forEach(l=> l.classList.toggle('hidden'))
            }
        })
    }
}

window.addEventListener('click', function(event) {
    const showNavbar2 = (toggleId, navId, bodyId, headerId) =>{
        const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId),
        bodypd = document.getElementById(bodyId),
        headerpd = document.getElementById(headerId)
        
        // Validate that all variables exist
        if (!nav.contains(event.target) && window.innerWidth <= 768 && !toggle.contains(event.target)) {
            // Close the navbar
            isNavbarExpanded = nav.classList.remove('show')
              sessionStorage.setItem('navbarExpanded', isNavbarExpanded);
              
              // change icon
              toggle.classList.remove('bx-x')
              // add padding to body
              bodypd.classList.remove('body-pd')
              // add padding to header
              headerpd.classList.remove('body-pd')
          }
          
    }
    showNavbar2('header-toggle','nav-bar','body-pd','header')
        
    // Check if the clicked element is not inside the navbar
  });

document.addEventListener("DOMContentLoaded", function(event) {
   
    const showNavbar = (toggleId, navId, bodyId, headerId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId),
    bodypd = document.getElementById(bodyId),
    headerpd = document.getElementById(headerId)
    
    // Validate that all variables exist
    if(toggle && nav && bodypd && headerpd){
        toggle.addEventListener('click', ()=>{
        // show navbar
        isNavbarExpanded = nav.classList.toggle('show')
        sessionStorage.setItem('navbarExpanded', isNavbarExpanded);
        
        // change icon
        toggle.classList.toggle('bx-x')
        // add padding to body
        bodypd.classList.toggle('body-pd')
        // add padding to header
        headerpd.classList.toggle('body-pd')
    })
    }
    }
    
    showNavbar('header-toggle','nav-bar','body-pd','header')
    
    /*===== LINK ACTIVE =====*/
    const linkColor = document.querySelectorAll('.nav_link')
    
    function colorLink(){
        if(linkColor){
            linkColor.forEach(l=> l.classList.remove('active'))
            this.classList.add('active')
        }
        
    }
    linkColor.forEach(l=> l.addEventListener('click', colorLink))
    
     // Your code to run since DOM is loaded and ready
    });

    $(document).ready(function() {
        
        const linkColor = document.querySelectorAll('.nav_link')
        
        var selectedMenu = document.getElementById('selected-menu').innerText
        
        if(selectedMenu){
            if(selectedMenu=="home"){
                linkColor.forEach(l=> l.classList.remove('active'))
                var selectedNav = document.getElementById('nav_home')
                selectedNav.classList.add('active');
            }else if(selectedMenu=="farmer-list"){
                linkColor.forEach(l=> l.classList.remove('active'))
                var selectedNav = document.getElementById('nav_farmer_list')
                selectedNav.classList.add('active');
            }else if(selectedMenu=="list"){
                linkColor.forEach(l=> l.classList.remove('active'))
                var selectedNav = document.getElementById('nav_purchase_list')
                selectedNav.classList.add('active');
            }else if(selectedMenu=="report"){
                linkColor.forEach(l=> l.classList.remove('active'))
                var selectedNav = document.getElementById('nav_purchase_report')
                selectedNav.classList.add('active');
            }
        }
        // $('#purchase-status').select2();

        var today = new Date();

        // Format the date as "YYYY-MM-DD"
        var yyyy = today.getFullYear();
        var mm = String(today.getMonth() + 1).padStart(2, '0');
        var dd = String(today.getDate()).padStart(2, '0');
        var formattedDate = yyyy + '-' + mm + '-' + dd;

        // Set the input field's value to today's date
        dateInput = document.getElementById('dateInput');
        if(dateInput){
            dateInput.value = formattedDate;
        }
        
    });

