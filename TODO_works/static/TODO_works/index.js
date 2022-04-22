document.addEventListener('DOMContentLoaded', function() {

    if (document.querySelector('#add_task_form')) {
        document.querySelector('#add_task_form').onsubmit = () => { addtask() };
    };
});

function addtask() {

    let text = document.querySelector('#description').value;

    fetch('/add_task', {
        method:'POST',
        body:JSON.stringify({
        description: text
        }),
    })
    .then(response => response.json())
    .then(result => {
    if (result.message == "OK") {
        document.location.href="/";
    } else {
        alert(result.error);
    }
    });
}
