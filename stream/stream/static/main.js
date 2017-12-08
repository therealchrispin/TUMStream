$(document).ready(function () {

    function getFormValues(){
        return {
            "title":$('#title').val(),
            "description":$('#description').val(),
            "topic":$('#topic').val(),
            "category":$('#category').val()
        };
    }



    function createStream(streamItem){
        var divContainer = $('<div class="container"></div>');
        $(divContainer).append('<h3>' + streamItem['title'] + '</h3>');
        $(divContainer).append('<p>' + streamItem['description'] + '</p>');

        return divContainer;
    }


    function loadStreamItems(){
        var url = "http://0.0.0.0:6543/stream.json";

        $.ajax({
            type:'POST',
            url: url,
            success: function (data) {
                console.log(data);
                for(var i=0;i<data['itemList'].length;i++){
                    console.log(data['itemList'][i]);
                    $('.stream').append(createStream(data['itemList'][i]));
                }
            }
        });
    }


    $('#button').click(function () {
        var url = 'http://0.0.0.0:6543/itemcreator.json';
        console.log(getFormValues());

        $.ajax({
                type: "POST",
                url: url,
                data: {'data': JSON.stringify(getFormValues())},
                dataType: 'json',
                success: function(data) {
                    $('from').remove("#success_message");
                    $('<p id="success_message" style="color:red;">' + data['message'] + '</p>').insertAfter('form');
                }
        });
    });


    loadStreamItems();


});