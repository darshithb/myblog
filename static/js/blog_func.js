$('.embolden').click(function(){
    var highlight = window.getSelection();  
    var span = '<span class="bold">' + highlight + '</span>';
    var text = $('.embolden').html();
    $('.embolden').html(text.replace(highlight, span));
});

document.execCommand('bold');