# ✈️ Blockbusters: Aeronautics

> Take to the skies. Build flying machines. Explore a world from above.

**Blockbusters: Aeronautics** is a NeoForge 1.21.1 modpack built around [Create: Aeronautics](https://modrinth.com/mod/create-aeronautics) — the art of building real, physics-driven airships. Pair that with deep exploration, atmospheric dungeons, and stunning visuals, and you've got a series worth watching.

---

## 📦 Installation

1. Download and install the [Modrinth App](https://modrinth.com/app)
2. Find the modpack at [modrinth.com/modpack/blockbusters-aeronautics](https://modrinth.com/modpack/blockbusters-aeronautics), by searching for it in the Modrinth App, or by downloading the latest release directly from the [Releases](../../releases/latest) page (`*-client.mrpack`)
3. Once the pack is installed, navigate to the instance in the Modrinth App and click **Play**

---

## 🖥️ Server Setup

Download the latest server pack from the [Releases](../../releases/latest) page (`*-server.mrpack`).

### Docker (recommended)

1. Copy the `.mrpack` file to your server directory
2. Create a `docker-compose.yml`:

```yaml
services:
  minecraft:
    image: itzg/minecraft-server:java21
    container_name: minecraft-server
    environment:
      EULA: "TRUE"
      TYPE: "MODRINTH"
      MODRINTH_MODPACK: "/modpack/blockbusters-aeronautics-X.X.X-server.mrpack"
      MEMORY: "10G"
    volumes:
      - ./server:/data
      - ./modpack:/modpack:ro
    ports:
      - "25565:25565"
    restart: unless-stopped
```

3. Run `docker compose up -d`

### Manual

1. Download [NeoForge 1.21.1](https://neoforged.net/) and install it
2. Extract the `-server.mrpack` (it's a ZIP) and copy the `mods/` folder to your server directory
3. Copy the `overrides/` folder contents to your server directory
4. Start the server with at least 8GB RAM

### Server Info

- **Version:** 1.21.1 NeoForge
- **Slots:** 10 players
- **Difficulty:** Normal

---

## ⚙️ Recommended Settings

For the best experience:

| Setting | Recommended |
|---|---|
| RAM allocated | 6–8 GB |
| Java version | Java 21 |
| View distance (client) | 12–16 |

**JVM Arguments** (paste into Modrinth launcher settings):
```
-Xms4G -Xmx8G -XX:+UseZGC -XX:+ZGenerational -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:ConcGCThreads=3
```

> **Note:** This pack includes Distant Horizons, which recommends ZGC for smoother rendering. ZGC runs garbage collection concurrently so you won't get stutters. Requires Java 21 (which the Modrinth launcher uses by default).

---

## 🐛 Troubleshooting

**Crash on launch:**
- Make sure you're using Java 21 (not Java 8 or 17)
- Try allocating more RAM (minimum 4GB)

**Low FPS / lag:**
- Lower your render distance
- Turn off shaders temporarily to check if they're the cause
- Make sure no other heavy programs are running

**Can't connect to server:**
- Confirm modpack version matches the server version (check [Releases](../../releases))
- Make sure you launched via the Modrinth App (not vanilla launcher)

---

## 📋 Changelog

See [CHANGELOG.md](CHANGELOG.md) for full version history.

---

## 📝 Contributing / Reporting Issues

Found a bug or want to suggest a mod? Open an [Issue](../../issues)!
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
