html ="""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="css/play.css" />
  </head>
  <body>
    <div class="game-into">
      <div class="game-info-text">
        <div class="game-title"></div>
        <div class="game-discription"></div>
        <div class="game-subject"></div>
      </div>

      <div class="game-info-timer">00:00</div>
    </div>

    <div class="game-board">
      <div class="answer">answer</div>
      <div class="board">
        <div class="board-row row0">
          <div class="board-col" data-key="00"></div>
          <div class="board-col" data-key="01"></div>
          <div class="board-col" data-key="02"></div>
          <div class="board-col" data-key="03"></div>
          <div class="board-col" data-key="04"></div>
          <div class="board-col" data-key="05"></div>
          <div class="board-col" data-key="06"></div>
          <div class="board-col" data-key="07"></div>
          <div class="board-col" data-key="08"></div>
          <div class="board-col" data-key="09"></div>
          <div class="board-col" data-key="010"></div>
          <div class="board-col" data-key="011"></div>
        </div>
        <div class="board-row row1">
          <div class="board-col" data-key="10"></div>
          <div class="board-col" data-key="11"></div>
          <div class="board-col" data-key="12"></div>
          <div class="board-col" data-key="13"></div>
          <div class="board-col" data-key="14"></div>
          <div class="board-col" data-key="15"></div>
          <div class="board-col" data-key="16"></div>
          <div class="board-col" data-key="17"></div>
          <div class="board-col" data-key="18"></div>
          <div class="board-col" data-key="19"></div>
          <div class="board-col" data-key="110"></div>
          <div class="board-col" data-key="111"></div>
        </div>
        <div class="board-row row2">
          <div class="board-col" data-key="20"></div>
          <div class="board-col" data-key="21"></div>
          <div class="board-col" data-key="22"></div>
          <div class="board-col" data-key="23"></div>
          <div class="board-col" data-key="24"></div>
          <div class="board-col" data-key="25"></div>
          <div class="board-col" data-key="26"></div>
          <div class="board-col" data-key="27"></div>
          <div class="board-col" data-key="28"></div>
          <div class="board-col" data-key="29"></div>
          <div class="board-col" data-key="210"></div>
          <div class="board-col" data-key="211"></div>
        </div>
        <div class="board-row row3">
          <div class="board-col" data-key="30"></div>
          <div class="board-col" data-key="31"></div>
          <div class="board-col" data-key="32"></div>
          <div class="board-col" data-key="33"></div>
          <div class="board-col" data-key="34"></div>
          <div class="board-col" data-key="35"></div>
          <div class="board-col" data-key="36"></div>
          <div class="board-col" data-key="37"></div>
          <div class="board-col" data-key="38"></div>
          <div class="board-col" data-key="39"></div>
          <div class="board-col" data-key="310"></div>
          <div class="board-col" data-key="311"></div>
        </div>
        <div class="board-row row4">
          <div class="board-col" data-key="40"></div>
          <div class="board-col" data-key="41"></div>
          <div class="board-col" data-key="42"></div>
          <div class="board-col" data-key="43"></div>
          <div class="board-col" data-key="44"></div>
          <div class="board-col" data-key="45"></div>
          <div class="board-col" data-key="46"></div>
          <div class="board-col" data-key="47"></div>
          <div class="board-col" data-key="48"></div>
          <div class="board-col" data-key="49"></div>
          <div class="board-col" data-key="410"></div>
          <div class="board-col" data-key="411"></div>
        </div>

        <div class="board-row row5">
          <div class="board-col" data-key="50"></div>
          <div class="board-col" data-key="51"></div>
          <div class="board-col" data-key="52"></div>
          <div class="board-col" data-key="53"></div>
          <div class="board-col" data-key="54"></div>
          <div class="board-col" data-key="55"></div>
          <div class="board-col" data-key="56"></div>
          <div class="board-col" data-key="57"></div>
          <div class="board-col" data-key="58"></div>
          <div class="board-col" data-key="59"></div>
          <div class="board-col" data-key="510"></div>
          <div class="board-col" data-key="511"></div>
        </div>
        <div class="board-row row6">
          <div class="board-col" data-key="60"></div>
          <div class="board-col" data-key="61"></div>
          <div class="board-col" data-key="62"></div>
          <div class="board-col" data-key="63"></div>
          <div class="board-col" data-key="64"></div>
          <div class="board-col" data-key="65"></div>
          <div class="board-col" data-key="66"></div>
          <div class="board-col" data-key="67"></div>
          <div class="board-col" data-key="68"></div>
          <div class="board-col" data-key="69"></div>
          <div class="board-col" data-key="610"></div>
          <div class="board-col" data-key="611"></div>
        </div>
        <div class="board-row row7">
          <div class="board-col" data-key="70"></div>
          <div class="board-col" data-key="71"></div>
          <div class="board-col" data-key="72"></div>
          <div class="board-col" data-key="73"></div>
          <div class="board-col" data-key="74"></div>
          <div class="board-col" data-key="75"></div>
          <div class="board-col" data-key="76"></div>
          <div class="board-col" data-key="77"></div>
          <div class="board-col" data-key="78"></div>
          <div class="board-col" data-key="79"></div>
          <div class="board-col" data-key="710"></div>
          <div class="board-col" data-key="711"></div>
        </div>
        <div class="board-row row8">
          <div class="board-col" data-key="80"></div>
          <div class="board-col" data-key="81"></div>
          <div class="board-col" data-key="82"></div>
          <div class="board-col" data-key="83"></div>
          <div class="board-col" data-key="84"></div>
          <div class="board-col" data-key="85"></div>
          <div class="board-col" data-key="86"></div>
          <div class="board-col" data-key="87"></div>
          <div class="board-col" data-key="88"></div>
          <div class="board-col" data-key="89"></div>
          <div class="board-col" data-key="810"></div>
          <div class="board-col" data-key="811"></div>
        </div>
        <div class="board-row row9">
          <div class="board-col" data-key="90"></div>
          <div class="board-col" data-key="91"></div>
          <div class="board-col" data-key="92"></div>
          <div class="board-col" data-key="93"></div>
          <div class="board-col" data-key="94"></div>
          <div class="board-col" data-key="95"></div>
          <div class="board-col" data-key="96"></div>
          <div class="board-col" data-key="97"></div>
          <div class="board-col" data-key="98"></div>
          <div class="board-col" data-key="99"></div>
          <div class="board-col" data-key="910"></div>
          <div class="board-col" data-key="911"></div>
        </div>
        <div class="board-row row10">
          <div class="board-col" data-key="100"></div>
          <div class="board-col" data-key="101"></div>
          <div class="board-col" data-key="102"></div>
          <div class="board-col" data-key="103"></div>
          <div class="board-col" data-key="104"></div>
          <div class="board-col" data-key="105"></div>
          <div class="board-col" data-key="106"></div>
          <div class="board-col" data-key="107"></div>
          <div class="board-col" data-key="108"></div>
          <div class="board-col" data-key="109"></div>
          <div class="board-col" data-key="1010"></div>
          <div class="board-col" data-key="1011"></div>
        </div>
        <div class="board-row row11">
          <div class="board-col" id="110" data-key="110"></div>
          <div class="board-col" id="111" data-key="111"></div>
          <div class="board-col" data-key="112"></div>
          <div class="board-col" data-key="113"></div>
          <div class="board-col" data-key="114"></div>
          <div class="board-col" data-key="115"></div>
          <div class="board-col" data-key="116"></div>
          <div class="board-col" data-key="117"></div>
          <div class="board-col" data-key="118"></div>
          <div class="board-col" data-key="119"></div>
          <div class="board-col" data-key="1110"></div>
          <div class="board-col" data-key="1111"></div>
        </div>
        <div class="board-row row12">
          <div class="board-col" data-key="120"></div>
          <div class="board-col" data-key="121"></div>
          <div class="board-col" data-key="122"></div>
          <div class="board-col" data-key="123"></div>
          <div class="board-col" data-key="124"></div>
          <div class="board-col" data-key="125"></div>
          <div class="board-col" data-key="126"></div>
          <div class="board-col" data-key="127"></div>
          <div class="board-col" data-key="128"></div>
          <div class="board-col" data-key="129"></div>
          <div class="board-col" data-key="1210"></div>
          <div class="board-col" data-key="1211"></div>
        </div>
        <div class="board-row row13">
          <div class="board-col" data-key="130"></div>
          <div class="board-col" data-key="131"></div>
          <div class="board-col" data-key="132"></div>
          <div class="board-col" data-key="133"></div>
          <div class="board-col" data-key="134"></div>
          <div class="board-col" data-key="135"></div>
          <div class="board-col" data-key="136"></div>
          <div class="board-col" data-key="137"></div>
          <div class="board-col" data-key="138"></div>
          <div class="board-col" data-key="139"></div>
          <div class="board-col" data-key="1310"></div>
          <div class="board-col" data-key="1311"></div>
        </div>
      </div>
      <div class="score"></div>
    </div>

    <script src="js/play.js"></script>
  </body>
</html>
"""