const checkPassword = () => {
  const formData = new FormData(form);
  const password1 = formData.get("password");
  const password2 = formData.get("password2");

  if (password1 !== password2) return false;
  return true;
};

const handleSubmit = async (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  // sha256을 이용한 암호화
  const sha256Password = sha256(formData.get("password"));
  formData.set("password", sha256Password);

  if (!checkPassword()) {
    const div = document.createElement("div");
    div.innerText = "비밀번호가 틀렸습니다.";
    div.classList.add("password-error");
    form.appendChild(div);
    return;
  }

  // create
  const res = await fetch("/signup", {
    method: "POST",
    body: formData,
  });

  if (res.status === 200) {
    const div = document.createElement("div");
    div.innerText = "회원가입에 성공하였습니다.";
    div.classList.add("signup-complete");
    form.appendChild(div);
  }
};

const form = document.querySelector("#form-signup");
form.addEventListener("submit", handleSubmit);
