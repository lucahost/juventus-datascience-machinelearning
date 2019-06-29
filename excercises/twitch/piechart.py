import matplotlib.pyplot as plt

labels = ["US", "DE", "CA", "N/A", "GB", "TR",
          "BR", "DK", "PL", "BE", "NL", "Others"]
countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]
colors = {'lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna',
          'khaki', 'gold', 'violet', 'yellowgreen'}
# Make your pie chart here
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
plt.pie(countries, explode=explode, colors=colors, shadow=True,
        startangle=345, autopct='%1.0f%%', pctdistance=1.15)
plt.title("League of Legends Viewers' Whereabouts")
plt.legend(labels, loc="right")
plt.show()
