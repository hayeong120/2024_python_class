# 셋 생성
game = {"LOL", "Overwatch", "Tetris", 1942, 2048}
print(game)
print(set("Funny"))
print(set([2048, "Tetris", "Cube"]))
print(set((2560, 1440)))
print(set({"google":"google.com", 18:"unesco.org"}))
print(set(range(3)))

# 셋에 추가
game.add("Fifa")
print(game)
game.update(("NBA", "MLB"))
print(game)

# 셋에서 제거
game.remove("LOL")
print(game)