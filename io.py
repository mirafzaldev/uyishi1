from pathlib import Path

desktop = Path("/Users/HP/desktop")

empty = desktop / "empty" / "somsa.jpeg"
empty1 = desktop / "empty" / "somsa.mp3"
empty2 = desktop / "empty" / "somsa.mp4"
empty3 = desktop / "empty" / "somsa.py"

full = desktop / "full" / "somsa.jpeg"
full1 = desktop / "full" / "somsa.mp3"
full2 = desktop / "full" / "somsa.mp4"
full3 = desktop / "full" / "somsa.py" 


full.replace(empty)
full1.replace(empty1)
full2.replace(empty2)
full3.replace(empty3)
