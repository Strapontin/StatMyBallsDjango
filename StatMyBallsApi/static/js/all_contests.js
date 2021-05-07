$(document).ready(function () {

    initDocument();
});


function initDocument() {

    $(".contest-container").off("click").on("click", onClickContest);
}

/**
 * When the user clicks on a contest, we join its view
 * @param {*} event 
 */
function onClickContest(event) {

    var pk = $(event.currentTarget).data("pk");

    location.href = `/contest/${pk}`;
}