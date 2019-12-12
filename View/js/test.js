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

