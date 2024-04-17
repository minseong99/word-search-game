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
  if (result.length < 10) {
    const alert = document.createElement("div");
    alert.id = "alert-message";
    alert.innerText = "At least 10 words are required";
    word_list.appendChild(alert);
    return;
  }
};

const handleSubmit = (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const words = formData.getAll("word");

  let subject = findSubject(); // on 또는 null

  // filtering
  result = words.filter((word) => word.length > 0);
  checkWordLength(result);
};

form.addEventListener("submit", handleSubmit);

const checkOnlyOne = (element) => {
  const checkBoxs = document.getElementsByName("check");

  checkBoxs.forEach((box) => {
    box.checked = false;
  });
  element.checked = true;
};
