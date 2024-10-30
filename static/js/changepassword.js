const toggleOldPassword = document.querySelector('#toggleOldPassword');
const oldPasswordInput = document.querySelector('#old-password');
toggleOldPassword.addEventListener('click', function () {
    const type = oldPasswordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    oldPasswordInput.setAttribute('type', type);
    this.querySelector('i').classList.toggle('fa-eye-slash');
});


const toggleNewPassword = document.querySelector('#toggleNewPassword');
const newPasswordInput = document.querySelector('#new-password');
toggleNewPassword.addEventListener('click', function () {
    const type = newPasswordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    newPasswordInput.setAttribute('type', type);
    this.querySelector('i').classList.toggle('fa-eye-slash');
});


const toggleConfirmPassword = document.querySelector('#toggleConfirmPassword');
const confirmPasswordInput = document.querySelector('#confirm-new-password');
toggleConfirmPassword.addEventListener('click', function () {
    const type = confirmPasswordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    confirmPasswordInput.setAttribute('type', type);
    this.querySelector('i').classList.toggle('fa-eye-slash');
});

