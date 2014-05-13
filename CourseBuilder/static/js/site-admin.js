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

$('#admin-content-tabs').sortable();
});



//initilize tabs
$(function () {
  var currentTab;
  var slideCount =  $('.nav-tabs').children().length + 1;

    //when ever any tab is clicked this method will be call
    $("#admin-content-tabs").on("click", "a", function (e) {
        e.preventDefault();

        $(this).tab('show');
        $currentTab = $(this);
    });


  //shows the tab with passed content div id..paramter tabid indicates the div where the content resides
  function showTab(tabId) {
      $('#admin-content-tabs a[href="#' + tabId + '"]').tab('show');
  }
  //return current active tab
  function getCurrentTab() {
      return currentTab;
  }

  //This function will create a new tab here and it will load the url content in tab content div.
  function craeteNewTabAndLoadUrl(parms, url, loadDivSelector) {

  /*    $("" + loadDivSelector).load(url, function (response, status, xhr) {
          if (status == "error") {
              var msg = "Sorry but there was an error getting details ! ";
              console.log()
              $("" + loadDivSelector).html(msg + xhr.status + " " + xhr.statusText);
              $("" + loadDivSelector).html("Load Ajax Content Here...");
          }
      });*/

  }

  //this will return element from current tab
  //example : if there are two tabs having  textarea with same id or same class name then when $("#someId") whill return both the text area from both tabs
  //to take care this situation we need get the element from current tab.
  function getElement(selector) {
      var tabContentId = $currentTab.attr("href");
      return $("" + tabContentId).find("" + selector);

  }


  function removeCurrentTab() {
      var tabContentId = $currentTab.attr("href");
      $currentTab.parent().remove(); //remove li of tab
      $('#admin-content-tabs a:last').tab('show'); // Select first tab
      $(tabContentId).remove(); //remove respective tab content
  }

  //this method will register event on close icon on the tab..
  var registerCloseEvent = function () {

      $(".closeTab").click(function () {

          //there are multiple elements which has .closeTab icon so close the tab whose close icon is clicked
          var tabContentId = $(this).parent().attr("href");
          $(this).parent().parent().remove(); //remove li of tab
          $('#admin-content-tabs a:last').tab('show'); // Select first tab
          $(tabContentId).remove(); //remove respective tab content

      });
  }
  //this method will demonstrate how to add tab dynamically
  var registerslideButtonEvent = function () {
      /* just for this demo */
      $('#newtab').click(function (e) {
          e.preventDefault();

          var tabId = "tab-" + slideCount; //this is id on tab content div where the 
          slideCount = slideCount + 1; //increment slide count

          $('.nav-tabs').append('<li><a href="#' + tabId + '"><button class="close closeTab" type="button" >×</button>'+$(this).html()+'</a></li>');
          $('.tab-content').append('<div class="tab-pane" id="' + tabId + '"></div>');

          craeteNewTabAndLoadUrl("", "./", "#" + tabId);

          $("#" +  tabId).html($('#emptyform').html());

          $(this).tab('show');
          showTab(tabId);
          registerCloseEvent();
      });
      registerCloseEvent(); //for preloaded slides.

  }();


});








    var approval_callback = function(approval_data) {
        return function(data, textStatus) {

      };
    };

    $(document).on('submit', '.approval-form', function(event) {

      /* stop form from submitting normally */
      event.preventDefault();

      /* get some values from elements on the page: */
      var $form = $( this ),
          bidder_id = $form.find( 'input[name="bidder-id"]' ).val(),
          submit_btn = $form.find( 'input[type="submit"]' ),
          action = submit_btn.val(),
          status_col = $form.parent().prev(),
          url = $form.attr( 'action' )

      submit_btn.button('loading');
      submit_btn.prop('disabled', true);

      /* Send the data using post */
      var data_closure = {
          'submit_btn': submit_btn,
          'status_col': status_col,
      };
 
      /* Send the data using post */
      var posting = $.post( url, {
        'bidder_id': bidder_id, 'action': action },
         approval_callback(data_closure),
         'json'
      );
      posting.fail(function() { alert("error"); })
      .always(function() { console.log('finished'); });

    });