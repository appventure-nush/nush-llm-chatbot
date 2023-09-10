$(document).ready(function() {
    $('#sendbtn').click(function(e){
        let user_msg = $('#textArea').val();

        // if message isn't empty then send the API call
        if (user_msg) {
            // clear textarea for next message
            $('#textArea').val("");
            $('#sendbtn').attr("disabled", true);

            // add user response to chatlog
            $('#chatlogs').append(`
                        <div class="d-flex flex-row justify-content-end mb-4">
                            <div class="p-3 me-3 border user-response" >
                                <p class="small mb-0">${user_msg}</p>
                            </div>
                            <i class="bi bi-person-circle avatar fs-1"></i>
                        </div>`);

            e.preventDefault();
            $.ajax({
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                type: "POST",
                cache: false,
                url: $(this).attr('action'),
                data: JSON.stringify(user_msg),
                datatype: "json",
                success: function (data) {
                    console.log("response received");
                    if (data.hasOwnProperty('response')) {
                        $('#chatlogs').append(`
                            <div class="d-flex flex-row justify-content-start mb-4" >
                                <img src=${chatbot_src} width="85" height="85"></img>
                                <div class="p-3 ms-3 chatbot-response">
                                    <p class="small mb-0">
                                    ${data['response']}
                                    </p>
                                </div>
                            </div>`);
                    }
                    $('#sendbtn').attr("disabled", false);
                }
            });
        }
    });
});