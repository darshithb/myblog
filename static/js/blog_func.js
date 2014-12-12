// $(document).ready(function(){

// 	$(document).on('click', '#buttonB', function(){
// 		// alert("button clicked");
// 		alert(window.getSelection);
//     	// var highlight = window.getSelection(); 
//     	if (window.getSelection){
//     		try {
//     			var ta = $('#body-blog').get(0);
//             	var newText = ta.value.substring(ta.selectionStart, ta.selectionEnd);
//             	alert(newText);
//             	var selectedText = newText.toString();
//     			var span = '<span class="bold">' + newText + '</span>';
//     			alert(span);
//     			var text = $('.bold').html();
//     			$('#body-blog').html(text.replace(newText, span));
//     		}
//     		catch (e){
//     			alert("cant get selected text");
//     		}
//     	} 
//     });

// });

// $(document).ready(function(){
// 	$(document).on('click', '#buttonB', function(){
// 		ShowSelection();
// 	});
// });


// $(document).ready(function(){
//   $(document).on('pageload', '#time-{{ post.0.id }}', function(){
//     show_time();
//   });
// });


// function show_time(time,val_id){
//         var now = moment();
//         var time_diff = moment(time, "YYYYMMDD").fromNow();
//         // alert(time_diff);
//         console.log(time_diff,time,val_id);
//         $(val_id).html(time_diff);
// }



// function ShowSelection()
// {
//   var textComponent = document.getElementById('body-blog');
//   var selectedText;
//   alert(textComponent);
//   // IE version
//   if (document.selection != undefined)
//   {
//     textComponent.focus();
//     var sel = document.selection.createRange();
//     selectedText = sel.text;
//   }
//   // Mozilla version
//   else if (textComponent.selectionStart != undefined)
//   {
//     var startPos = textComponent.selectionStart;
//     var endPos = textComponent.selectionEnd;
//     selectedText = textComponent.value.substring(startPos, endPos);
//   }
//   alert("You selected: " + selectedText);
// }


// document.execCommand('bold');