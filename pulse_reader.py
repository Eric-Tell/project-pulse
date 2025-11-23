from rich import print

lines = open("pulse.txt").read().splitlines()
print(f"[cyan]commits:[/cyan] {lines[0]}")
print(f"[cyan]Timesstamp:[/cyan] {lines[1]}")
print(f"[cyan]Files Tracked:[/cyan] {lines[2]}")