function toggleV() {
    let div = document.getElementById('videos-games')
    if (div.style.display === 'none') {
        div.style.display = 'block';
    } else {
        div.style.display = 'none';
    }
}

function toggleE() {
    let div = document.getElementById('educational')
    if (div.style.display === 'none') {
        div.style.display = 'block';
    } else {
        div.style.display = 'none';
    }
}

function toggleB() {
    let div = document.getElementById('board-games')
    if (div.style.display === 'none') {
        div.style.display = 'block';
    } else {
        div.style.display = 'none';
    }
}

function toggleF() {
    let div = document.getElementById('figures')
    if (div.style.display === 'none') {
        div.style.display = 'block';
    } else {
        div.style.display = 'none';
    }
}


 // Took from https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top
    // Get the button
    let mybutton = document.getElementById("myBtn");

    // When the user scrolls down 20px from the top of the document, show the button
    window.onscroll = function () { scrollFunction() };

    function scrollFunction() {
        if (document.body.scrollTop > 10 || document.documentElement.scrollTop > 10) {
            mybutton.style.display = "block";
        } else {
            mybutton.style.display = "none";
        }
    }

    // When the user clicks on the button, scroll to the top of the document
    function topFunction() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    }

    function toggleI() {
        let div = document.getElementById('images')
        if (div.style.display === 'none') {
            div.style.display = 'block';
        } else {
            div.style.display = 'none';
        }
    }