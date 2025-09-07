import random

class Card:
    def __init__(self, name, damage=0, heal=0, accuracy=100, cooldown=0, aoe=False, steal=False, dodge=False):
        self.name = name
        self.damage = damage
        self.heal = heal
        self.accuracy = accuracy
        self.cooldown = cooldown
        self.aoe = aoe
        self.steal = steal
        self.dodge = dodge
        self.current_cd = 0

    def is_ready(self):
        return self.current_cd == 0

    def reset_cooldown(self):
        self.current_cd = self.cooldown

    def tick(self):
        if self.current_cd > 0:
            self.current_cd -= 1


class Character:
    def __init__(self, name, hp, deck):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.deck = deck
        self.dodge_next = False

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        if self.dodge_next:
            print(f"{self.name} dodged the attack!")
            self.dodge_next = False
            return
        self.hp -= amount
        print(f"{self.name} took {amount} damage! [HP: {self.hp}]")

    def heal_self(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"{self.name} healed {amount} HP. [HP: {self.hp}]")

    def tick_cooldowns(self):
        for card in self.deck:
            card.tick()

    def get_ready_cards(self):
        return [card for card in self.deck if card.is_ready()]

    def use_card(self, card, targets):
        if random.randint(1, 100) <= card.accuracy:
            if card.dodge:
                self.dodge_next = True
                print(f"{self.name} used {card.name} and is ready to dodge the next attack.")
            for target in targets:
                if card.damage > 0:
                    target.take_damage(card.damage)
                if card.heal > 0:
                    self.heal_self(card.heal)
                if card.steal:
                    stolen = min(target.hp, card.damage)
                    target.take_damage(stolen)
                    self.heal_self(stolen)
        else:
            print(f"{self.name}'s {card.name} missed!")
        card.reset_cooldown()


class Game:
    def __init__(self):
        # Initialize characters
        self.av = Character("A.V 🐯", 50, [
            Card("STAR_CANON", damage=20, accuracy=50, cooldown=4),
            Card("BLAST_EM", damage=10, accuracy=100, cooldown=0)
        ])
        self.maria = Character("MARIA 🦇", 65, [
            Card("BLOOD_BATH", heal=15, accuracy=50, cooldown=3),
            Card("CURSE", damage=5, accuracy=100, cooldown=0)
        ])
        self.yurei = Character("Yurei Shogun 🌀", 70, [
            Card("SPIRIT_DRAIN", damage=10, heal=10, accuracy=80, cooldown=2, steal=True),
            Card("CURSED_FLAME", damage=15, accuracy=60, cooldown=1, aoe=True),
            Card("PHASE_SHIFT", accuracy=100, cooldown=3, dodge=True)
        ])

        self.turn = 0
        self.max_turns = 15

    def play(self):
        while self.turn < self.max_turns and self.yurei.is_alive() and (self.av.is_alive() or self.maria.is_alive()):
            print(f"\n-- Turn {self.turn + 1} --")

            # Tick cooldowns
            self.av.tick_cooldowns()
            self.maria.tick_cooldowns()
            self.yurei.tick_cooldowns()

            # Player actions (AI or choose best available card)
            for player in [self.av, self.maria]:
                if player.is_alive():
                    ready_cards = player.get_ready_cards()
                    if ready_cards:
                        best_card = ready_cards[0]  # Simple logic
                        player.use_card(best_card, [self.yurei])

            # Enemy turn
            if self.yurei.is_alive():
                ready_cards = self.yurei.get_ready_cards()
                if ready_cards:
                    card = random.choice(ready_cards)
                    if card.aoe:
                        targets = [t for t in [self.av, self.maria] if t.is_alive()]
                    else:
                        targets = [random.choice([self.av, self.maria])]
                    self.yurei.use_card(card, targets)

            self.turn += 1

        # Game end
        if not self.yurei.is_alive():
            print("\n🎉 Players Win! Yurei Shogun defeated.")
        elif not self.av.is_alive() and not self.maria.is_alive():
            print("\n💀 Yurei Shogun Wins! All players defeated.")
        elif self.turn >= self.max_turns:
            print("\n⌛ Time's up!")
            if self.yurei.is_alive():
                print("💀 Yurei Shogun Wins by surviving 15 turns.")
            else:
                print("🎉 Players Win by defeating Yurei before time!")

