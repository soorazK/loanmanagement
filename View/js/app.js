// anusachi form1
/* Loading all elelmentsin javascript variables */
var form=$("#loanApplyForm"); // variable containing loan apppication form (Anusuchi 1)

/* Remove all elements after loading them into variables */
$("#loanApplyForm").remove();

// call back function for loan application tab
// emptys app div and fills it with anusuchi 1
$("#loanApply").click(function(){
    $("#app").empty();
    $(".welcome").remove();
    $("#app").append(form);
});



// Karja Bebasthapan
/* Loading all elelmentsin javascript variables */
var karjabebas=$("#karja-bebasthapan"); // variable containing loan apppication form (Anusuchi 1)

/* Remove all elements after loading them into variables */
$("#karja-bebasthapan").remove();

// call back function for loan application tab
// emptys app div and fills it with anusuchi 1
$("#karjabebasthapan").click(function(){
    $("#app").empty();
    $(".welcome").remove();
    $("#app").append(karjabebas);
});



// karja vuktani
/* Loading all elelmentsin javascript variables */
var karjavukta=$("#karja-vuktani"); // variable containing loan apppication form (Anusuchi 1)

/* Remove all elements after loading them into variables */
$("#karja-vuktani").remove();

// call back function for loan application tab
// emptys app div and fills it with anusuchi 1
$("#karjavuktani").click(function(){
    $(".welcome").remove();
    $("#app").empty();
    $("#app").append(karjavukta);
});



// karja parmanikaran
/* Loading all elelmentsin javascript variables */
var karjaData=$("#karja-parmanikaran");
/* Remove all elements after loading them into variables */
$("#karja-parmanikaran").remove();
// call back function for karja application tab
// emptys app div and fills it with karja data
$("#karjapra").click(function(){
    $(".welcome").remove();
    $("#app").empty();
    $("#app").append(karjaData);
});



	
$( function () {
var $userName = $('#uname');
var $userPass = $('#pass');
var $name = $('#employee_name');
var $eid = $('#employee_id');
var $lname = $('#loanname');
var $rdate = $('#recruitdate');
var $position1 = $('#position');
var $lamount = $('#loanamount');
var $paddress = $('#permanent_address');
var $taddress = $('#temporary_address');
var $birththdate = $('#DOB');

$('#karjapra').click(function () {
	// clear data before loading new data
	$("#loanemployeedata").empty();	

	$.ajax({
		type:'GET',
		url: 'http://127.0.0.1/api/loans/',
		success:function (data) {
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
		}

		

	});
	// body...
} );

$('#submit2').click(function () {
	var inputloantype = {
		employee_name: $name.val(),
		employee_id: $eid.val(),
		loanname: $lname.val(),
		recruitdate: $rdate.val(),
		position: $position1.val(),
		loanamount: $lamount.val(),
		permanent_address: $paddress.val(),
		temporary_address: $taddress.val(),
		DOB: $birththdate.val(),
	};
	$.ajax({
		type:'post',
		url:'http://127.0.0.1/api/loans/create/',
		data: inputloantype,
		dataType: "json",
    	error: function () {
			alert('error saving data');
			// body...
		}

	});
	// body...
});

$('#loginbtn').click(function () {
		var login = {
			username: $userName.val(),
			password: $userPass.val(),
			
	};
	$.ajax({
		type: 'post',
		url: 'http://127.0.0.1/api/login/',
		data: login,
		error: function () {
			alert('error');
			// body...
		}
	}); 

		// body...
	});
	// body...
});


