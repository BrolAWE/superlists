window.Superlists = {}; 1
window.Superlists.initialize = function () { 2
 $('input[name="text"]').on('keypress', function () {
     $('.has-error').hide();
 });
};