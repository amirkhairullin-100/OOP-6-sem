from abc import ABC, abstractmethod

class Hero(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass

    @abstractmethod
    def attack(self, weapon) -> str:
        pass

class Enemy(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass

    @abstractmethod
    def health(self) -> int:
        pass

class Weapon(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def damage(self) -> int:
        pass

class FantasyHero(Hero):
    def describe(self) -> str:
        return "Рыцарь, защищающий королевство"

    def attack(self, weapon) -> str:
        return f"Рыцарь атакует врага с помощью {weapon.name()}, нанося {weapon.damage()} урона"

class FantasyEnemy(Enemy):
    def describe(self) -> str:
        return "Дракон, охраняющий сокровища"

    def health(self) -> int:
        return 300

class FantasyWeapon(Weapon):
    def name(self) -> str:
        return "Меч"

    def damage(self) -> int:
        return 50

class SciFiHero(Hero):
    def describe(self) -> str:
        return "Космодесантник с тяжелым вооружением"

    def attack(self, weapon) -> str:
        return f"Космодесантник стреляет из {weapon.name()}, нанося {weapon.damage()} урона"

class SciFiEnemy(Enemy):
    def describe(self) -> str:
        return "Робот-суперагент"

    def health(self) -> int:
        return 200

class SciFiWeapon(Weapon):
    def name(self) -> str:
        return "Лазерный пистолет"

    def damage(self) -> int:
        return 70

class WorldFactory(ABC):
    @abstractmethod
    def create_hero(self) -> Hero:
        pass

    @abstractmethod
    def create_enemy(self) -> Enemy:
        pass

    @abstractmethod
    def create_weapon(self) -> Weapon:
        pass

class FantasyWorldFactory(WorldFactory):
    def create_hero(self) -> Hero:
        return FantasyHero()

    def create_enemy(self) -> Enemy:
        return FantasyEnemy()

    def create_weapon(self) -> Weapon:
        return FantasyWeapon()

class SciFiWorldFactory(WorldFactory):
    def create_hero(self) -> Hero:
        return SciFiHero()

    def create_enemy(self) -> Enemy:
        return SciFiEnemy()

    def create_weapon(self) -> Weapon:
        return SciFiWeapon()

def create_world(factory: WorldFactory):
    hero = factory.create_hero()
    enemy = factory.create_enemy()
    weapon = factory.create_weapon()

    print(f"Герой: {hero.describe()}")
    print(f"Враг: {enemy.describe()} (здоровье: {enemy.health()})")
    print(hero.attack(weapon))

if __name__ == "__main__":
    print("=== Fantasy Мировой сценарию ===")
    create_world(FantasyWorldFactory())

    print("\n=== SciFi Мировой сценарию ===")
    create_world(SciFiWorldFactory())