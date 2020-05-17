

let register_btn = document.getElementById("register_btn");

register_btn.addEventListener("click", function() {
    function matchPassword(form) {
        password = form.password.value;
        conf_pass = form.conf_pass.value;
    
        if (password === '') {   // if empty
            alert('Please create a password.')
    
        } else if (conf_pass === '') {
            alert('Please confirm your password')
    
        } else if (password != conf_pass) {
            alert('Passwords do not match. Please confirm again')
        }
    }
})