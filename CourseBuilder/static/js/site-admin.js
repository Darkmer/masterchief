  $(function() {

  function filter(element,what) {
      var value = $(element).val();
      value = value.toLowerCase().replace(/\b[a-z]/g, function(letter) {
          return letter.toUpperCase();
      });
      if(value == '')
          $(what+' > li').show();
      else{
          $(what+' > li:not(:contains(' + value + '))').hide();
          $(what+' > li:contains(' + value + ')').show();
      }
  };

	$('#q').keyup(function(){
      filter(this,'#sortable');
  });

  var $currentlySelected = null;
  var selected = [];

  $('#sortable')
    .sortable({ handle: ".handle",  placeholder: "ui-state-highlight" })
    .selectable({
      filter: "li",
      cancel: ".handle",
      start: function(event, ui) {
          $currentlySelected = $('#selectable .ui-selected');
      },
      stop: function(event, ui) {
          for (var i = 0; i < selected.length; i++) {
              if ($.inArray(selected[i], $currentlySelected) >= 0) {
                $(selected[i]).removeClass('ui-selected');
              }
          }
          selected = [];
      },
      selecting: function(event, ui) {
          $currentlySelected.addClass('ui-selected'); // re-apply ui-selected class to currently selected items
      },
      selected: function(event, ui) {
          selected.push(ui.selected); 
      },
      tolerance: 'fit'
    })
      .find( "li" )
          .addClass( "ui-corner-all" )
          .prepend( "<div class='handle'><span class='ui-icon ui-icon-carat-2-n-s'></span></div>" );

  });