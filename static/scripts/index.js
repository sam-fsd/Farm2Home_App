const tabs = document.querySelectorAll('.tab_btn');
const all_forms = document.querySelectorAll('.form');

tabs.forEach((tab, index) => {
  tab.addEventListener('click', (e) => {
    tabs.forEach((tab) => tab.classList.remove('active'));
    tab.classList.add('active');
    const line = document.querySelector('.line');
    line.style.width = e.target.offsetWidth + 'px';
    line.style.left = e.target.offsetLeft + 'px';

    all_forms.forEach((form) => form.classList.remove('active'));
    all_forms[index].classList.add('active');
  });
});

const uploadBtn = document.querySelector('.upload-btn');
const imagePreview = document.querySelector('.imagePreview');
const imageInput = document.querySelector('#imageInput');
const uploadImageIcon = document.querySelector('.upload-image-icon');
const uploadImageContainer = document.querySelector('.upload-image-container');
const removeImageBtn = document.querySelector('#remove-image-btn');
const cancelProductModalBtn = document.querySelector('.cancel-btn');
const postProductModal = document.querySelector('.post-product-modal');
const overylay = document.querySelector('#overlay');
const productMoreDetailsModal = document.querySelector('.product-more-details');
const moreDetailsBtn = document.querySelectorAll('.more-details');
const displayPostProductModal = document.querySelector(
  '.display-post-product-modal'
);
const cancelMoreDetailsModalBtn = document.querySelector(
  '.cancel-product-modal'
);

function previewImage(event) {
  const fileInput = event.target;

  const file = fileInput.files[0];

  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      imagePreview.setAttribute('src', e.target.result);
      imagePreview.style.display = 'block';
      uploadImageIcon.classList.add('hide');
      uploadBtn.classList.add('hide');
      uploadImageContainer.style.border = 'none';
      removeImageBtn.style.display = 'block';
    };
    reader.readAsDataURL(file);
  } else {
    imagePreview.setAttribute('src', '');
    imagePreview.style.display = 'none';
    uploadImageIcon.classList.remove('hide');
  }
}

function removeImage() {
  imageInput.value = ''; // Clear the selected file
  previewImage({ target: imageInput }); // Reset the image preview
  removeImageBtn.style.display = 'none';
  uploadBtn.classList.remove('hide');
  uploadImageContainer.style.border = '2px dashed #fff';
}

//Trigger Post Product modal
displayPostProductModal.addEventListener('click', () => {
  postProductModal.style.display = 'block';
  overylay.style.display = 'block';
});

cancelProductModalBtn.addEventListener('click', () => {
  postProductModal.style.display = 'none';
  overylay.style.display = 'none';
});

//Trigger Product more details modal
moreDetailsBtn.forEach((btn) => {
  btn.addEventListener('click', () => {
    productMoreDetailsModal.style.display = 'block';
    overylay.style.display = 'block';
  });
});

//Close Product more details modal
cancelMoreDetailsModalBtn.addEventListener('click', () => {
  productMoreDetailsModal.style.display = 'none';
  overylay.style.display = 'none';
});

//Submitting Buyer farm details

const submitCustomerForm = () => {
  const form = document.getElementById('customer-form');
  const formData = new FormData(form);

  //Add the default query parameter
  formData.append('user_type', 'Customer');

  fetch('/api/v1/register', {
    method: 'POST',
    body: formData,
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      if (data.status === 'success') {
        window.location.href = 'pages/login.html';
      }
    })
    .catch((err) => console.log(err));
};

//Submitting Farmer farm details
const submitFarmerForm = () => {
  const form = document.getElementById('farmer-form');
  const formData = new FormData(form);

  //Add the default query parameter
  formData.append('user_type', 'Farmer');

  fetch('/api/v1/register', {
    method: 'POST',
    body: formData,
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      if (data.status === 'success') {
        window.location.href = 'pages/login.html';
      }
    })
    .catch((err) => console.log(err));
};
