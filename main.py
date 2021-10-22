import wrap, random

shirena = 500
vysota = 500
x1 = random.randint(50, 150)
y1 = random.randint(50, 466)
x2 = random.randint(150, 300)
y2 = random.randint(50, 466)
x3 = random.randint(300, 450)
y3 = random.randint(50, 466)

wrap.world.create_world(shirena, vysota, 200, 200)
wrap.world.set_back_color(255, 255, 255)

# еда1
wrap.sprite.add_text("1apple", x1, y1 + 34, True, "Comic Sans")
wrap.sprite.add("pacman", x1, y1, "item_apple")
# еда2
wrap.sprite.add_text("2apple", x2, y2 + 34, True, "Comic Sans")
wrap.sprite.add("pacman", x2, y2, "item_apple")
# еда3
wrap.sprite.add_text("3apple", x3, y3 + 34, True, "Comic Sans")
wrap.sprite.add("pacman", x3, y3, "item_apple")

#создаём пакмена
pacman=wrap.sprite.add("pacman", shirena/2, vysota/2, "player2")
wrap.sprite.set_size(pacman,50,50)
