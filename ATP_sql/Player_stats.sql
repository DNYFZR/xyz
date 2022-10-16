-- Set output Jinja
{{ config(materialized='view') }}

WITH unique_names as (
    SELECT DISTINCT winner_name players
      FROM matches

    UNION

    SELECT DISTINCT loser_name
      FROM matches
)


-- Query
SELECT DISTINCT players
  FROM unique_names