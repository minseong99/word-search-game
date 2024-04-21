const displayBoard = (word, startRow, startCol, direction) => {
  let row = startRow;
  let col = startCol;
  for (let i = 0; i < word.length; i++) {
    const dataKey = row.toString() + col.toString();

    const targetDiv = document.querySelector(
      `.board-col[data-key='${dataKey}']`
    );

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

    const startRow = wordObj.start_row;
    console.log(startRow);
    const startCol = wordObj.start_col;
    console.log(startCol);
    const direction = wordObj.direction;
    displayWord(word);
    displayBoard(word, startRow, startCol, direction);
  });
};

const fetchGame = async () => {
  const res = await fetch("/game");
  const jsonRes = await res.json();

  displayGame(jsonRes);
};

fetchGame();
