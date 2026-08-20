# Emulator selection and configuration

Use this reference to choose the smallest maintained emulator set for the requested library. Verify current releases and Cocoon support before installation.

## Common package identities

These package IDs are discovery anchors, not guaranteed current values.

| Component | Common package ID |
|---|---|
| Cocoon | `rip.moth.cocoonshell` |
| RetroArch | `com.retroarch.aarch64` or store-specific variant |
| DuckStation | `com.github.stenzek.duckstation` |
| Dolphin | `org.dolphinemu.dolphinemu` |
| PPSSPP | `org.ppsspp.ppsspp` |
| ARMSX2 | `com.armsx2` |
| Azahar | `org.azahar_emu.azahar` |
| melonDS | `me.magnum.melonds` |
| GameNative | `app.gamenative` |

## Practical platform map

| Platform | Preferred starting point | Notes |
|---|---|---|
| Game Boy / Game Boy Color | RetroArch Gambatte | Use core overrides for handheld shaders or palettes. |
| Game Boy Advance | RetroArch mGBA | Apply color correction only when desired. |
| SNES | RetroArch Snes9x | Prefer current Snes9x unless accuracy requirements justify a heavier core. |
| PlayStation | DuckStation, RetroArch PCSX-ReARMed, or SwanStation | Choose by device performance and BIOS availability; test Cocoon intent and playlist launching. |
| Nintendo 64 | RetroArch Mupen64Plus-Next or a maintained standalone app | Use per-game overrides; renderer compatibility varies. |
| Dreamcast | RetroArch Flycast or maintained standalone Flycast | BIOS paths differ from ordinary RetroArch system files. |
| PSP | PPSSPP | Native widescreen content will letterbox on 4:3 displays. |
| GameCube / Wii | official Dolphin | Add only the requested platform folders. |
| PlayStation 2 | current official or well-understood maintained ARM64 emulator | BIOS must come from the user's console; per-game settings are normal. |
| Nintendo DS | melonDS or a maintained device-specific variant | Screen layout is device-specific. |
| Nintendo 3DS | Azahar | Verify title IDs, screen layout, and storage provider behavior. |

Do not install an emulator for an excluded or absent platform merely because a guide recommends it.

For cue/bin libraries, confirm each `FILE` entry resolves before import. CHD is a useful lossless copy format when the selected core supports it. Multi-disc titles still need one CHD per disc plus a playlist or frontend grouping; compression alone does not merge discs.

DuckStation requires a user-dumped PlayStation BIOS to play games. Its onboarding can still be completed without one so the ROM directory, renderer, controller, and frontend player mapping can be prepared. Do not mistake successful library scanning for a playable BIOS configuration.

## RetroArch baseline

- Use Vulkan when the selected cores and shaders support it; use GL per-core where Vulkan is incompatible.
- Update core information and the selected shader package before configuring presets.
- Set a BIOS/system directory explicitly and verify that required files are detected.
- Reserve the built-in gamepad for player 1 when Android exposes other controller-like devices. ADB `input keyevent` creates a `Virtual` input device that can take port 1 during automated testing. Discover the controller name live, set `input_player1_reserved_device` to that exact RetroArch name, set `input_player1_device_reservation_type` to `2` (reserved), restart RetroArch, and confirm its on-screen connection message says `port 1`.
- Configure hotkey enable, menu toggle, quit, save/load state, fast-forward, and rewind without shadowing normal game buttons.
- Save shaders and options at the intended game, content-directory, core, or global scope.
- Optional 120 Hz black-frame insertion reduces brightness and can show visible flicker. Enable it only at the user's request and test comfort; never make it a silent default.

## 4:3 display baseline

- Use original/core-provided aspect ratio for 4:3 console libraries.
- Do not enable widescreen hacks globally.
- GameCube: start with official Dolphin defaults, 2x internal resolution, and renderer selected by game compatibility; 3x is a per-game upgrade when stable.
- PlayStation 2: start at 2x internal resolution, then test 3x per game. Use Vulkan or OpenGL according to the emulator and title.
- PSP: keep original 16:9 output with letterboxing unless the game offers a safe alternative.

## Test standard

For each configured emulator family, prove:

1. The app sees the intended ROM root.
2. A representative title boots past logos into interactive gameplay.
3. Built-in controls and audio work.
4. Aspect ratio and orientation are correct.
5. A native save can be created or loaded.
6. Exit returns to Cocoon and relaunch works.
