{{ config(materialized='view') }}

-- Select player 
WITH player as (SELECT 'Rafael Nadal' as player)


-- Select tournament, total hours played, match wins and tournament wins
SELECT tourney_name tournament, 
       COUNT(DISTINCT "round") Rounds,
       ROUND(CAST(SUM(minutes) / 60 AS NUMERIC), 1) duration_hours, 
       COUNT(DISTINCT tourney_date) times_entered,
       COUNT(*) matches_played,
       COUNT(*) FILTER (WHERE winner_name = player) as wins,
       CAST(COUNT(*) FILTER (WHERE loser_name != player) as REAL) / CAST(COUNT(*) as REAL) as win_pct,
       ROUND(AVG(sets_played), 2) avg_sets
       
  FROM player CROSS JOIN matches

 WHERE (winner_name = player OR loser_name = player) AND minutes IS NOT NULL

 GROUP BY tourney_name

 ORDER BY win_pct DESC