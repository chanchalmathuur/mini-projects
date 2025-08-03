let timer;
let startTime;
let elapsedTime = 0;
let isRunning = false;

function updateDisplay() {
  const display = document.getElementById("display");
  const time = Date.now() - startTime + elapsedTime;

  const hrs = Math.floor(time / (1000 * 60 * 60));
  const mins = Math.floor((time % (1000 * 60 * 60)) / (1000 * 60));
  const secs = Math.floor((time % (1000 * 60)) / 1000);

  // ✅ Corrected template literal usage
  display.textContent = `${hrs.toString().padStart(2, '0')}:${mins
    .toString()
    .padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
}

function start() {
  if (!isRunning) {
    startTime = Date.now();
    timer = setInterval(updateDisplay, 1000);
    isRunning = true;
  }
}

function pause() {
  if (isRunning) {
    clearInterval(timer);
    elapsedTime += Date.now() - startTime;
    isRunning = false;
  }
}

function reset() {
  clearInterval(timer);
  isRunning = false;
  elapsedTime = 0;
  document.getElementById("display").textContent = "00:00:00";
  document.getElementById("laps").innerHTML = "";
}

function lap() {
  if (isRunning) {
    const lapTime = document.getElementById("display").textContent;
    const lapList = document.getElementById("laps");
    const li = document.createElement("li");

    // ✅ Corrected template literal usage
    li.textContent = `Lap ${lapList.children.length + 1}: ${lapTime}`;
    lapList.appendChild(li);
  }
}
