/* Loading all elelmentsin javascript variables */
var form=$("#loanApplyForm");

/* Remove all elements after loading them into variables */
$("#loanApplyForm").remove();

// call back function for loan application tab
// emptys app div and fills it with anusuchi 1
$("#loanApply").click(function(){
    $("#app").empty();
    $("#app").append(form);
});