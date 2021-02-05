
       function fileValidation() {
           var fileInput =
               document.getElementById('myFile');

           var filePath = fileInput.value;

           // Allowing file type
           var allowedExtensions =
/(\.doc|\.docx|\.odt|\.pdf|\.tex|\.txt|\.rtf|\.wps|\.wks|\.wpd)$/i;

           if (!allowedExtensions.exec(filePath)) {
               alert('Invalid file type');
               fileInput.value = '';
               return false;
           }
       }
