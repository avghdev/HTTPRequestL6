function factorial() {
    xhr = new XMLHttpRequest();
    xhr.open("GET", "/factorial/" + $("#factorial").val());

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            $("#result").html(xhr.response);
        }
    }

    xhr.send();
}