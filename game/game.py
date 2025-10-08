import json
import random
import time

# ==============================
# Character Class
# ==============================
class Character:
    def __init__(self, name, hp, moves):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.moves = moves  # dict
        self.cooldowns = {m: 0 for m in moves.keys()}

    def info(self):
        print(f"\n🧠 {self.name} — HP: {self.hp}/{self.max_hp}")
        print("Available Moves:")
        for idx, (name, move) in enumerate(self.moves.items(), start=1):
            cd = f"(CD:{self.cooldowns[name]} turn(s) left)" if self.cooldowns[name] > 0 else ""
            print(f" {idx}. {name}: {move['desc']} {cd}")

    def reduce_cooldowns(self):
        for k in self.cooldowns.keys():
            if self.cooldowns[k] > 0:
                self.cooldowns[k] -= 1

    def use_move(self, move_name, target):
        move = self.moves[move_name]

        # Cooldown check
        if self.cooldowns[move_name] > 0:
            print(f"⚠️ {move_name} is on cooldown for {self.cooldowns[move_name]} more turns!")
            return

        # Accuracy check
        if random.randint(1, 100) > move["accuracy"]:
            print(f"💨 {self.name}'s {move_name} missed!")
        else:
            dmg = move["damage"]
            heal = move["heal"]

            if dmg > 0:
                target.hp = max(target.hp - dmg, 0)
                print(f"🔥 {self.name} used {move_name} and dealt {dmg} damage to {target.name}!")
            if heal > 0:
                self.hp = min(self.hp + heal, self.max_hp)
                print(f"💚 {self.name} healed {heal} HP using {move_name}!")

        # Apply cooldown
        if move["cooldown"] > 0:
            self.cooldowns[move_name] = move["cooldown"]

    def is_alive(self):
        return self.hp > 0

# ==============================
# Utility Functions
# ==============================
def load_character(file_path):
    with open(file_path, "r") as f:
        char_data = json.load(f)
    return Character(char_data["Name"], char_data["HP"], char_data["Moves"])

# ==============================
# Battle Logic
# ==============================
def battle(player, enemy):
    print(f"\n⚔️ Battle Start! {player.name} vs {enemy.name}\n")
    turn = 1
    phase_shift_active = False

    while player.is_alive() and enemy.is_alive():
        print(f"\n====== Turn {turn} ======")
        print(f"{player.name}: {player.hp}/{player.max_hp} HP | {enemy.name}: {enemy.hp}/{enemy.max_hp} HP")

        player.reduce_cooldowns()
        enemy.reduce_cooldowns()

        # Player move
        player.info()
        try:
            choice = int(input("\nChoose your move (number): "))
            move_names = list(player.moves.keys())
            if 1 <= choice <= len(move_names):
                move_name = move_names[choice - 1]
            else:
                print("Invalid choice! Skipping turn.")
                move_name = None
        except ValueError:
            print("Invalid input! Skipping turn.")
            move_name = None

        if move_name:
            player.use_move(move_name, enemy)

        if not enemy.is_alive():
            print(f"\n🏆 {enemy.name} was defeated! You win!")
            break

        # Enemy turn (AI)
        time.sleep(1)
        move_names = [m for m in enemy.moves.keys() if enemy.cooldowns[m] == 0]
        if not move_names:
            move_names = list(enemy.moves.keys())
        move_name = random.choice(move_names)

        print(f"\n🤖 {enemy.name} is preparing {move_name}...")

        if move_name == "PHASE_SHIFT":
            phase_shift_active = True
            print(f"✨ {enemy.name} activated PHASE_SHIFT and will dodge next attack!")
            enemy.cooldowns["PHASE_SHIFT"] = enemy.moves["PHASE_SHIFT"]["cooldown"]
        else:
            if phase_shift_active:
                print(f"⚡ {enemy.name} dodged your attack completely!")
                phase_shift_active = False
            else:
                enemy.use_move(move_name, player)

        if not player.is_alive():
            print(f"\n💀 {player.name} was defeated! Game Over.")
            break

        turn += 1
        time.sleep(1.5)

# ==============================
# Game Menu
# ==============================
def main():
    print("=== Welcome to the Turn-Based Battle Game ===\n")
    print("Choose your Hero:")
    print("1. Maria 🦇")
    print("2. A.V 🤖")

    choice = input("Enter your choice: ")
    if choice == "1":
        player = load_character("Maria.json")
    elif choice == "2":
        player = load_character("av.json")
    else:
        print("Invalid choice. Exiting game.")
        return

    enemy = load_character("shogun.json")
    battle(player, enemy)

# ==============================
# Run Game
# ==============================
if __name__ == "__main__":
    main()
