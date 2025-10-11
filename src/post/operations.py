from enum import Enum

class Operation(Enum):
    READ =          "select (data) from flat where (data->>'device')::int = %s"
    GROUP =         "select (data->>'device')::int as device from flat group by device order by device asc"
    AVG =           "select avg((data->> 'volume_total_bytes')::int) as average from flat where (data->>'device')::int > 9390"
    INSERT =        "insert into flat (data) values %s"
    UPDATE =        "update flat set data = jsonb_set(data, '{volume_total_bytes}', %s, false) where (data->>'device')::int = %s"
