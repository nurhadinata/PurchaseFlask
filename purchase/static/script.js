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

function testFunction(eventId){

        const testCol = document.querySelectorAll('.event-info'+eventId)
        
        if(testCol){
            testCol.forEach(l=> l.classList.toggle('hidden'))
        }
            // add padding to body
}

function updateEvent(eventId){
    var fund = document.getElementById("fund-update"+eventId).value
    var cashier = document.getElementById("cashier-update"+eventId).value
    var purchaser = document.getElementById("purchaser-update"+eventId).value

    var updatedData = {
        id: eventId, 
        fund: fund,
        cashier: cashier,
        purchaser: purchaser
    };
    
    // Send POST request to update data
    $.ajax({
        url: '/purchase/event/update',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(updatedData),
        success: function(response) {
            // Request was successful, handle response here
            document.getElementById("fund-info"+eventId).innerHTML = fund
            document.getElementById("cashier-info"+eventId).innerHTML = cashier
            document.getElementById("purchaser-info"+eventId).innerHTML = purchaser
            console.log(response.message);
        },
        error: function(xhr, status, error) {
            // Request failed
            console.error('Request failed: ' + error);
        }
    });

    testFunction(eventId)


    // console.log(fund)

}

function cancelUpdateEvent(eventId){
    document.getElementById("fund-update"+eventId).value = document.getElementById("fund-info"+eventId).innerHTML.trim()
    document.getElementById("cashier-update"+eventId).value = document.getElementById("cashier-info"+eventId).innerHTML.trim()
    document.getElementById("purchaser-update"+eventId).value = document.getElementById("purchaser-info"+eventId).innerHTML.trim()

    testFunction(eventId)
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
        $('.selectpicker').selectpicker();
        
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

