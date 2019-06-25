$(document).ready(function() {
    console.log("Reach here");

    $.ajax({
        url: "https://dog.ceo/api/breeds/image/random",
        type: "GET",
        // This is the important part
        xhrFields: {
            withCredentials: false
        },
        // data: "",
        dataType: 'json',
        success: function (response) {
            console.log(response.message)
            console.log($(".intro-header")[0].style.background = "url(" + response. message + ")")
            // $(":header").attr('src',response.message);

            // $(":header").css("style", "background-image: url(" + response. message + ")");

        },
        error: function (xhr, status) {
            console.log(xhr)
            console.log(status)
        }
    });    
});