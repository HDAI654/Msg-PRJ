$(document).ready(function() {

    


    // get all message from backend from database and make page
    function reload () {

        // Reload the current page
        $.ajax({
            type: "POST",
            url: "http://"+window.location.host+"/readmsg",
            data: $("#frm-getdata").serialize(),
            beforeSend: function() {
              //console.log("before")
            },
            success: function(result) {
                //console.log("success")
                data = JSON.parse(result);
                if(result.length>0){
                    //console.log(data);
                    strvar=""
                    for(item in data){
                      strvar = strvar+
                      "<div class='row mt-1'>"+
                          "<div class='col-md-12'>"+
                              "<div class='toast show' data-autohide='false'>"+
                                  "<div class='toast-header'>"+
                                    "<strong class='mr-auto text-primary'>"+data[item]['fields']['user_name']+"</strong>"+
                                    "<small class='text-muted'>"+data[item]['fields']['date_and_time']+"</small>"+
                                  "</div>"+
                                  "<div class='toast-body'>"+data[item]['fields']['text']+"</div>"+
                              "</div>"+
                          "</div>"+
                      "</div>"
                      //console.log(strvar)
                      $("#message").html(strvar);
                    }
                } 
            },
            error: function(e) {
              console.log("error");
            },
          });

    };
    reload()
    setInterval(reload, 100);



    // refresh the page when the refresh button is clicked
    $("#refresh_btn").click(function() {
      reload()
    });


    // send message to view for save with ajax
    $("#send_btn").click(function() {

      // send message to view for save with ajax
      $.ajax({
        type: "POST",
        url: "http://"+window.location.host+"/savemessage",
        data: $("#message_form").serialize(),
        beforeSend: function() {
            //console.log("sending...")
        },
        success: function(result) {
          if (result=="true") {
            //console.log("Saved successfully!")
          }else{
            console.log("Saveing failed!")
          }
        },
        error: function(e) {
          console.log("Saveing failed!")
        },
      });

      // clear textbox
      $("#id_text").val("")

      // reload page after successful save
      reload()
    });

});