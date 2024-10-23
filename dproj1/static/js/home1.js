var popup = document.getElementById("popupBox");
var overlay = document.getElementById("popupOverlay");
var passwordLink = document.getElementById("passwordLink");
var span = document.getElementsByClassName("close")[0];
passwordLink.onclick = function(event) {
 
document.getElementById('email').value = localStorage.getItem('email');
    
    popup.style.display = "block";
    overlay.style.display = "block";
}

span.onclick = function() {
    popup.style.display = "none";
    overlay.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == overlay) {
        popup.style.display = "none";
        overlay.style.display = "none";
    }
}

document.getElementById('confirm-password-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const storedPassword = localStorage.getItem('password');
    const confirmPassword = document.getElementById('confirm-password').value;
    const confirmPasswordError = document.getElementById('confirm-password-error');

    if (confirmPassword !== storedPassword) {
        confirmPasswordError.style.display = 'block';
    } else {
        confirmPasswordError.style.display = 'none';
      
        document.getElementById('confirm-password-form').style.display = 'none';
        document.getElementById('new-password-form').style.display = 'block';// Update heading
    }
});

document.getElementById('new-password-form').addEventListener('submit', function (event) {
    event.preventDefault();
    const newPassword = document.getElementById('new-password').value;
    const confirmNewPassword = document.getElementById('confirm-new-password').value;
    const newPasswordError = document.getElementById('new-password-error');

    if (newPassword !== confirmNewPassword) {
        newPasswordError.style.display = 'block';
    } else {
        newPasswordError.style.display = 'none';
      
        localStorage.setItem('password', newPassword);
        alert('Password changed successfully!');
        popup.style.display = "none";
        overlay.style.display = "none";
    }
});


document.querySelectorAll('.toggle-password').forEach(toggle => {
    toggle.addEventListener('click', function () {
        const passwordField = this.previousElementSibling;
        const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordField.setAttribute('type', type);
        this.classList.toggle('bi-eye-slash');
        this.classList.toggle('bi-eye');
    });
});


document.getElementById('email').value = localStorage.getItem('email');