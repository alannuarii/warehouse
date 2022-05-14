const number = (ang) => {
  const nilai = Math.round(Math.random() * Math.random() * Math.random() * Math.random() * ang);
  return nilai;
};

document.querySelector(".random").value = number(123456789);
