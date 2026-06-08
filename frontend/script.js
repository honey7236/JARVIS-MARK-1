// SYSTEM STATUS (main Jarvis state)
eel.expose(updateSystem);
function updateSystem(data) {
  const el = document.getElementById("system");
  if (el) {
    let display = "";
    if (typeof data === 'string') {
      display = `<div>${data}</div>`;
    } else if (data && typeof data === 'object') {
      display = `
        <div style="display: flex; flex-direction: column; gap: 4px; font-family: monospace; font-size: 11px; line-height: 1.3;">
          <div>CPU: <span style="color: #00ffcc">${data.cpu || "N/A"}</span></div>
          <div>RAM: <span style="color: #00ffcc">${data.ram_percent || "N/A"}</span> (USED: <span style="color: #00ffcc">${data.ram_details || "N/A"}</span>)</div>
          <div>DISK: <span style="color: #00ffcc">${data.disk_percent || "N/A"}</span> (FREE: <span style="color: #00ffcc">${data.disk_details || "N/A"}</span>)</div>
        </div>
      `;
    } else {
      display = "<div>System stats unavailable</div>";
    }
    el.innerHTML = `
      <div style="font-weight: bold; font-size: 11px; margin-bottom: 5px; text-transform: uppercase;"></div>
      ${display}
    `;
  }
}


// NETWORK PANEL
eel.expose(updateNetwork);
function updateNetwork(data) {
  const el = document.getElementById("network");
  if (el) {
    if (typeof data === 'string') {
      el.innerHTML = `
        <div style="font-weight: bold; font-size: 11px; margin-bottom: 5px; text-transform: uppercase;"></div>
        <div>${data}</div>
      `;
      return;
    }
    
    const statusColor = data.status === 'Connected' ? '#00ffcc' : '#ff3366';
    el.innerHTML = `
      <div style="font-weight: bold; font-size: 11px; margin-bottom: 5px; text-transform: uppercase;"></div>
      <div style="display: flex; flex-direction: row; gap: 15px; font-family: monospace; font-size: 11px; align-items: center;">
        <span>SYS: <span style="color: ${statusColor}">${data.status}</span></span>
        <span>PING: <span style="color: #00ffcc">${data.ping}</span></span>
        <span>DL: <span style="color: #00ffcc">${data.download}</span></span>
        <span>UL: <span style="color: #00ffcc">${data.upload}</span></span>
      </div>
    `;
  }
}


// WEATHER PANEL
eel.expose(updateWeather);
function updateWeather(data) {
  const el = document.getElementById("weather");
  if (el) {
    let display = "";
    if (typeof data === 'string') {
      display = `<div>${data}</div>`;
    } else if (data && typeof data === 'object') {
      display = `
        <div style="display: flex; flex-direction: column; gap: 4px; font-family: monospace; font-size: 11px; line-height: 1.3;">
          <div>LOC: <span style="color: #00ffcc">${data.city || "N/A"}</span></div>
          <div>TEMP: <span style="color: #00ffcc">${data.temp || "N/A"}</span> (FEELS: <span style="color: #00ffcc">${data.feels_like || "N/A"}</span>)</div>
          <div>COND: <span style="color: #00ffcc">${data.description || "N/A"}</span></div>
          <div>HUMID: <span style="color: #00ffcc">${data.humidity || "N/A"}</span></div>
          <div>WIND: <span style="color: #00ffcc">${data.wind || "N/A"}</span></div>
        </div>
      `;
    } else {
      display = "<div>Weather unavailable</div>";
    }
    el.innerHTML = `
      <div style="font-weight: bold; font-size: 11px; margin-bottom: 5px; text-transform: uppercase;"></div>
      ${display}
    `;
  }
}


