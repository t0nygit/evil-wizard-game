import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  
    
    def attack(self, opponent):
        # Random damage between 80% and 120% of attack power
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
    
    def heal(self):
        # Heal for 30 health but don't go over max health
        heal_amount = 30
        old_health = self.health
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        actual_heal = self.health - old_health
        print(f"{self.name} heals for {actual_heal} health! Current health: {self.health}/{self.max_health}")
    
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.rage_available = True
        self.block_next_attack = False
    
    def power_strike(self, opponent):
        if self.rage_available:
            # Double damage attack
            damage = random.randint(int(self.attack_power * 1.6), int(self.attack_power * 2.0))
            opponent.health -= damage
            print(f"{self.name} uses Power Strike on {opponent.name} for {damage} damage!")
            self.rage_available = False
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
        else:
            print("Power Strike is not available right now!")
    
    def defensive_stance(self):
        if not self.block_next_attack:
            self.block_next_attack = True
            print(f"{self.name} takes a defensive stance and will block the next attack!")
        else:
            print("You are already in defensive stance!")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.fireball_available = True
        self.shield_active = False
    
    def fireball(self, opponent):
        if self.fireball_available:
            # High damage magical attack
            damage = random.randint(45, 60)
            opponent.health -= damage
            print(f"{self.name} casts Fireball on {opponent.name} for {damage} damage!")
            self.fireball_available = False
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
        else:
            print("Fireball is not available right now!")
    
    def magic_shield(self):
        if not self.shield_active:
            self.shield_active = True
            print(f"{self.name} casts Magic Shield and will absorb the next attack!")
        else:
            print("Magic Shield is already active!")

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        self.quick_shot_available = True
        self.evade_next_attack = False
    
    def quick_shot(self, opponent):
        if self.quick_shot_available:
            # Double arrow attack
            damage1 = random.randint(20, 30)
            damage2 = random.randint(20, 30)
            total_damage = damage1 + damage2
            opponent.health -= total_damage
            print(f"{self.name} uses Quick Shot on {opponent.name}!")
            print(f"First arrow hits for {damage1} damage! Second arrow hits for {damage2} damage!")
            print(f"Total damage: {total_damage}")
            self.quick_shot_available = False
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
        else:
            print("Quick Shot is not available right now!")
    
    def evade(self):
        if not self.evade_next_attack:
            self.evade_next_attack = True
            print(f"{self.name} prepares to evade the next attack!")
        else:
            print("You are already prepared to evade!")

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20)
        self.holy_strike_available = True
        self.divine_shield_active = False
    
    def holy_strike(self, opponent):
        if self.holy_strike_available:
            # Bonus holy damage
            damage = random.randint(35, 50)
            opponent.health -= damage
            print(f"{self.name} uses Holy Strike on {opponent.name} for {damage} holy damage!")
            self.holy_strike_available = False
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
        else:
            print("Holy Strike is not available right now!")
    
    def divine_shield(self):
        if not self.divine_shield_active:
            self.divine_shield_active = True
            print(f"{self.name} activates Divine Shield and will block the next attack!")
        else:
            print("Divine Shield is already active!")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
    
    def regenerate(self):
        # Regenerate 5 health each turn
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
    
    def attack(self, opponent):
        # Check if opponent has any defensive abilities active
        damage_blocked = False
        
        # Check Warrior defensive stance
        if hasattr(opponent, 'block_next_attack') and opponent.block_next_attack:
            print(f"{opponent.name}'s defensive stance blocks the attack!")
            opponent.block_next_attack = False
            damage_blocked = True
        # Check Mage magic shield
        elif hasattr(opponent, 'shield_active') and opponent.shield_active:
            print(f"{opponent.name}'s Magic Shield absorbs the attack!")
            opponent.shield_active = False
            damage_blocked = True
        # Check Archer evade
        elif hasattr(opponent, 'evade_next_attack') and opponent.evade_next_attack:
            print(f"{opponent.name} evades the attack!")
            opponent.evade_next_attack = False
            damage_blocked = True
        # Check Paladin divine shield
        elif hasattr(opponent, 'divine_shield_active') and opponent.divine_shield_active:
            print(f"{opponent.name}'s Divine Shield blocks the attack!")
            opponent.divine_shield_active = False
            damage_blocked = True
        
        # If attack wasn't blocked, deal damage
        if not damage_blocked:
            damage = random.randint(12, 18)
            opponent.health -= damage
            print(f"{self.name} attacks {opponent.name} for {damage} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")
    
    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def use_special_ability(player, wizard):
    if isinstance(player, Warrior):
        print("1. Power Strike (double damage attack)")
        print("2. Defensive Stance (block next attack)")
        choice = input("Choose special ability: ")
        if choice == '1':
            player.power_strike(wizard)
        elif choice == '2':
            player.defensive_stance()
        else:
            print("Invalid choice!")
    
    elif isinstance(player, Mage):
        print("1. Fireball (high damage spell)")
        print("2. Magic Shield (absorb next attack)")
        choice = input("Choose special ability: ")
        if choice == '1':
            player.fireball(wizard)
        elif choice == '2':
            player.magic_shield()
        else:
            print("Invalid choice!")
    
    elif isinstance(player, Archer):
        print("1. Quick Shot (double arrow attack)")
        print("2. Evade (dodge next attack)")
        choice = input("Choose special ability: ")
        if choice == '1':
            player.quick_shot(wizard)
        elif choice == '2':
            player.evade()
        else:
            print("Invalid choice!")
    
    elif isinstance(player, Paladin):
        print("1. Holy Strike (bonus holy damage)")
        print("2. Divine Shield (block next attack)")
        choice = input("Choose special ability: ")
        if choice == '1':
            player.holy_strike(wizard)
        elif choice == '2':
            player.divine_shield()
        else:
            print("Invalid choice!")

def battle(player, wizard):
    print(f"\n=== BATTLE BEGINS ===")
    print(f"{player.name} vs {wizard.name}")
    print("=" * 30)
    
    while wizard.health > 0 and player.health > 0:
        print(f"\n--- {player.name}'s Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")
        
        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            use_special_ability(player, wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            wizard.display_stats()
            continue  # Don't end turn if just viewing stats
        else:
            print("Invalid choice. Try again.")
            continue  # Don't end turn for invalid choice
        
        # Check if wizard is defeated
        if wizard.health <= 0:
            break
        
        # Wizard's turn
        print(f"\n--- {wizard.name}'s Turn ---")
        wizard.regenerate()
        wizard.attack(player)
        
        # Check if player is defeated
        if player.health <= 0:
            break
    
    # Display final results
    print("\n" + "=" * 40)
    if wizard.health <= 0:
        print("🎉 VICTORY! 🎉")
        print(f"Congratulations! {player.name} has defeated {wizard.name}!")
        print("You have saved the kingdom from the evil wizard's dark magic!")
    else:
        print("💀 DEFEAT 💀")
        print(f"Oh no! {player.name} has been defeated by {wizard.name}!")
        print("The evil wizard's dark power was too strong...")
        print("Better luck next time, hero!")
    print("=" * 40)

def main():
    print("🧙‍♂️ Welcome to 'Defeat the Evil Wizard'! 🧙‍♂️")
    print("Choose your hero and battle the powerful Dark Wizard!")
    print()
    
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    
    print(f"\nYou have chosen {player.name} the {player.__class__.__name__}!")
    player.display_stats()
    print()
    
    battle(player, wizard)

if __name__ == "__main__":
    main()