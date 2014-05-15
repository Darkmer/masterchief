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
      filter(this,'#contentList');
  });

  var $currentlySelected = null;
  var selected = [];

$('#admin-content-tabs').sortable();
});



//initilize tabs
$(document).ready(function() {

  var currentTab;
  var slideCount =  $('.nav-tabs').children().length + 1;


      function block_form() {
          $(".loading").show();
          $('textarea').attr('disabled', 'disabled');
          $('input').attr('disabled', 'disabled');
      }

      function unblock_form() {
          $('.loading').hide();
          $('textarea').removeAttr('disabled');
          $('input').removeAttr('disabled');
          $('.errorlist').remove();
      }

      // prepare Options Object for plugin
      var options = {
          beforeSubmit: function(form, options) {
              // return false to cancel submit
              console.log(form);
              block_form();
          },
          success: function(data) {
              unblock_form();

              $(".form_ajax").show();
              setTimeout(function() {
                  $(".form_ajax").hide();
              }, 5000);
          },
          error:  function(resp) {
              unblock_form();
              $(".form_ajax_error").show();
              // render errors in form fields
              var errors = JSON.parse(resp.responseText);
              for (error in errors) {
                  var tabId = '#id_' + error;
                  $(""+tabId).next().html(errors[error]);
              }
              setTimeout(function() {
                  $(".form_ajax_error").hide();
              }, 5000);
          },
      };

      $('.form-horizontal').ajaxForm(options);

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

    $(".closeTab").click(function (e) {
        e.preventDefault();

        var r=confirm("Are you sure you want to delete this tab?");
        if (r==false){
            return;
        }
          //there are multiple elements which has .closeTab icon so close the tab whose close icon is clicked
          var tabContentId = $(this).parent().attr("href");
          $(this).parent().parent().remove(); //remove li of tab
          $('#admin-content-tabs a:last').tab('show'); // Select first tab
          $(tabContentId).remove(); //remove respective tab content
          
          var postUrl = $(this).data("url");

          if(postUrl){
            var jqxhr = $.post(postUrl, function(e) {
            })
            .fail(function(e) {
              alert( "Error in Performing Deletion" );
            });
          }
      });
  }
  //this method will demonstrate how to add tab dynamically
  var registerslideButtonEvent = function () {
      /* just for this demo */
      $('#newtab').click(function (e) {
          e.preventDefault();

          var tabId = "tab-" + slideCount; //this is id on tab content div where the 
          slideCount = slideCount + 1; //increment slide count

          $('.nav-tabs').append('<li><a href="#' + tabId + '" data-subject="999"><button class="close closeTab" type="button" >×</button><span>'+$(this).html()+'</span></a></li>');
          $('.tab-content').append('<div class="tab-pane" id="' + tabId + '"></div>');

          $("#" +  tabId).html($('#emptyform').html());

          $(this).tab('show');
          showTab(tabId);
          registerCloseEvent();

          $("#" +  tabId + " form").ajaxForm(options);
        
      });
      registerCloseEvent(); //for preloaded slides.

  }();

    $("div.panel-body").on("keyup", ".tab-subject", function (e) {
      e.preventDefault();
      var tabId = $(this).parents(".tab-pane").attr('id');
       $('#admin-content-tabs a[href="#' + tabId + '"] span').html(this.value);
     });


    $('#updateOrder').click(function (e) {
      
      var subjectlist = []
      $('#admin-content-tabs a').each(function( index) {
        subjectlist.push($(this).data('subject'));
      });
        var postUrl = $(this).data("url");

        if(postUrl){
          var jqxhr = $.post(postUrl, {subjectlist: subjectlist} , function(e) {
            alert( "Order Updated Successfully" );
          })
          .fail(function(e) {
            alert( "Error In Performing Reorder" );
          });
        }
    });
});
