$(document).ready(function () {

    initDocument();
});


function initDocument() {

    $("#new-contest").off("click").on("click", onClickNewContest);
    $("#all-contests").off("click").on("click", onClickAllContests);
    $("#stats").off("click").on("click", onClickStats);
}

/**
 * Opens the page to create a new game
 */
function onClickNewContest() {

    location.href = "/create";
}

/**
 * Opens the page to see all the games
 */
 function onClickAllContests() {

    location.href = "/all-contests";
}

/**
 * Opens the page to see the stats
 */
 function onClickStats() {

    // location.href = "/stats";
}
