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
        $('.login-error').css('display', 'none');

        window.location.href = '/home';
      },
      error: (err) => {
        $('.login-error').css('display', 'block');
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
        setTimeout(() => {
          window.location.href = '/home';
        }, 2000);
      },
      error: (err) => {
        console.log(err);
      },
    });
  };

  $('.post_btn').on('click', postProduct);

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
                    <a href="#" class="more-details"  data-product-id="${product.product_id}">more details</a>
                  </div>
                </div>
              `;
              $('.product-card-grid').prepend(productTemplate);
              // Get DOM Elements
              const modal = document.querySelector('#productDetailsModal');
              const modalBtn = document.querySelectorAll('.more-details');
              const closeBtn = document.querySelector('.close');

              // Events
              modalBtn.forEach((btn) => {
                btn.addEventListener('click', openModal);
              });
              closeBtn.addEventListener('click', closeModal);
              window.addEventListener('click', outsideClick);

              // Open
              function openModal() {
                modal.style.display = 'block';
              }

              // Close
              function closeModal() {
                modal.style.display = 'none';
              }

              // Close If Outside Click
              function outsideClick(e) {
                if (e.target == modal) {
                  modal.style.display = 'none';
                }
              }

              // Update modal content
              // Make an ajax request to get product details

              $('.more-details').on('click', function () {
                // Get product id from the clicked element
                let productId = $(this).attr('data-product-id');
                $.ajax({
                  url: `/api/v1/products/${productId}`,
                  type: 'GET',
                  success: (product) => {
                    // Update modal title
                    $('.modal-title').text(product.description);

                    // Update modal image
                    $('.modal-image').attr('src', product.image);

                    // Update other modal content
                    $('.modal-price').text(`Price: Kshs. ${product.price}`);
                    $('.product-blog').text(product.description);
                    $('.product-category').text(product.category);
                    $('.modal-show-contact').text('Show contact');

                    // Show modal
                    $('#productDetailsModal').css('display', 'block');

                    if (token) {
                      $('.modal-show-contact').on('click', function () {
                        $.ajax({
                          url: `/api/v1/farmers/${product.farmer_id}`,
                          type: 'GET',
                          success: (farmer) => {
                            $('.modal-show-contact').text(farmer.phone);
                          },
                        });
                      });
                    } else {
                      $('.modal-show-contact').on('click', function () {
                        window.location.href = '/login';
                      });
                    }
                  },
                  error: (err) => {
                    console.log('Error Fetching product details:', err);
                  },
                });
              });
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

  //Search products
  const searchProducts = () => {
    const searchInput = $('#searchInput').val();
    $.ajax({
      url: `/api/v1/products/search/${searchInput}`,
      type: 'GET',
      success: (data) => {
        console.log(data);
        $('.product-card-grid').empty();
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
                    <a href="#" class="more-details" data-product-id="${product.product_id}">more details</a>
                  </div>
                </div>
              `;
              $('.product-card-grid').prepend(productTemplate);
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
  };
  $('.search-btn').on('click', searchProducts);

  // return products if there is no search input
  $('#searchInput').on('input', function () {
    if (!$(this).val()) {
      $.ajax({
        url: '/api/v1/products',
        type: 'GET',
        success: (data) => {
          $('.product-card-grid').empty();
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
                    <a href="#" class="more-details"  data-product-id="${product.product_id}">more details</a>
                  </div>
                </div>
              `;
                $('.product-card-grid').prepend(productTemplate);
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
  });
});
