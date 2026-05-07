// SYSTEM STATUS (main Jarvis state)
eel.expose(updateSystem);

function updateSystem(text) {
  document.getElementById("system").innerHTML = `
    // <h3>SYSTEM</h3>
    ${text}
  `;
}


// NETWORK PANEL
eel.expose(updateNetwork);

function updateNetwork(data) {
  document.getElementById("network").innerHTML = `
    // <h3>NETWORK</h3>
    ${text}
  `;
}


// WEATHER PANEL
eel.expose(updateWeather);

function updateWeather(data) {
  document.getElementById("weather").innerHTML = `
    // <h3>WEATHER</h3>
    Temp: ${data.temp}°C <br>
    Humidity: ${data.hum}% <br>
    Wind: ${data.wind}
  `;
}


// NEWS PANEL
eel.expose(updateNews);

function updateNews(items) {
  let list = items.map(i => `<li>${i}</li>`).join("");

  document.getElementById("news").innerHTML = `
    // <h3>NEWS</h3>
    ${text}
  `;
}