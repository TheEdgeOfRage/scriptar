$('#submit-file-upload').on('click', function (event){
    event.preventDefault();
    //$('#upload-input').click();
    $('.progress-bar').text('0%');
    $('.progress-bar').width('0%');
// });

// $('#upload-input').on('change', function(){

    var files = $("#upload-input").get(0).files;
    alert(files.length)
    if (files.length > 0){
        var formData = new FormData();

        for (var i = 0; i < files.length; i++) {
            var file = files[i];

            formData.append('file' + i, file, file.name);
        }

        formData.append('script_name', $("#script_name").value());
        formData.append('description', $("#description").value());
    
        $.ajax({
            url: '/upload',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data){
                console.log('upload successful!\n' + data);
            },
            xhr: function() {
                // create an XMLHttpRequest
                var xhr = new XMLHttpRequest();

                // listen to the 'progress' event
                xhr.upload.addEventListener('progress', function(evt) {

                    if (evt.lengthComputable) {
                        // calculate the percentage of upload completed
                        var percentComplete = evt.loaded / evt.total;
                        percentComplete = parseInt(percentComplete * 100);

                        // update the Bootstrap progress bar with the new percentage
                        $('.progress-bar').text(percentComplete + '%');
                        $('.progress-bar').width(percentComplete + '%');

                        // once the upload reaches 100%, set the progress bar text to done
                        if (percentComplete === 100) {
                            $('.progress-bar').html('Done');
                        }

                    }

                }, false);

                return xhr;
            }
        });

    }
});
