const handleSubmit = async (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const sha256Password = sha256(formData.get("password"));
  formData.set("password", sha256Password);

  const res = await fetch("/login", {
    method: "POST",
    body: formData,
  });
  const resJson = await res.json();
  const alert = document.querySelector(".no-exist");
  if (res.status === 200) {
    const div = document.createElement("div");
    div.innerText = "로그인에 성공하였습니다.";
    div.style.background = "aqua";
    form.appendChild(div);
  } else {
    if (alert) form.removeChild(alert);
    const div = document.createElement("div");
    div.innerText = "아이디 혹은 비밀번호가 같지 않습니다.";
    div.style.background = "red";
    div.className = "no-exist";
    form.appendChild(div);
  }
};

const form = document.querySelector(".form-login");
form.addEventListener("submit", handleSubmit);
