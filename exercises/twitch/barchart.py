import matplotlib.pyplot as plt

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS",
         "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]
viewers = [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]
plt.bar(range(len(games)), viewers, color='slateblue')
plt.legend(["Twitch"])
plt.xlabel('Games')
plt.ylabel('Viewers')
ax = plt.subplot()
ax.set_xticks(range(0, 10))
ax.set_xticklabels(games, rotation=30)
plt.show()
