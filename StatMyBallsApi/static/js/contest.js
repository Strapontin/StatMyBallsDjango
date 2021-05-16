$(document).ready(function () {

    initDocument();
});


function initDocument() {

    $(".blue-score-up").off("click").on("click", _onClickBlueScoreUp);
    $(".blue-score-down").off("click").on("click", _onClickBlueScoreDown);
    $(".yellow-score-up").off("click").on("click", _onClickYellowScoreUp);
    $(".yellow-score-down").off("click").on("click", _onClickYellowScoreDown);

    $(".player-scored div").off("click").on("click", _onSetPlayerScored);
    $(".goal-types div").off("click").on("click", _onSetGoalScored);
}

/**
 * When the user adds one point to the blue team
 */
function _onClickBlueScoreUp() {

    var scoreValue = $(".blue-score .score").text();
    $(".blue-score .score").text(parseInt(scoreValue) + 1);
}

/**
 * When the user removes one point to the blue team
 */
function _onClickBlueScoreDown() {

    var scoreValue = $(".blue-score .score").text();
    $(".blue-score .score").text(parseInt(scoreValue) - 1);
}

/**
 * When the user adds one point to the yellow team
 */
function _onClickYellowScoreUp() {

    var scoreValue = $(".yellow-score .score").text();
    $(".yellow-score .score").text(parseInt(scoreValue) + 1);
}

/**
 * When the user removes one point to the yellow team
 */
function _onClickYellowScoreDown() {

    var scoreValue = $(".yellow-score .score").text();
    $(".yellow-score .score").text(parseInt(scoreValue) - 1);
}

/**
 * On click on a player that scored
 * @param {*} event 
 */
function _onSetPlayerScored(event) {

    var element = $(event.currentTarget);

    var pk = element.data("pk");
    var name = element.text();

    // Set the player in the slot 
    $(".player-scored .slot")
        .data("pk", pk)
        .text(name);
}

/**
 * On click on a goal type
 */
function _onSetGoalScored(event) {

    var element = $(event.currentTarget);
    
    var pk = element.data("pk");
    var name = element.text();

    // Set the goal type in the slot 
    $(".goal-types-container .slot")
        .data("pk", pk)
        .text(name);
}