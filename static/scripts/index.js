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

  // Change Menu once user logs in
  const token = localStorage.getItem('token');
  if (token) {
    $('.button').css('display', 'none');
    $('.logged-in').css('display', 'block');
  } else {
    $('.logged-in').css('display', 'none');
  }

  //Toggle menu dropdown
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
        localStorage.setItem('token', data.access_token);
        window.location.href = '/home';
      },
      error: (err) => {
        console.log(err);
      },
    });
  };

  loginBtn.on('click', loginUser);

  $('.logout').on('click', function () {
    localStorage.removeItem('token');
    window.location.href = '/login';
  });

  // Display modal if user is logged in
  $('.display-post-product-modal').on('click', function () {
    const token = localStorage.getItem('token');
    if (!token) {
      window.location.href = '/login';
    }
  });

  // Post product
  const postProduct = () => {
    const form = $('#postProductForm')[0];
    const formData = new FormData(form);

    $.ajax({
      url: '/api/v1/products',
      type: 'POST',
      contentType: false,
      processData: false,
      data: formData,
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
      success: (data) => {
        $('#liveToast').addClass('fade show');
        window.location.href = '/home';
      },
      error: (err) => {
        console.log(err);
      },
    });
  };

  $('.post_btn').on('click', postProduct);

  // const addProductToList = (product) => {
  //   const productTemplate = `
  //   <div class="col-md-4 col-sm-6">
  //     <div class="card mb-4">
  //       <img src="${product.image}" class="card-img-top" alt="...">
  //       <div class="card-body">
  //         <h5 class="card-title">${product.name}</h5>
  //         <p class="card-text">${product.description}</p>
  //         <p class="card-text">Price: ${product.price}</p>
  //         <p class="card-text">Quantity: ${product.quantity}</p>
  //         <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#productDetailsModal" data-product='${JSON.stringify(
  //           product
  //         )}'>More Details</button>
  //       </div>
  //     </div>
  //   </div>
  //   `;

  //   $('.products-list').append(productTemplate);
  // };

  // Add product to list
  if (window.location.pathname === '/home') {
    $.ajax({
      url: '/api/v1/products',
      type: 'GET',
      success: (data) => {
        data.forEach((product) => {
          // Get product location
          $.ajax({
            url: `/api/v1/products/${product.product_id}/location`,
            type: 'GET',
            success: (data) => {
              const location = data;
              const productTemplate = `
                <div class="product-card card-one" data-product-id=${product.product_id}>
                  <div class="product-card-img">
                    <img src="${product.image}" alt="" />
                  </div>
                  <div class="product-card-text">
                    <p class="category">${product.category}</p>
                    <h4>${product.description}</h4>
                    <p class="price">Price: Kshs. ${product.price}</p>
                    <div class="farmer-location">
                      <img src="static/assets/icons/icons8-location-50 (1).png" alt="" />
                      <p class="location">${location}</p>
                    </div>
                    <a href="static/pages/signup.html"><button class="add-to-list">Add to list</button></a>
                    <a href="#" class="more-details"data-bs-toggle="modal" data-bs-target="#productDetailsModal">more details</a>
                  </div>
                </div>
              `;
              $('.product-card-grid').append(productTemplate);
            },
            error: (err) => {
              console.log(err);
            },
          });
        });
      },
      error: (err) => {
        console.log(err);
      },
    });
  }
  const moreDetailsBtn = $('.more-details');

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

  //search products
  const searchProducts = () => {
    const searchInput = $('#searchInput').val();
    $.ajax({
      url: `/api/v1/products/search/${searchInput}`,
      type: 'GET',
      success: (data) => {
        console.log(data);
        //$('.product-card-grid').empty();
        // data.forEach((product) => {
        //   const productTemplate = `
        //   <div class="product-card card-one" data-product-id=${product.product_id}>
        //   <div class="product-card-img">
        //     <img
        //       src="${product.image}"
        //       alt=""
        //     />
        //   </div>
        //   <div class="product-card-text">
        //     <p class="category">${product.category}</p>
        //     <h4>${product.description}</h4>
        //     <p class="price">${product.price}</p>
        //     <div class="farmer-location">
        //       <img
        //         src="static/assets/icons/icons8-location-50 (1).png"
        //         alt=""
        //       />
        //       <p class="location">${product.location}</p>
        //     </div>
        //     <a href="static/pages/signup.html"
        //       ><button class="add-to-list">Add to list</button></a
        //     >
        //     <a href="#" class="more-details">more details</a>
        //   </div>
        // </div>
        // `;
        // $('.product-card-grid').append(productTemplate);
      },
      error: (err) => {
        console.log(err);
      },
    });
  };
  $('.search-btn').on('click', searchProducts);

  // Save product to a list
  const productList = [];
  if (token) {
    $('.save-product').on('click', function () {
      const product = JSON.parse($(this).attr('data-product'));
      productList.push(product);
      localStorage.setItem('productList', JSON.stringify(productList));
    });
  }
});
