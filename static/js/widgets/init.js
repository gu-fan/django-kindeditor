var csrfitems = document.getElementsByName("csrfmiddlewaretoken");
var csrftoken = "";
if(csrfitems.length > 0)
{
    csrftoken = csrfitems[0].value;
}
KindEditor.ready(function(K) {
    K.create('#id_content', { 
        height:'400px',
        // uploadJson : K.undef('/upload/'),
        uploadJson : '/upload/',
        fileManagerJson : '/upload/man/',
        allowFileManager : true,
        extraFileUploadParams : {
            csrfmiddlewaretoken:csrftoken
        },
    });
});
