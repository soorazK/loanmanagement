var form=$("#loanApplyForm");
$("#loanApplyForm").remove();

$("#loanApply").click(function(){
    $("#app").empty();
    $("#app").append(form);
});
