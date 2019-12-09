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

/* Loading all elelmentsin javascript variables */
var karjaData=$("#karja");
/* Remove all elements after loading them into variables */
$("#karja").remove();
// call back function for karja application tab
// emptys app div and fills it with karja data
$("#karjapra").click(function(){
    $("#loan_data").empty();
    $("#loan_data").append(karjaData);
});
// click function for loan data
$("#karjapra").click(function(){
	// clear data before loading new data
	$("#loanemployeedata").empty();
$(document).ready(function () {
	$.getJSON("http://127.0.0.1/api/loans/", function (data) {
		var loandata = '';
		// to print each data
		$.each(data,function (key, value) {
			loandata += '<tr>';
			loandata += '<td>'+ value.employee_name +'</td>';
			loandata += '<td>'+ value.employee_id +'</td>';
			loandata += '<td>'+ value.position +'</td>';
			loandata += '<td>'+ value.loanamount +'</td>';
			loandata += '<td>'+ value.status +'</td>';
			loandata += '</tr>';
			// body...
		});
		// append loandata to table id loanemployeedata
		$('#loanemployeedata').append(loandata);
		// body...
	});
	// body...
});
});
