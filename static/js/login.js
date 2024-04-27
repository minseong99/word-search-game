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
    const access_token = resJson.access_token;
    const refresh_token = resJson.refresh_token;
    window.localStorage.setItem("access_token", access_token);
    window.localStorage.setItem("refresh_token", refresh_token);
    window.location.pathname = "/";
  } else {
    if (alert) form.removeChild(alert);
    const div = document.createElement("div");
    div.innerText = "아이디 혹은 비밀번호가 같지 않습니다.";
    div.style.background = "red";
    div.className = "no-exist";
    form.appendChild(div);
  }
};
const moveToSignup = () => {
  window.location.pathname = "/signup.html";
};

const form = document.querySelector(".form-login");
form.addEventListener("submit", handleSubmit);
const button = document.querySelector("#moveToSignUp");
button.addEventListener("click", moveToSignup);
