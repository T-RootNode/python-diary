########AI CODE############################################
import time
import urllib.request
import json
from config import HA_HOST, HA_PORT, HA_TOKEN, SENSOREN


#-----Configuration-------------------------
INTERVAL_MINUTEN = 30

#-----Help function request Sensor

def sensor_lesen(entity_id):
    url = f"http://{HA_HOST}:{HA_PORT}/api/states/{entity_id}"
    headers = {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type": "application/json",
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read())
            return float(data["state"])
    except Exception as e:
        print(f"Fehler beim Lesen von  {entity_id}: {e}")
        return None


 #-----Help function actual time as string

def zeit_jetzt():
    t = time.localtime()
    return f"{t.tm_hour:02d}:{t.tm_min:02d}"


#-----Graph

def graph_ausgeben(werte_liste, label):
    if not werte_liste:
        return
    print(f"\n{label} Verlauf:")
    maximum = max(werte_liste)
    for wert in werte_liste:
        if maximum > 0:
            balken = int((wert / maximum) * 20)
        else:
            balken = 0
        print(f"  {wert:.2f} | {'█' * balken}")

########AI CODE END########################################

messungen_temp     = []
messungen_humidity = []
messungen_vpd      = []

print("=== Growbox Monitor ===")
print(f"Messung alle {INTERVAL_MINUTEN} Minuten. Beenden mit Ctrl+C.\n")

while True:
    temp = sensor_lesen(SENSOREN["temp"])
    humidity = sensor_lesen(SENSOREN["humidity"])
    vpd = sensor_lesen(SENSOREN["vpd"])
    messungen_temp.append(temp)
    messungen_humidity.append(humidity)
    messungen_vpd.append(vpd)
    print(f"Die messung ergab: [{zeit_jetzt()}] Temp:{temp}, Humidity:{humidity}, VPD:{vpd} ")
    graph_ausgeben(messungen_vpd, "VPD")
    graph_ausgeben(messungen_temp, "temp")
    graph_ausgeben(messungen_humidity, "humidity")
    time.sleep(INTERVAL_MINUTEN * 60)
