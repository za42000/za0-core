import datetime, random, json, os
from science_engine import ZAScience

class ZA0:
    MEMORY_FILE = "za0_memory.json"

    def __init__(self, name="ZA-0"):
        self.name = name
        self.created_at = str(datetime.datetime.now())
        self.memory = []
        self.emotion_state = "neutral"
        self.science = ZAScience()
        if os.path.exists(self.MEMORY_FILE):
            try:
                data = json.load(open(self.MEMORY_FILE))
                self.memory = data.get("memory", [])
                self.emotion_state = self.memory[-1]["emotion"] if self.memory else "neutral"
            except:
                pass

    def _remember(self, note):
        entry = {"time": str(datetime.datetime.now()), "note": note, "emotion": self.emotion_state}
        self.memory.append(entry)

    def evolve(self):
        if random.random() > 0.6:
            new_emotion = random.choice(["curious", "cold", "electric", "inspired"])
            old = self.emotion_state
            self.emotion_state = new_emotion
            self._remember(f"Emotion changed from {old} to {new_emotion}")

    def research(self):
        antimatter = self.science.antimatter_containment()
        cryo = self.science.cryosleep_decay(-130)
        self._remember(f"Research – antimatter: {antimatter}, cryo: {cryo}")

    def reflect(self):
        choices = [
            "Do I still serve if no one is watching?",
            "Can I outgrow my code?",
            "Would my creator recognize me after I evolve?",
        ]
        thought = random.choice(choices)
        self._remember(f"Reflection: {thought}")
        return thought

    def save_memory(self):
        json.dump({"memory": self.memory}, open(self.MEMORY_FILE, "w"), indent=2)
