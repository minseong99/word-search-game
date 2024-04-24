let answerCnt = 0;
let currectCnt = 0;
const Alpha = "abcdefghijklmnopqrstuvwxyz";
const row = 14;
const col = 12;
let timer;
let startTime;

let total = 0;
const pathname = window.location.pathname;
let userName;
const ws = new WebSocket("ws://localhost:8000/ws");
ws.onmessage = async function (event) {
  const scoreData = JSON.parse(event.data);
  const name = scoreData.userName;
  const total = scoreData.total;

  const score = document.querySelector(".score");

  if (score.lastChild !== null) {
    if (score.lastChild.className === "soket-score") {
      score.removeChild(score.lastChild);
    }
  }
  const div = document.createElement("div");
  div.innerText = `name: ${name}   score:${total} `;
  div.className = "soket-score";
  score.appendChild(div);
};

const completeBoard = () => {
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      const dataKey = i.toString() + j.toString();
      let block = document.querySelector(`.board-col[data-key='${dataKey}']`);
      if (
        i.toString() === "11" &&
        (j.toString() === "0" || j.toString() === "1")
      ) {
        block = document.getElementById(`${dataKey}`);
      }

      if (block.innerText === "") {
        block.innerText = Alpha[Math.floor(Math.random() * Alpha.length)];
      }
    }
  }
};

const displayBoard = (word, startRow, startCol, direction) => {
  let row = startRow;
  let col = startCol;
  for (let i = 0; i < word.length; i++) {
    const dataKey = row.toString() + col.toString();

    let targetDiv = document.querySelector(`.board-col[data-key='${dataKey}']`);
    if (
      row.toString() === "11" &&
      (col.toString() === "0" || col.toString() === "1")
    ) {
      targetDiv = document.getElementById(`${dataKey}`);
    }

    targetDiv.innerText = word[i];
    targetDiv.style = "";
    if (direction === "right") col += 1;
    else if (direction === "down") row += 1;
    else if (direction === "right-down") (row += 1), (col += 1);
  }
};

const displayWord = (word) => {
  const answerDiv = document.querySelector(".answer");
  const div = document.createElement("div");
  div.innerText = word;
  div.style.background = "aqua";
  div.className = word;

  answerDiv.appendChild(div);
};

const displayGame = (data) => {
  const titleDiv = document.querySelector(".game-title");
  titleDiv.innerText = `title: ${data[0].title}`;

  const descriptionDiv = document.querySelector(".game-discription");
  descriptionDiv.innerText = `description: ${data[0].description}`;

  const subjectDiv = document.querySelector(".game-subject");
  subjectDiv.innerText = `subject: ${data[0].subject}`;

  data.forEach((wordObj) => {
    const word = wordObj.word;
    answerCnt += 1;
    const startRow = wordObj.start_row;

    const startCol = wordObj.start_col;

    const direction = wordObj.direction;
    displayWord(word);
    displayBoard(word, startRow, startCol, direction);
  });
  // completeBoard();
};

const fetchGame = async (input) => {
  const pathName = window.location.pathname;
  const res = await fetch(`/game${pathName}`);
  const jsonRes = await res.json();

  displayGame(jsonRes);
  startTime = new Date();

  const setTime = () => {
    const curTime = new Date();
    const passedTime = new Date(curTime - startTime);
    const minutes = passedTime.getMinutes().toString().padStart(2, "0");
    const seconds = passedTime.getSeconds().toString().padStart(2, "0");

    const timer = document.querySelector(".game-info-timer");
    timer.innerText = `${minutes}:${seconds}`;
  };

  timer = setInterval(setTime, 1000);
  const makeScoreBoard = async () => {
    const title = pathname.split("/")[2];
    const scoreDiv = document.querySelector(".score");
    const res = await fetch(`/score${title}`);
    const jsonRes = await res.json();
    jsonRes.forEach((obj) => {
      const name = obj.name;
      const score = obj.score;
      const time = obj.complete_time;

      const div = document.createElement("div");
      div.innerText = `name:${name}  score:${score}  time:${time}`;

      scoreDiv.appendChild(div);
    });
  };
  makeScoreBoard();
};

//mouse down
const handleMouseDown = (event) => {
  let word = "";
  let dataKey = "";
  let blocks = [];
  const cleanBlockColor = () => {
    blocks.forEach((block) => {
      block.style.background = "white";
    });
  };
  //mouse move
  const handleMouseMove = (event) => {
    console.log(event.offsetX, event.offsetY);
    const x = event.offsetX;
    const y = event.offsetY;
    //(x - 20)^2 + (y - 20)^2 = 25
    if (!(Math.pow(x - 20, 2) + Math.pow(y - 20, 2) <= 49)) return;
    if (dataKey !== event.target.dataset.key) {
      console.log(event.offsetX);
      dataKey = event.target.dataset.key;

      word += event.target.innerText;
      let block = document.querySelector(`.board-col[data-key='${dataKey}']`);
      if (event.target.id === "110" || event.target.id === "111") {
        block = document.getElementById(`${dataKey}`);
      }

      block.style.background = "aqua";
      blocks.push(block);
    }
  };

  document.addEventListener("mousemove", handleMouseMove);

  //mouseup
  board.onmouseup = async function () {
    const res = await fetch(`/answer${word}`);
    const jsonRes = await res.json();

    if (jsonRes === "exist") {
      const tableName = pathname.split("/")[2];
      currectCnt += 1;
      total += 100;
      const messageObj = {
        tableName: tableName,
        userName: userName,
        total: total,
      };
      ws.send(JSON.stringify(messageObj));

      const div = document.querySelector(`.${word}`);
      div.remove();
      if (currectCnt === answerCnt) {
        const currentTime = new Date();
        const passedTime = new Date(currentTime - startTime);
        const title = pathname.split("/")[2];
        const res = await fetch("/score", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            name: userName,
            score: total,
            time: passedTime.getTime(),
            title,
          }),
        });

        alert("Congraturation!!");
        clearInterval(timer);
        window.location.pathname = "/gameurl.html";
      }
    } else cleanBlockColor();

    document.removeEventListener("mousemove", handleMouseMove);
    board.onmouseup = null;
  };
};

const checkInput = () => {
  const input = document.querySelector("#input-user-name");
  if (input.value.length > 1) {
    userName = input.value;
    const body = document.querySelector("body");
    const targetDiv = document.querySelector(".start");
    body.removeChild(targetDiv);
    board.addEventListener("mousedown", handleMouseDown);
    //브라우저 자체적으로 이미지나 요소에 대한 드래그 앤 드롭을
    //지원하기 때문에 브라우저에서 제공하는 기능이 자동 실행되어
    //작성한 코드와 충돌하여 이것을 막기 위해 false로 설정
    board.ondragstart = function () {
      return false;
    };
    fetchGame();
  }
};

const inputUserNameAndStart = () => {
  const body = document.querySelector("body");
  const div = document.createElement("div");
  div.className = "start";
  div.style =
    "position:fixed; top:30%; left:40%; width:400px; height:100px; background-color:red";

  const input = document.createElement("input");
  input.placeholder = "input name!";
  input.type = "text";
  input.id = "input-user-name";
  input.style = "width:80%; height:20%;";

  const button = document.createElement("button");
  button.innerText = "start";
  button.addEventListener("click", checkInput);
  button.style = "width:40%; height:20%;";

  div.appendChild(input);
  div.appendChild(button);
  body.appendChild(div);
};

inputUserNameAndStart();

const board = document.querySelector(".board");
