var notify_badge_class;
var notify_menu_class;
var notify_api_url;
var notify_fetch_count;
var notify_unread_url;
var notify_mark_all_unread_url;
var notify_mark_all_seen_url;
var notify_refresh_period = 15000;
var consecutive_misfires = 0;
var registered_functions = [];


// To hide notification dropdown on clicking anywhere on document but 
// not on inside dropdown items
$(document).click( function(evt){
        if($(evt.target).closest('#id_notify_dropdown').length == 0){
          $("#id_notify_dropdown").hide();
          return;          
        }

});

function fill_notification_badge(data,is_unread) {
    if(data.unseen_count == 0){
        $(".live_notify_badge").remove()
        $(".icon-Notification_Bell").attr('style','font-size: 30px;font-weight: 100;color: #fff"')
    }
    else{
        $("#dropdownMenuButtonNotify").html('<i class="icon-Notification_Bell" aria-hidden="true" style="position: absolute;font-size: 30px;font-weight: 100;color: #fff"></i><span class="live_notify_badge badge badge-primary" style="border-radius: 10px;margin-bottom: 10px;overflow: auto;font-size: 10px;position: relative;margin-left: 15px;padding: 1px 5px">'+data.unseen_count+'</span>')
    }
    var badges = document.getElementsByClassName(notify_badge_class);
    if (badges) {
        for(var i = 0; i < badges.length; i++){
            badges[i].innerHTML = data.unseen_count;
        }
    }
}

function fill_notification_list(data,is_unread) {
    var menus = document.getElementsByClassName(notify_menu_class);
    var timestamp;
    unread_checked = ''
    if (is_unread){
        unread_checked = 'checked="true"'
        document.getElementById("unread").checked = true;
    }
    document.getElementById("notification_count").innerHTML = "Notifications ("+data.unread_count+")";
    if(data.all_count <= notify_fetch_count ){
        $(".notification_footer").remove()
    }
    if (menus) {
        var messages = data.all_list.map(function (item) {
            var message = "";
            var color = "#fff";
            if(typeof item.verb !== 'undefined'){
                message = message + " " + item.verb;
            }
            if(typeof item.timestamp !== 'undefined'){
                timestamp = item.timestamp;
            }
            if(item.unread == true){
                color = "#eee"
            }
            notification_message =  '<p style="margin-bottom:0.1rem">' + message+"</p><p style='font-size:10px;color:#999;margin:0'>"+ timestamp+ '</p>';
            return '<div class="dropdown-item" style="border:1px solid #ddd;position:relative;padding:0.5rem;font-size:12px;color:#000;background-color:'+color+'"><div class="row"><div class="col-md-11"><a style="text-decoration:none;color:#000;" href="/inbox/notifications/mark-as-read/'+item.slug+'?next='+item.redirect_url+'">'+notification_message+"</a></div><div class='col-md-1'><button style='margin-top:-0.5rem;margin-right:0.5rem' type='button' class='close' onclick='delete_notification("+item.slug+")' aria-label='Close'><span aria-hidden='true'>&times;</span></button></div></div></div>"
        }).join('')

        for (var i = 0; i < menus.length; i++){
            menus[i].innerHTML = messages;
        }
    }
}

function register_notifier(func) {
    registered_functions.push(func);
}

function is_unread_only(){
    if(document.getElementById("unread") != null){
    is_checked = document.getElementById("unread").checked;
    return is_checked;
    }
    return false;
}
function fetch_api_data(is_show_dropdown) {
    registered_functions = [fill_notification_list,fill_notification_badge]
    api_url = notify_api_url;
    if (registered_functions.length > 0) {
        //only fetch data if a function is setup
        var r = new XMLHttpRequest();
        r.addEventListener('readystatechange', function(event){
            if (this.readyState === 4){
                if (this.status === 200){
                    consecutive_misfires = 0;
                    var data = JSON.parse(r.responseText);
                    registered_functions.forEach(function (func) { func(data,is_unread_only()); });
                }else{
                    consecutive_misfires++;
                }
            }
        })
        if(is_unread_only()){
            api_url = notify_unread_url;
        }
        r.open("GET", api_url+'?max='+notify_fetch_count, true);
        r.send();
    }
    if (consecutive_misfires < 10) {
        setTimeout(fetch_api_data,notify_refresh_period);
    } else {
        var badges = document.getElementsByClassName(notify_badge_class);
        if (badges) {
            for (var i = 0; i < badges.length; i++){
                badges[i].innerHTML = "!";
                badges[i].title = "Connection lost!"
            }
        }
    }
    if(is_show_dropdown){
        $("#id_notify_dropdown").show();}
}

function delete_notification(slug){
    delte_url = '/inbox/notifications/delete/'+slug
    $.ajax({
        url: delte_url,
        type: 'GET',
        success: function (data) {
            fetch_api_data(true);
        },
        cache: false,
        contentType: false,
        processData: false
    });
}

function mark_all_read(){
    $.ajax({
        url: notify_mark_all_unread_url,
        type: 'GET',
        success: function (data) {

            fetch_api_data(true);
            $("#id_notify_dropdown").show();

        },
        cache: false,
        contentType: false,
        processData: false
    });
}

function mark_all_as_seen(obj){
    $.ajax({
        url: notify_mark_all_seen_url,
        type: 'GET',
        async: false,
        success: function (data) {
            fetch_api_data(true);
            dropdown = obj.parentElement.className
            if(dropdown == "dropdown show"){
                $("#id_notify_dropdown").hide();
                $("#dropdownMenuButtonNotify").attr("style","background-color:#000;border:#000;color:#fff")
            
            }
            else{
                $("#id_notify_dropdown").show();
                $("#dropdownMenuButtonNotify").attr("style","background-color:#000;border:#000;color:#fff")
            }
        },
        cache: false,
        contentType: false,
        processData: false
    });   
}

function get_unread_notifications(){
            fetch_api_data(true);
};

function show_more(){
    dropdown_option_count = $(".live_notify_list").children().length;
    notify_fetch_count = parseInt(notify_fetch_count) + 20
    fetch_api_data(true);
}   

// setTimeout(fetch_api_data, 3000,false);
