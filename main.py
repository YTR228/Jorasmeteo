import threading
from collector import run_collector
from bot import run_bot

threading.Thread(target=run_collector, daemon=True).start()
run_bot()
