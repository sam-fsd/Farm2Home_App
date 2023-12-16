$(document).ready(function () {
  const tabs = $('.tab_btn');
  const allForms = $('.form');
  const uploadBtn = $('.upload-btn');
  const imagePreview = $('.imagePreview');
  const imageInput = $('#imageInput');
  const uploadImageIcon = $('.upload-image-icon');
  const uploadImageContainer = $('.upload-image-container');
  const removeImageBtn = $('#remove-image-btn');
  const loginBtn = $('#loginBtn');
  const moreDetailsBtn = $('.more-details');

  $('.toggle').on('click', function () {
    if ($('.item').hasClass('active')) {
      $('.item').removeClass('active');
    } else {
      $('.item').addClass('active');
    }
  });

  tabs.on('click', function (e) {
    tabs.removeClass('active');
    $(this).addClass('active');
    const line = $('.line');
    line.css('width', e.target.offsetWidth + 'px');
    line.css('left', e.target.offsetLeft + 'px');

    allForms.removeClass('active');
    allForms.eq(tabs.index(this)).addClass('active');
  });

  uploadBtn.on('change', function (event) {
    previewImage(event);
  });

  removeImageBtn.on('click', function () {
    imageInput.val('');
    previewImage({ target: imageInput[0] });
    $(this).css('display', 'none');
    uploadBtn.removeClass('hide');
    uploadImageContainer.css('border', '2px dashed #fff');
  });

  const attributes = {
    'data-bs-toggle': 'modal',
    'data-bs-target': '#productDetailsModal',
  };

  // Copy attributes to each 'moreDetailsBtn' element
  moreDetailsBtn.each(function () {
    for (const [key, value] of Object.entries(attributes)) {
      $(this).attr(key, value);
    }
  });

  window.previewImage = function (event) {
    const fileInput = event.target;
    const file = fileInput.files[0];

    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        imagePreview.attr('src', e.target.result);
        imagePreview.css('display', 'block');
        uploadImageIcon.addClass('hide');
        uploadBtn.addClass('hide');
        uploadImageContainer.css('border', 'none');
        removeImageBtn.css('display', 'block');
      };
      reader.readAsDataURL(file);
    } else {
      imagePreview.attr('src', '');
      imagePreview.css('display', 'none');
      uploadImageIcon.removeClass('hide');
    }
  };

  window.submitRegisterForm = function (userType) {
    const formId = userType === 'customer' ? '#customer-form' : '#farmer-form';
    const form = $(formId)[0];

    //Validate form has not empty fields
    const inputs = form.querySelectorAll('input');
    let isFormValid = true;
    inputs.forEach((input) => {
      if (!input.value) {
        $(input).addClass('error');
        isFormValid = false;
      } else {
        $(input).removeClass('error');
      }
    });

    if (!isFormValid) {
      return;
    }

    //validate password and confirm password
    let password = '';
    let confirmPassword = '';

    if (formId === '#customer-form') {
      password = form.querySelector('#buyerPassword').value;
      confirmPassword = form.querySelector('#buyerConfirmPassword').value;
      if (password !== confirmPassword) {
        $('#customer-form .password-error').css('display', 'block');
        return;
      } else {
        $('#customer-form .password-error').css('display', 'none');
      }
    } else {
      password = form.querySelector('#password').value;
      confirmPassword = form.querySelector('#confirmPassword').value;
      if (password !== confirmPassword) {
        $('#farmer-form .password-error').css('display', 'block');
        return;
      } else {
        $('#farmer-form .password-error').css('display', 'none');
      }
    }

    const formData = new FormData(form);

    //Create a plain JS object from the formData object
    const jsonData = {};
    for (const [key, value] of formData.entries()) {
      jsonData[key] = value;
    }

    const jsonstring = JSON.stringify(jsonData);

    $.ajax({
      url: `/api/v1/auth/register?user_type=${userType}`,
      type: 'POST',
      contentType: 'application/json',
      data: jsonstring,
      success: (data) => {
        window.location.href = '/login';
      },
      error: (err) => {
        console.log(err);
      },
    });
  };

  let isFormValid = true;

  // Function to validate the form
  function validateForm() {
    const form = $('#loginForm')[0];
    const inputs = form.querySelectorAll('input');
    inputs.forEach((input) => {
      input.addEventListener('input', () => {
        if (input.value.trim() !== '') {
          $(input).removeClass('error');
        }
      });

      // Initial check for empty fields
      if (!input.value.trim()) {
        $(input).addClass('error');
        isFormValid = false;
      }
    });
    inputs.forEach((input) => {
      if (!input.value.trim()) {
        $(input).addClass('error');
        isFormValid = false;
      } else {
        $(input).removeClass('error');
      }
    });
  }

  //Login user
  const loginUser = () => {
    //Validate form has not empty fields
    validateForm();
    if (!isFormValid) {
      return;
    }
    const form = $('#loginForm')[0];

    const formData = new FormData(form);

    $.ajax({
      url: '/api/v1/auth/token',
      type: 'POST',
      contentType: false,
      data: formData,
      processData: false,
      success: (data) => {
        window.location.href = '/home';
      },
      error: (err) => {
        console.log(err);
      },
    });
  };

  loginBtn.on('click', loginUser);
});
