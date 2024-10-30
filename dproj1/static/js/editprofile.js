$(document).ready(function () {
    const cityInput = $('#city');
    const stateInput = $('#state');
    const cityDropdown = $('#cityDropdown');
    const stateDropdown = $('#stateDropdown');

    const cities = ["Chengalpattu", "Coimbatore", "Dharmapuri", "Erode", 
                    "Karur", "Nagapattinam", "Nilgiris", "Theni", 
                    "Salem", "Virudhunagar", "Tiruvannamalai", "Thootukudi"];
    const states = ["Tamil Nadu", "Kerala", "Karnataka", 
                    "Andhra Pradesh", "Telangana", "Maharashtra"];

    function filterOptions(input, options, dropdown) {
        dropdown.empty().hide();
        const filter = input.val().toLowerCase();
        const filteredOptions = options.filter(option => option.toLowerCase().startsWith(filter));

        if (filteredOptions.length > 0) {
            dropdown.show();
            filteredOptions.forEach(option => {
                $('<div>').text(option).on('click', function () {
                    input.val(option);
                    dropdown.hide();
                }).appendTo(dropdown);
            });
        }
    }

    cityInput.on('input', function () {
        filterOptions(cityInput, cities, cityDropdown);
    });

    stateInput.on('input', function () {
        filterOptions(stateInput, states, stateDropdown);
    });

    $(document).on('click', function (e) {
        if (!cityDropdown.is(e.target) && cityDropdown.has(e.target).length === 0) {
            cityDropdown.hide();
        }
        if (!stateDropdown.is(e.target) && stateDropdown.has(e.target).length === 0) {
            stateDropdown.hide();
        }
    });

    $('#profile_image').on('change', function (e) {
        const file = e.target.files[0];
        if (file && file.type.startsWith('image/')) {
            const reader = new FileReader();
            reader.onload = function (event) {
                $('#profileImage').attr('src', event.target.result);
            };
            reader.readAsDataURL(file);
        } else {
            alert('Please upload a valid image file.');
        }
        $(document).ready(function () {
const editProfileUrl = "{% url 'editprofile' %}"; 
const profileUrl = "{% url 'profile' %}"; 

$('#editProfileForm').on('submit', function(e) {
    e.preventDefault(); 

    const formData = new FormData(this); 

    $.ajax({
        url: editProfileUrl, 
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false, 

        success: function() {
          
            window.location.href = profileUrl;
        },
        error: function(xhr) {
            console.error("Error:", xhr);
            alert('There was an error saving your changes.');
        }
    });
});
});
});
})