// NEWS PANEL
eel.expose(updateNews);
function updateNews(items) {
  const el = document.getElementById("news");
  if (el) {
    let newsHTML = "";
    if (Array.isArray(items)) {
      newsHTML = items.map(h => `<div style="margin-bottom: 6px; border-left: 2px solid cyan; padding-left: 6px; line-height: 1.2;">${h}</div>`).join("");
    } else if (typeof items === 'string' && items.trim().length > 0) {
      const headlines = items.split("\n");
      newsHTML = headlines.map(h => `<div style="margin-bottom: 6px; border-left: 2px solid cyan; padding-left: 6px; line-height: 1.2;">${h}</div>`).join("");
    } else {
      newsHTML = "<div>No news available</div>";
    }

    el.innerHTML = `
      <div style="display: flex; justify-content: flex-end; align-items: center; margin-bottom: 6px;">
        <button onclick="triggerNewsRefresh(event)" style="background: transparent; border: 1px solid #00ffff; color: #00ffff; font-family: monospace; font-size: 9px; cursor: pointer; padding: 2px 8px; border-radius: 3px; letter-spacing: 1px; transition: all 0.2s; box-shadow: 0 0 5px rgba(0,255,255,0.2);" onmouseover="this.style.background='#00ffff'; this.style.color='#000'; this.style.boxShadow='0 0 10px #00ffff'" onmouseout="this.style.background='transparent'; this.style.color='#00ffff'; this.style.boxShadow='0 0 5px rgba(0,255,255,0.2)'">REFRESH</button>
      </div>
      <div class="news-scroll" style="max-height: 80%; overflow-y: auto; padding-right: 4px; font-family: monospace; font-size: 11px;">${newsHTML}</div>
    `;
  }
}

async function triggerNewsRefresh(event) {
  if (event) event.preventDefault();
  
  const el = document.getElementById("news");
  if (el) {
    el.innerHTML = `
      <div style="display: flex; justify-content: flex-end; align-items: center; margin-bottom: 6px;">
        <span style="font-family: monospace; font-size: 9px; color: #00ffff; letter-spacing: 1px;">REFRESHING...</span>
      </div>
      <div style="font-family: monospace; font-size: 11px; color: #00ffff; opacity: 0.7;">Fetching latest headlines from GNews...</div>
    `;
  }
  
  try {
    const newsData = await eel.get_news_data()();
    updateNews(newsData);
  } catch (error) {
    console.error("Error refreshing news:", error);
    updateNews("News unavailable");
  }
}


// INITIALIZE AND FETCH DATA ON STARTUP
async function initDashboard() {
  try {
    // 1. Network Status
    const networkData = await eel.get_network_status()();
    updateNetwork(networkData);
  } catch (error) {
    console.error("Error fetching network status:", error);
    updateNetwork("Disconnected (Offline)");
  }

  try {
    // 2. Weather Status
    const weatherData = await eel.get_weather_data()();
    updateWeather(weatherData);
  } catch (error) {
    console.error("Error fetching weather status:", error);
    updateWeather("Weather unavailable");
  }

  try {
    // 3. News Status
    const newsData = await eel.get_news_data()();
    updateNews(newsData);
  } catch (error) {
    console.error("Error fetching news status:", error);
    updateNews("News unavailable");
  }

  try {
    // 4. System Info (Keep empty for now as requested)
    const systemData = await eel.get_system_data()();
    updateSystem(systemData);
  } catch (error) {
    console.error("Error fetching system info:", error);
    updateSystem("");
  }

  try {
    // 5. Load last session messages
    const sessionData = await eel.get_last_session_messages()();
    if (sessionData && Array.isArray(sessionData)) {
      sessionData.forEach(msg => {
        if (msg.role === 'you') {
          userMessages.push(msg.content);
        } else if (msg.role === 'jarvis') {
          jarvisMessages.push(msg.content);
        }
      });
      renderUserInput();
      renderJarvisOutput();
    }
  } catch (error) {
    console.error("Error fetching session data:", error);
  }
}

// USER INPUT AND JARVIS OUTPUT PANELS WITH SCROLLING CHAT HISTORY
let userMessages = [];
let jarvisMessages = [];

eel.expose(updateUserInput);
function updateUserInput(content) {
  userMessages.push(content);
  renderUserInput();
}

function renderUserInput() {
  const el = document.getElementById("user-input");
  if (el) {
    const contentHTML = userMessages.map(msg => `
      <div style="margin-bottom: 6px; line-height: 1.3;">${msg}</div>
    `).join("");
    el.innerHTML = `
      <div style="font-weight: bold; font-size: 11px; margin-bottom: 5px; text-transform: uppercase; color: #00ffff;">USER INPUT:</div>
      <div class="chat-history-scroll" style="height: calc(100% - 20px); overflow-y: auto; font-family: monospace; font-size: 11px; color: #00ffcc; word-wrap: break-word;">
        ${contentHTML}
      </div>
    `;
    const scrollEl = el.querySelector(".chat-history-scroll");
    if (scrollEl) {
      scrollEl.scrollTop = scrollEl.scrollHeight;
    }
  }
}

eel.expose(updateJarvisOutput);
function updateJarvisOutput(content) {
  jarvisMessages.push(content);
  renderJarvisOutput();
}

