const input = document.querySelectorAll(".modal input");

input.forEach((el) => {
  el.addEventListener("dblclick", function () {
    el.removeAttribute("readonly");
  });
});