const form = document.querySelector("#form-block");

const findSubject = () => {
  const checkBoxs = document.getElementsByName("check");
  let subject;
  checkBoxs.forEach((box) => {
    if (box.checked === true) {
      subject = box.id;
    }
  });
  return subject;
};

const checkWordLength = (result) => {
  const word_list = document.querySelector("#word_list");
  const div = document.querySelector("#alert-message");
  if (div != null) word_list.removeChild(div);
  if (result.length < 2) {
    const alert = document.createElement("div");
    alert.id = "alert-message";
    alert.innerText = "At least 10 words are required";
    word_list.appendChild(alert);
    return false;
  }
  return true;
};

const requestMakeGame = async (title, description, wordList, subject) => {
  let access_token = window.localStorage.getItem("access_token");
  const refresh_token = window.localStorage.getItem("refresh_token");
  const res = await fetch("/game", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${access_token}`,
    },
    body: JSON.stringify({
      title,
      description,
      wordList,
      subject,
    }),
  });
  const jsonRes = await res.json();
  if (res.status === 200) {
    localStorage.setItem("url", jsonRes);
    window.location.pathname = "/gameurl.html";
  } else if (res.status === 401) {
    alert("refresh_token이 만료되었습니다.");
    const refreshRes = await fetch(`/token/${refresh_token}`);
    if (refreshRes.status === 401) window.location.pathname = "/login.html";
    const data = await refreshRes.json();
    access_token = data.access_token;
    window.localStorage.setItem("access_token", access_token);
    window.location.pathname = "/";
  }
};

const handleSubmit = (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const words = formData.getAll("word");
  const title = formData.get("title");
  const description = formData.get("description");

  let subject = findSubject(); // on 또는 null

  // filtering
  wordList = words.filter((word) => word.length > 0);
  if (!checkWordLength(wordList)) {
    return;
  }

  requestMakeGame(title, description, wordList, subject);
};

form.addEventListener("submit", handleSubmit);

const checkOnlyOne = (element) => {
  const checkBoxs = document.getElementsByName("check");

  checkBoxs.forEach((box) => {
    box.checked = false;
  });
  element.checked = true;
};
