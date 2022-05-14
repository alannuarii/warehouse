const tglMasuk = document.querySelector(".tglMasuk");

tglMasuk.onchange = function () {
  document.querySelector(".tglIn").value = tglMasuk.value;
};
