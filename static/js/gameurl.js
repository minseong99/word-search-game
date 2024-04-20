const displayURL = () => {
  const playUrl = new URL("http://127.0.0.1:8000/game");

  const answerUrl = new URL("http://127.0.0.1:8000/answer");
  const playURL = document.querySelector("#play");
  playURL.innerText = playUrl;

  const answerURL = document.querySelector("#answer");
  answerURL.innerText = answerUrl;
};

const moveToPlay = () => {
  window.location.pathname = "/play.html";
};

const moveToAnswer = () => {
  window.location.pathname = "/answer.html";
};

displayURL();
