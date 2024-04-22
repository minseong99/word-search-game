const displayURL = () => {
  const url = `http://127.0.0.1:8000/play.html`;

  const playURL = document.querySelector("#play");
  playURL.innerText = url;
};

const moveToPlay = () => {
  window.location.pathname = `/play.html`;
};

displayURL();