function renderJarvisOutput() {
  const el = document.getElementById("jarvis-output");
  if (el) {
    const contentHTML = jarvisMessages.map(msg => `
      <div style="margin-bottom: 6px; line-height: 1.3;">${msg}</div>
    `).join("");
    el.innerHTML = `
      <div style="font-weight: bold; font-size: 11px; margin-bottom: 5px; text-transform: uppercase; color: #00ffff;">JARVIS:</div>
      <div class="chat-history-scroll" style="height: calc(100% - 20px); overflow-y: auto; font-family: monospace; font-size: 11px; color: #00ffcc; word-wrap: break-word;">
        ${contentHTML}
      </div>
    `;
    const scrollEl = el.querySelector(".chat-history-scroll");
    if (scrollEl) {
      scrollEl.scrollTop = scrollEl.scrollHeight;
    }
  }
}

// ORCHESTRATE INTRO TO DASHBOARD TRANSITION
let isActivated = false;

function activateJarvis() {
  if (isActivated) return;
  isActivated = true;

  const dashboard = document.getElementById("dashboard");
  const bgVideo = document.getElementById("bg-video");

  if (!dashboard) return;

  // Fade out background video to reveal JARVIS.png underneath
  if (bgVideo) {
    bgVideo.classList.add("video-fade-out");
  }

  // Fade in dashboard
  dashboard.classList.remove("dashboard-hidden");
  dashboard.classList.add("dashboard-visible");
}

// Run dashboard initialization when DOM is loaded
window.addEventListener("DOMContentLoaded", () => {
  // Pre-load dashboard data
  initDashboard();

  // Handle single-play video end event to automatically transition
  const bgVideo = document.getElementById("bg-video");
  if (bgVideo) {
    bgVideo.addEventListener("ended", () => {
      activateJarvis();
    });
    
    // Fallback: If video fails to load or play, auto-activate after 5 seconds
    setTimeout(() => {
      if (!isActivated) activateJarvis();
    }, 5000);
  } else {
    // If no video is present, activate immediately
    activateJarvis();
  }
  
  // Pre-load contacts
  loadContacts();
});

// OPTIONS MENU LOGIC
function toggleMenu(event) {
  if (event) event.stopPropagation();
  const dropdown = document.getElementById("menu-dropdown");
  if (dropdown) {
    dropdown.classList.toggle("menu-dropdown-visible");
  }
}

function triggerMenuAction(action, event) {
  if (event) event.stopPropagation();
  
  // Close the dropdown menu
  const dropdown = document.getElementById("menu-dropdown");
  if (dropdown) {
    dropdown.classList.remove("menu-dropdown-visible");
  }
  
  if (action === 'contacts') {
    toggleContactsPanel();
  }
}

// Global click handler to close the menu dropdown if clicking outside
window.addEventListener("click", (e) => {
  const dropdown = document.getElementById("menu-dropdown");
  const toggleBtn = document.getElementById("menu-toggle");
  
  if (dropdown && dropdown.classList.contains("menu-dropdown-visible")) {
    if (!dropdown.contains(e.target) && e.target !== toggleBtn) {
      dropdown.classList.remove("menu-dropdown-visible");
    }
  }
});

// CONTACTS DATABASE WIDGET LOGIC
let allContacts = {};

function toggleContactsPanel() {
  const panel = document.getElementById("contacts-panel");
  if (!panel) return;
  
  panel.classList.toggle("contacts-panel-visible");
  
  if (panel.classList.contains("contacts-panel-visible")) {
    loadContacts();
    setTimeout(() => {
      const search = document.getElementById("contacts-search");
      if (search) search.focus();
    }, 300);
  }
}

async function loadContacts() {
  try {
    const contacts = await eel.get_contacts()();
    allContacts = contacts || {};
    renderContacts(allContacts);
  } catch (error) {
    console.error("Error loading contacts:", error);
    showStatus("FAILED TO LOAD CONTACTS", "error");
  }
}

