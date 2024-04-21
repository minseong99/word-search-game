let answerCnt = 0;
let currectCnt = 0;
const Alpha = "abcdefghijklmnopqrstuvwxyz";
const row = 14;
const col = 12;

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
        console.log(block);
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
  completeBoard();
};

const fetchGame = async () => {
  const res = await fetch("/game");
  const jsonRes = await res.json();

  displayGame(jsonRes);
};

const handleDragEvent = (event) => {
  console.log(event.target);
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
    if (dataKey !== event.target.dataset.key) {
      dataKey = event.target.dataset.key;
      console.log(event.target.id);
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
      currectCnt += 1;
      console.log(currectCnt);
      const div = document.querySelector(`.${word}`);
      div.remove();
      if (currectCnt === answerCnt) {
        alert("Congraturation!!");
        window.location.pathname = "/gameurl.html";
      }
    } else cleanBlockColor();

    document.removeEventListener("mousemove", handleMouseMove);
    board.onmouseup = null;
  };
};

fetchGame();

const board = document.querySelector(".board");
board.addEventListener("mousedown", handleMouseDown);
//브라우저 자체적으로 이미지나 요소에 대한 드래그 앤 드롭을
//지원하기 때문에 브라우저에서 제공하는 기능이 자동 실행되어
//작성한 코드와 충돌하여 이것을 막기 위해 false로 설정
board.ondragstart = function () {
  return false;
};
