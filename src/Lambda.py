def lambda_handler(event, context):
    mobs = {
        "passive": ["Chicken", "Cow", "Horse", "Ocelot", "Pig", "Sheep",
                    "Bat", "Mushroom", "Squid", "Villager"],
        "neutral": ["Cave Spider", "Enderman", "Spider", "Wolf",
                    "Zombie Pigman"],
        "hostile": ["Blaze", "Creep", "Endermite", "Ghast", "Magma Cube",
                    "Silverfish", "Skeleton", "Slime", "Spider Jockey",
                    "Witch", "Whither Skeleton", "Zombie",
                    "Zombie Villager", "Chicken Jockey", "Killer Bunny",
                    "Guardian", "Elder Guardian"],
        "utility": ["Snow Golem", "Iron Golem"],
        "boss": ["Whither", "Ender Dragon"]
    }

    return {"mob_type": mobs[event['mob_type']]}
