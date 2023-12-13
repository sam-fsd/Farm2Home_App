// const tabs = document.querySelectorAll('.tab_btn');
// const all_forms = document.querySelectorAll('.form');

// tabs.forEach((tab, index) => {
//   tab.addEventListener('click', (e) => {
//     tabs.forEach((tab) => tab.classList.remove('active'));
//     tab.classList.add('active');
//     const line = document.querySelector('.line');
//     line.style.width = e.target.offsetWidth + 'px';
//     line.style.left = e.target.offsetLeft + 'px';

//     all_forms.forEach((form) => form.classList.remove('active'));
//     all_forms[index].classList.add('active');
//   });
// });

// const uploadBtn = document.querySelector('.upload-btn');
// const imagePreview = document.querySelector('.imagePreview');
// const imageInput = document.querySelector('#imageInput');
// const uploadImageIcon = document.querySelector('.upload-image-icon');
// const uploadImageContainer = document.querySelector('.upload-image-container');
// const removeImageBtn = document.querySelector('#remove-image-btn');
// const cancelProductModalBtn = document.querySelector('.cancel-btn');
// const postProductModal = document.querySelector('.post-product-modal');
// const overylay = document.querySelector('#overlay');
// const productMoreDetailsModal = document.querySelector('.product-more-details');
// const moreDetailsBtn = document.querySelectorAll('.more-details');
// const displayPostProductModal = document.querySelector(
//   '.display-post-product-modal'
// );
// const cancelMoreDetailsModalBtn = document.querySelector(
//   '.cancel-product-modal'
// );

// function previewImage(event) {
//   const fileInput = event.target;

//   const file = fileInput.files[0];

//   if (file) {
//     const reader = new FileReader();
//     reader.onload = (e) => {
//       imagePreview.setAttribute('src', e.target.result);
//       imagePreview.style.display = 'block';
//       uploadImageIcon.classList.add('hide');
//       uploadBtn.classList.add('hide');
//       uploadImageContainer.style.border = 'none';
//       removeImageBtn.style.display = 'block';
//     };
//     reader.readAsDataURL(file);
//   } else {
//     imagePreview.setAttribute('src', '');
//     imagePreview.style.display = 'none';
//     uploadImageIcon.classList.remove('hide');
//   }
// }

// //Trigger Post Product modal
// displayPostProductModal.addEventListener('click', () => {
//   postProductModal.style.display = 'block';
//   overylay.style.display = 'block';
// });

// cancelProductModalBtn.addEventListener('click', () => {
//   postProductModal.style.display = 'none';
//   overylay.style.display = 'none';
// });

// //Trigger Product more details modal
// moreDetailsBtn.forEach((btn) => {
//   btn.addEventListener('click', () => {
//     productMoreDetailsModal.style.display = 'block';
//     overylay.style.display = 'block';
//   });
// });

// //Close Product more details modal
// cancelMoreDetailsModalBtn.addEventListener('click', () => {
//   productMoreDetailsModal.style.display = 'none';
//   overylay.style.display = 'none';
// });

// //Submitting Buyer farm details

// const submitCustomerForm = () => {
//   const form = document.getElementById('customer-form');
//   const formData = new FormData(form);

//   //Add the default query parameter
//   formData.append('user_type', 'customer');

//   fetch('/api/v1/auth/register', {
//     method: 'POST',
//     body: formData,
//   })
//     .then((res) => res.json())
//     .then((data) => {
//       console.log(data);
//       if (data.status === 'success') {
//         window.location.href = 'pages/login.html';
//       }
//     })
//     .catch((err) => console.log(err));
// };

// //Submitting Farmer farm details
// const submitFarmerForm = () => {
//   const form = document.getElementById('farmer-form');
//   const formData = new FormData(form);

//   //Add the default query parameter
//   formData.append('user_type', 'farmer');

//   fetch('/api/v1/auth/register', {
//     method: 'POST',
//     body: formData,
//   })
//     .then((res) => res.json())
//     .then((data) => {
//       console.log(data);
//       if (data.status === 'success') {
//         window.location.href = 'pages/login.html';
//       }
//     })
//     .catch((err) => console.log(err));
// };

$(document).ready(function () {
  const tabs = $('.tab_btn');
  const allForms = $('.form');
  const uploadBtn = $('.upload-btn');
  const imagePreview = $('.imagePreview');
  const imageInput = $('#imageInput');
  const uploadImageIcon = $('.upload-image-icon');
  const uploadImageContainer = $('.upload-image-container');
  const removeImageBtn = $('#remove-image-btn');
  const cancelProductModalBtn = $('.cancel-btn');
  const postProductModal = $('.post-product-modal');
  const overlay = $('#overlay');
  const productMoreDetailsModal = $('.product-more-details');
  const moreDetailsBtn = $('.more-details');
  const displayPostProductModal = $('.display-post-product-modal');
  const cancelMoreDetailsModalBtn = $('.cancel-product-modal');

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

    //   fetch(`/api/v1/auth/register?user_type=${userType}`, {
    //     method: 'POST',
    //     headers: {
    //       'Content-Type': 'application/json',
    //     },
    //     body: jsonstring,
    //   })
    //     .then((res) => res.json())
    //     .then((data) => {
    //       if (data.status === 'success') {
    //         console.log(data.status);
    //         console.log(data);
    //         window.location.href = 'pages/login.html';
    //       }
    //     })
    //     .catch((err) => console.log(err));
    // };

    // $('#submit-customer-form').on('click', function () {
    //   submitForm('customer');
    // });

    // $('#submit-farmer-form').on('click', function () {
    //   submitForm('farmer');

    $.ajax({
      url: `/api/v1/auth/register?user_type=${userType}`,
      type: 'POST',
      contentType: 'application/json',
      data: jsonstring,
      success: (data) => {
        window.location.href = 'pages/login.html';
      },
      error: (err) => {
        console.log(err);
      },
    });
  };
});
