from profiles import PROFILES

def apply_profile(config):
    profile = config.get("profile")

    if not profile:
        return config

    values = PROFILES.get(profile)

    if values is None:
        available = ", ".join(sorted(PROFILES.keys()))
        raise ValueError(
            f"Unknown profile '{profile}'. "
            f"Available profiles: {available}"
        )

    for key, value in values.items():
        parts = key.split(".")
        target = config.data

        for part in parts[:-1]:
            target = target.setdefault(part, {})

        target[parts[-1]] = value

    return config
