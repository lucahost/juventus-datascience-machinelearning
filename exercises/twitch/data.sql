-- Task 1
SELECT column
FROM table_name LIMIT
20;

-- Task 2
SELECT DISTINCT column
FROM table_name;

-- Task 3
SELECT game, COUNT(*)
FROM stream
GROUP BY game
ORDER BY COUNT(*) DESC;

-- Task 4
SELECT game, COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 2 DESC;

-- Task 5
SELECT country, COUNT(*)
FROM stream
WHERE game = 'League of Legends'
GROUP BY 1
ORDER BY 2 DESC;

-- Task 6
SELECT player, COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 2 DESC;

-- Task 7
SELECT game,
  CASE
  WHEN game = 'Dota 2'
      THEN 'MOBA'
  WHEN game = 'League of Legends'
      THEN 'MOBA'
  WHEN game = 'Heroes of the Storm'
      THEN 'MOBA'
    WHEN game = 'Counter-Strike: Global Offensive'
      THEN 'FPS'
    WHEN game = 'DayZ'
      THEN 'Survival'
    WHEN game = 'ARK: Survival Evolved'
      THEN 'Survival'
  ELSE 'Other'
  END AS 'genre',
  COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 3 DESC;

-- Task 8
SELECT time
FROM stream
LIMIT
10;

-- Task 9
SELECT time,
  strftime('%S', time)
FROM stream
GROUP BY 1
LIMIT 20;


-- Task 10
SELECT strftime('%H', time),
  COUNT(*)
FROM stream
WHERE country = 'US'
GROUP BY 1;


-- Task 11
SELECT *
FROM stream
  JOIN chat
  ON stream.device_id = chat.device_id;