function renderContacts(contacts) {
  const container = document.getElementById("contacts-list");
  if (!container) return;
  
  const searchInput = document.getElementById("contacts-search");
  const filter = searchInput ? searchInput.value.toLowerCase().trim() : "";
  
  container.innerHTML = "";
  
  const keys = Object.keys(contacts).sort();
  let count = 0;
  
  keys.forEach(name => {
    const phone = contacts[name];
    if (filter && !name.includes(filter) && !phone.includes(filter)) {
      return;
    }
    
    count++;
    
    const item = document.createElement("div");
    item.className = "contact-item";
    
    item.innerHTML = `
      <div class="contact-details">
        <span class="contact-name-display">${escapeHtml(name)}</span>
        <span class="contact-phone-display">${escapeHtml(phone)}</span>
      </div>
      <div class="contact-actions">
        <button class="action-icon-btn edit-btn" onclick="editContact('${escapeJsString(name)}', '${escapeJsString(phone)}')">EDIT</button>
        <button class="action-icon-btn delete-btn" onclick="deleteContact('${escapeJsString(name)}')">DEL</button>
      </div>
    `;
    container.appendChild(item);
  });
  
  if (count === 0) {
    container.innerHTML = `<div style="text-align: center; font-family: monospace; font-size: 11px; opacity: 0.6; padding-top: 20px; color: #00ffff; letter-spacing: 1px;">NO CONTACTS FOUND</div>`;
  }
}

function filterContacts() {
  renderContacts(allContacts);
}

function editContact(name, phone) {
  document.getElementById("form-action-title").textContent = "EDIT CONTACT";
  document.getElementById("edit-original-name").value = name;
  document.getElementById("contact-name").value = name;
  document.getElementById("contact-phone").value = phone;
  document.getElementById("form-cancel-btn").textContent = "CANCEL";
  
  // Smooth scroll form into view or focus name input
  const nameInput = document.getElementById("contact-name");
  if (nameInput) nameInput.focus();
}

function clearContactForm() {
  document.getElementById("form-action-title").textContent = "ADD NEW CONTACT";
  document.getElementById("edit-original-name").value = "";
  document.getElementById("contact-form").reset();
  document.getElementById("form-cancel-btn").textContent = "CLEAR";
  hideStatus();
}

async function saveContactEvent(event) {
  if (event) event.preventDefault();
  
  const nameInput = document.getElementById("contact-name");
  const phoneInput = document.getElementById("contact-phone");
  const origNameInput = document.getElementById("edit-original-name");
  
  const name = nameInput.value.trim();
  const phone = phoneInput.value.trim();
  const originalName = origNameInput.value.trim();
  
  if (!name || !phone) {
    showStatus("NAME AND PHONE ARE REQUIRED", "error");
    return;
  }
  
  showStatus("SAVING...", "success");
  
  try {
    // If editing and changed the name, delete the old contact name entry first
    if (originalName && originalName.toLowerCase() !== name.toLowerCase()) {
      await eel.delete_contact(originalName)();
    }
    
    const response = await eel.save_contact(name, phone)();
    if (response.success) {
      allContacts = response.contacts;
      renderContacts(allContacts);
      clearContactForm();
      showStatus("CONTACT SAVED SUCCESSFULLY", "success");
      setTimeout(hideStatus, 3000);
    } else {
      showStatus(response.error.toUpperCase() || "SAVE FAILED", "error");
    }
  } catch (error) {
    console.error("Error saving contact:", error);
    showStatus("SAVE FAILED (CONNECTION ERROR)", "error");
  }
}

async function deleteContact(name) {
  if (!confirm(`ARE YOU SURE YOU WANT TO DELETE "${name.toUpperCase()}"?`)) {
    return;
  }
  
  showStatus("DELETING...", "success");
  
  try {
    const response = await eel.delete_contact(name)();
    if (response.success) {
      allContacts = response.contacts;
      renderContacts(allContacts);
      
      // If we were editing this contact, clear form
      const origName = document.getElementById("edit-original-name").value.trim();
      if (origName.toLowerCase() === name.toLowerCase()) {
        clearContactForm();
      }
      
      showStatus("CONTACT DELETED SUCCESSFULLY", "success");
      setTimeout(hideStatus, 3000);
    } else {
      showStatus(response.error.toUpperCase() || "DELETE FAILED", "error");
    }
  } catch (error) {
    console.error("Error deleting contact:", error);
    showStatus("DELETE FAILED (CONNECTION ERROR)", "error");
  }
}

function showStatus(msg, type) {
  const el = document.getElementById("contacts-status");
  if (el) {
    el.textContent = msg;
    el.className = `contacts-status-msg ${type}`;
  }
}

function hideStatus() {
  const el = document.getElementById("contacts-status");
  if (el) {
    el.textContent = "";
    el.className = "contacts-status-msg";
  }
}

function escapeHtml(str) {
  if (!str) return "";
  return str.toString()
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function escapeJsString(str) {
  if (!str) return "";
  return str.toString()
    .replace(/\\/g, "\\\\")
    .replace(/'/g, "\\'")
    .replace(/"/g, '\\"');
}