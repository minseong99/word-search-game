const url = localStorage.getItem("url");

const url2 = new URL(url);

const displayURL = () => {
  const playURL = document.querySelector("#play");
  playURL.innerText = url;
};

const moveToPlay = () => {
  window.location.href = url2;
};

displayURL();
