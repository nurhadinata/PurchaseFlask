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
    var cashier_id = document.getElementById("cashier-update"+eventId).value
    var purchaser_id = document.getElementById("purchaser-update"+eventId).value

    var updatedData = {
        id: eventId, 
        fund: fund,
        cashier_id: cashier_id,
        purchaser_id: purchaser_id
    };
    
    // Send POST request to update data
    $.ajax({
        url: '/purchase/event/update',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(updatedData),
        success: function(response) {
            // Request was successful, handle response here
            document.getElementById("fund-info"+eventId).innerHTML = response.fund.toFixed(2)
            document.getElementById("cashier-info"+eventId).innerHTML = response.cashier
            document.getElementById("purchaser-info"+eventId).innerHTML = response.purchaser
            document.getElementById("cashier-id"+eventId).innerHTML = cashier_id
            document.getElementById("purchaser-id"+eventId).innerHTML = purchaser_id
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
    var cashier_select = document.getElementById("cashier-update"+eventId);
    cashier_select.value = parseInt(document.getElementById("cashier-id"+eventId).innerHTML.trim())

    var purchaser_select = document.getElementById("purchaser-update"+eventId);
    purchaser_select.value = parseInt(document.getElementById("purchaser-id"+eventId).innerHTML.trim())

    document.getElementById("fund-update"+eventId).value = document.getElementById("fund-info"+eventId).innerHTML.trim()

    $(cashier_select).selectpicker('refresh')
    $(purchaser_select).selectpicker('refresh')
    
    testFunction(eventId)
}

function editTransaction(transactionId){

    const tCol = document.querySelectorAll('.transaction-info'+transactionId)
    
    if(tCol){
        tCol.forEach(l=> l.classList.toggle('hidden'))
    }
        // add padding to body
}

function updateTransaction(transactionId){
    var purchase_order_id = document.getElementById("po-update"+transactionId).value
    var purchase_event_id = document.getElementById("event-update"+transactionId).value
    var farmer_id = document.getElementById("farmer-update"+transactionId).value
    var price_unit = document.getElementById("price-update"+transactionId).value
    var qty = document.getElementById("qty-update"+transactionId).value

    var updatedData = {
        id: transactionId, 
        purchase_order_id: purchase_order_id,
        purchase_event_id: purchase_event_id,
        farmer_id: farmer_id,
        price_unit: price_unit,
        qty: qty
    };
    
    // Send POST request to update data
    $.ajax({
        url: '/purchase/transaction/update',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(updatedData),
        success: function(response) {
            // Request was successful, handle response here
            document.getElementById("po-info"+transactionId).innerHTML = response.po
            document.getElementById("event-info"+transactionId).innerHTML = response.event
            document.getElementById("farmer-info"+transactionId).innerHTML = response.farmer
            document.getElementById("po-id"+transactionId).innerHTML = purchase_order_id
            document.getElementById("event-id"+transactionId).innerHTML = purchase_event_id
            document.getElementById("farmer-id"+transactionId).innerHTML = farmer_id
            document.getElementById("price-info"+transactionId).innerHTML = response.price_unit.toFixed(2)
            document.getElementById("qty-info"+transactionId).innerHTML = response.qty.toFixed(0)
            document.getElementById("subtotal-info"+transactionId).innerHTML = response.subtotal.toFixed(2)
            console.log(response.message);
        },
        error: function(xhr, status, error) {
            // Request failed
            console.error('Request failed: ' + error);
        }
    });

    editTransaction(transactionId)


    // console.log(fund)

}

function cancelUpdateTransaction(transactionId){
    var po_select = document.getElementById("po-update"+transactionId);
    po_select.value = parseInt(document.getElementById("po-id"+transactionId).innerHTML.trim())
    
    var event_select = document.getElementById("event-update"+transactionId)
    event_select.value = parseInt(document.getElementById("event-id"+transactionId).innerHTML.trim())
    
    var farmer_select = document.getElementById("farmer-update"+transactionId)
    farmer_select.value = parseInt(document.getElementById("farmer-id"+transactionId).innerHTML.trim())

    document.getElementById("price-update"+transactionId).value = parseFloat(document.getElementById("price-info"+transactionId).innerHTML.trim()).toFixed(2)
    document.getElementById("qty-update"+transactionId).value = parseFloat(document.getElementById("qty-info"+transactionId).innerHTML.trim()).toFixed(0)
    
    $(po_select).selectpicker('refresh')
    $(event_select).selectpicker('refresh')
    $(farmer_select).selectpicker('refresh')

    editTransaction(transactionId)
}

function getPO(){
    var po = $('#purchase-order').val();
    var relativeURL = '/purchase/cashier' +
                        '?po=' + po;
    // Use window.open to open the new page
    window.location.href = location.origin + relativeURL;

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

    function createPagination(totalPages, currentPage, pageLink) {
        let paginationHTML = '<ul class="pagination">';
        const delta = 2;
        const left = currentPage - delta;
        const right = currentPage + delta + 1;
        const range = [];
        const rangeWithDots = [];
        let l;

        for (let i = 1; i <= totalPages; i++) {
            if(currentPage<6){
                if (i < 8 || i === totalPages || (i >= left && i < right)) {
                    range.push(i);
                }
            }else if(totalPages-currentPage<5){
                if (i === 1 || i > totalPages-7 || (i >= left && i < right)) {
                    range.push(i);
                }
            }else{
                if (i === 1 || i === totalPages || (i >= left && i < right)) {
                    range.push(i);
                }
            }
            // if (i === 1 || i === totalPages || (i >= left && i < right)) {
            //     range.push(i);
            // }
        }

        for (let i of range) {
            if (l) {
                if (i - l === 2) {
                    rangeWithDots.push(l + 1);
                } else if (i - l !== 1) {
                    rangeWithDots.push('...');
                }
            }
            rangeWithDots.push(i);
            l = i;
        }

        if(currentPage!=1){
            paginationHTML += `<li><a href="${pageLink}${currentPage-1}"><i class='bx bx-chevron-left'></i></a></li>`;
        }

        rangeWithDots.forEach(page => {
            if (page === '...') {
                paginationHTML += `<li><a class="disabled">...</a></li>`;
            } else {
                paginationHTML += `<li><a class="${page === currentPage ? 'active' : ''}" href="${pageLink}${page}">${page}</a></li>`;
            }
        });

        if(currentPage!=totalPages){
            paginationHTML += `<li><a href="${pageLink}${currentPage+1}"><i class='bx bx-chevron-right'></i></a></li>`;
        }

        paginationHTML += '</ul>';
        return paginationHTML;
    }

    const paginationContainer = document.getElementById('pagination');
    if(paginationContainer){
        const totalPages = parseInt(document.getElementById('total-page').innerHTML.trim());
        const currentPage = parseInt(document.getElementById('current-page').innerHTML.trim());
        const pageLink = document.getElementById('pagination-link').innerHTML.trim();
        paginationContainer.innerHTML = createPagination(totalPages, currentPage, pageLink);
    }

    console.log(sessionStorage.getItem('fullscreen'))


    document.getElementById('fullscreenButton').addEventListener('click', function() {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen();
        } else {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            }
        }
        sessionStorage.setItem('fullscreen', !document.fullscreenElement ? 'true' : 'false');
        console.log(sessionStorage.getItem('fullscreen'))
        console.log(document.fullscreenElement)
    });

    document.getElementById('reloadButton').addEventListener('click', function() {
        location.reload();
    });

    

    // Add event listener for pagination clicks (optional)
    // paginationContainer.addEventListener('click', (e) => {
    //     if (e.target.tagName === 'A' && !e.target.classList.contains('disabled') && !e.target.classList.contains('active')) {
    //         e.preventDefault();
    //         const newPage = parseInt(e.target.textContent);
    //         paginationContainer.innerHTML = createPagination(totalPages, newPage);
    //     }
    // });
   
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

            // select all selectpicker that contains class populateJSON and initialize selectpicker
            var selectElements = $('.populateJSON').selectpicker();

            // Attach the event handler to the 'changed.bs.select' event for select elements with the 'selectpicker' class
            selectElements.on('shown.bs.select', function(e) {
                var selector = $(this);
                var parentClassName = selector.attr('class').split(' ');
                var dataNameJSONClass = parentClassName[parentClassName.length - 1];
                var firstPrevSelect = selector.find('option:selected').prop('outerHTML');

                // Find the search input within the Bootstrap Select dropdown relative to the current select element
                var searchBoxElement = $(this).parent().find('.bs-searchbox > input');

                // set typing timeout and minLength character in input
                var timeout = null;
                var typingTime = 250; // milliseconds
                var minLength = 0;
                var previousInput = ' ';
                                    // when user type in selectpicker searchbox
                searchBoxElement.keyup(function(event) {
                    clearTimeout(timeout);
                    timeout = setTimeout(() => {
                        var inputValue = $(this).val().trim();
                        if (inputValue.length >= minLength == previousInput !== inputValue) {
                            previousInput = inputValue;
                            $.ajax({
                                url: '/' + dataNameJSONClass, // e.g. 'get_data_products'
                                method: 'GET',
                                dataType: 'json',
                                async: true,
                                cache: {
                                    expires: 60000 // 60 second cache
                                },
                                data: { q: inputValue , user_id: $('#user_filter_form').val()},
                                success: function(response) {
                                    const optionsHTML = response.map(
                                        ({ id, text }) => `<option value="${id}">${text}</option>`
                                    ).join('');
                                    selector.empty();
                                    selector.append(firstPrevSelect);
                                    if (dataNameJSONClass === 'get_data_picking_type' || dataNameJSONClass === 'get_data_out_location') {
                                        selector.append(`<option value="none" data-subtext="Delete"><span>None</span></option>`);
                                    };
                                    selector.append(`<option data-divider="true"/>`);
                                    selector.append(optionsHTML);
                                    selector.selectpicker('refresh');
                                    selector.selectpicker('refresh'); // twice
                                },
                                error: function(xhr, status, error) {
                                    console.error('Error fetching options:', error);
                                }
                            });
                        }
                    }, typingTime);
                });
            });
        
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
            }else if(selectedMenu=="event"){
                linkColor.forEach(l=> l.classList.remove('active'))
                var selectedNav = document.getElementById('nav_purchase_event')
                selectedNav.classList.add('active');
            }else if(selectedMenu=="transaction"){
                linkColor.forEach(l=> l.classList.remove('active'))
                var selectedNav = document.getElementById('nav_transaction')
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

