
def get_pricing_list():
    pricing_agg = {
        "Itinerary": ["Itinerary Category"],
        "Ship": ["Ship"],
        "Port": ["Port"],
        "Room Type": ["Room Type"],
        "Room Classification": ["Room Classification"],

        "ship_by_room": ["Ship", "Room Type"],
        "ship_by_room_classification": ["Ship", "Room Classification"],
        "ship_by_month": ["Ship", "Month"],
        "ship_by_itinerary": ["Ship", "Itinerary Category"],
        "ship_by_room_ports": ["Ship", "Room Type", "Number of Ports"],

        "ship_by_month_itinerary": ["Ship", "Month", "Itinerary Category"],
        "ship_by_month_room": ["Ship", "Month", "Room Type"],
        "ship_by_month_room_classification": ["Ship", "Month", "Room Classification"],
        "ship_by_month_floor_room": ["Ship", "Month", "Floor", "Room Type"],

        "class_by_room_classification": ['Ship Class', "Room Classification"],
        "class_by_room_type": ['Ship', 'Room Type'],

        "floor_by_room": ["Floor", "Room Type"],
        "floor_by_room_classification": ["Floor", "Room Classification"],

        "month_by_room_type": ["Month", "Room Type"],
        "month_by_room_Classification": ["Month", "Room Classification"],
        "month_by_floor": ["Month", "Floor"],
        "month_by_port": ["Month", "Port"],
        "month_by_room_num_ports": ['Month', 'Room Type', 'Number of Ports'],

        "itinerary_by_ship_room_type": ["Itinerary Category", "Ship", "Room Type"],
        "itinerary_by_ship_room_classification": ["Itinerary Category", "Ship", "Room Classification"],
        "itinerary_by_port": ["Itinerary Category", "Port"],
        "itinerary_by_month": ["Itinerary Category", "Month"],
        "itinerary_by_room_type": ["Itinerary Category", "Room Type"],
        "itinerary_by_room_classification": ["Itinerary Category", "Room Classification"],

        "room_type_by_port_floor_itinerary": ["Room Type", "Port", "Floor", "Itinerary Category"],
        "room_type_by_itinerary_by_day": ["Room Type", "Itinerary Category", "Days"],
        "room_type_by_itinerary_by_month": ["Room Type", "Itinerary Category", "Month"],

        "port_ship_room": ["Port", "Ship", "Room Type"],
        "port_ship_month": ["Port", "Ship", "Month"],
        "port_ship_room_month": ["Port",  "Ship", "Room Type", "Month"],

        "ship_class_rank": ['Ship Class Rank'],
        "ship_class_rank_port": ['Ship Class Rank', 'Port'],
        "ship_class_room": ['Ship Class Rank', 'Room Type'],
        "ship_Class_room_day": ['Ship Class Rank', 'Room Type', 'Days'],

        "ship_size": ['Size Category'],
        "ship_size_port": ['Size Category', 'Port'],
        "ship_size_room": ['Size Category', 'Room Type'],
        "ship_size_room_day": ['Size Category', 'Room Type', 'Days'],

        "age_bucket_by_room_type": ["Age Bucket", "Room Type"],
        "age_bucket_by_room_classification": ["Age Bucket", "Room Classification"],
        "age_bucket_by_port": ["Age Bucket", "Port"],
        "age_bucket_by_month": ["Age Bucket", "Month"],
        "age_bucket_by_room_type_days": ["Age Bucket", "Room Type", "Days"],
        "age_bucket_by_month_floor_room": ["Age Bucket", "Month", "Floor", "Room Type"],

        "age_bucket_by_port_room_type": ["Age Bucket", "Port", "Room Type"],
        "age_bucket_by_port_room_classification": ["Age Bucket", "Port", "Room Classification"],
        "age_bucket_by_port_month": ["Age Bucket", "Port", "Month"],
        "age_bucket_by_port_room_type_days": ["Age Bucket", "Port", "Room Type", "Days"],
        "age_bucket_by_port_month_floor_room": ["Age Bucket", "Port", "Month", "Floor", "Room Type"],

        "age_bucket_by_port_size_room_type": ["Age Bucket", "Port", "Size Category", "Room Type"],
        "age_bucket_by_port_size_room_classification": ["Age Bucket", "Port", "Size Category", "Room Classification"],
        "age_bucket_by_port_size": ["Age Bucket", "Port", "Size Category"],
        "age_bucket_by_port_size_month": ["Age Bucket", "Port", "Size Category", "Month"],
        "age_bucket_by_port_size_room_type_days": ["Age Bucket", "Port", "Size Category", "Room Type", "Days"],
        "age_bucket_by_port_size_month_floor_room": ["Age Bucket", "Port", "Size Category", "Month", "Floor", "Room Type"],

        "age_bucket_by_size_room_type": ["Age Bucket", "Size Category", "Room Type"],
        "age_bucket_by_size_room_classification": ["Age Bucket", "Size Category", "Room Classification"],
        "age_bucket_by_size": ["Age Bucket", "Size Category"],
        "age_bucket_by_size_month": ["Age Bucket", "Size Category", "Month"],
        "age_bucket_by_size_room_type_days": ["Age Bucket", "Size Category", "Room Type", "Days"],
        "age_bucket_by_size_month_floor_room": ["Age Bucket", "Size Category", "Month", "Floor", "Room Type"]
    }
    return pricing_agg