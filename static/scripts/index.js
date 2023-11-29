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
