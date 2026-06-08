import time
import requests
import eel

# Global variable to cache network metrics
cached_network_data = {
    "status": "Checking...",
    "ping": "...",
    "download": "...",
    "upload": "..."
}

def network_status_loop():
    global cached_network_data
    
    last_speed_check = 0
    download_speed = "Testing..."
    upload_speed = "Testing..."
    
    while True:
        try:
            start = time.time()
            res = requests.get("https://speed.cloudflare.com/__down?bytes=0", timeout=3)
            ping = f"{round((time.time() - start) * 1000)} ms"
            online = "Connected"
        except Exception:
            ping = "N/A"
            online = "Disconnected"
            
        now = time.time()
        if online == "Connected" and (now - last_speed_check >= 30 or last_speed_check == 0):
            try:
                # Fast download check (300 KB)
                dl_start = time.time()
                dl_res = requests.get("https://speed.cloudflare.com/__down?bytes=300000", timeout=5)
                dl_duration = time.time() - dl_start
                download_speed = f"{round(((len(dl_res.content) * 8) / dl_duration) / 1000000, 1)} Mbps"
                
                # Fast upload check (150 KB)
                ul_data = b"0" * 150000
                ul_start = time.time()
                requests.post("https://speed.cloudflare.com/__up", data=ul_data, timeout=5)
                ul_duration = time.time() - ul_start
                upload_speed = f"{round(((len(ul_data) * 8) / ul_duration) / 1000000, 1)} Mbps"
                
                last_speed_check = now
            except Exception as e:
                print("Speed test error:", e)
                download_speed = "Error"
                upload_speed = "Error"
                
        cached_network_data = {
            "status": online,
            "ping": ping,
            "download": download_speed if online == "Connected" else "N/A",
            "upload": upload_speed if online == "Connected" else "N/A"
        }
        
        try:
            # Push updates dynamically to the frontend
            eel.updateNetwork(cached_network_data)
        except Exception:
            pass
            
        time.sleep(5)

def start_network_monitoring():
    import threading
    threading.Thread(target=network_status_loop, daemon=True).start()

def get_cached_status():
    global cached_network_data
    return cached_network_data
