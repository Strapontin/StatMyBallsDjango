
$(document).ready(function () {

    initDocument();
});

/**
 * Init launched once the page is ready
 */
function initDocument() {

    $(".playerName").off("click").on("click", onClickPlayerName);
    $(".playerSlot").off("click").on("click", onClickplayerSlot);
    $("#startContest").off("click").on("click", startContest);
}

/**
 * When the user clicks on a player to add on a team
 */
function onClickPlayerName(event) {

    var element = $(event.currentTarget);

    // Check if a player is already selected
    var availabeSlot = element.parents(".team").find(".empty");

    console.log(availabeSlot);

    if (availabeSlot.length > 0) {

        var pk = element.data('pk');

        $(availabeSlot.get(0)).data('pk', pk).text(element.text()).removeClass("empty");
        $(`[data-pk='${pk}'`).addClass("hidden");
    }

    refreshStartButton();
}

/**
 * Sets the disabled attribute of the start button depending on if the contest can start
 */
function refreshStartButton() {

    var playerSlots = $(".playerSlot ");

    for (var i = 0; i < playerSlots.length; i++) {

        if ($(playerSlots[i]).data("pk") === -1) {

            $("#startContest").attr("disabled", "disabled");
            return;
        }
    }

    $("#startContest").attr("disabled", null);
}

/**
 * When the user clicks on a player slot, we remove the player selected, and make him available again
 */
function onClickplayerSlot(event) {

    var slot = $(event.currentTarget);

    // Show again the player hidded in both lists
    $(`[data-pk="${slot.data("pk")}"]`).removeClass("hidden");

    slot.data("pk", -1).text("").addClass("empty");

    refreshStartButton();
}

/**
 * When the user clicks on the button to start the contest
 */
function startContest() {

    // Deactivate the button once it is clicked so the same team cannot be created multiple times
    $("#startContest").attr("disabled", null);

    var data = {};
    var playerTeams = [];
    var color;

    // Save the pk of the players and their respective team color
    $(".playerSlot").each(function () {

        color = $(this).parents(".team").hasClass("blue") ? "blue" : "yellow";

        playerTeams.push(JSON.stringify({
            player: $(this).data("pk"),
            color: color
        }));
    });

    data = {
        player_teams: playerTeams,
    };

    console.log(data)

    $.ajax({
        type: 'GET',
        data: data,
        url: start_contest
    }).done(function (data) {
        console.log("Retour ajaxCall");
        console.log(data);

        // window.location.href = data.url;
    }).fail(function (data) {
        console.log('Erreur ajaxCall');
        console.log(data);
    });
}
