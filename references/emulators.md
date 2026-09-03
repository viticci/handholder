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

Read [retroarch.md](retroarch.md) before changing RetroArch controls, hotkeys, save states, shaders, or controller profiles. Keep BIOS handling and core selection in the approved task scope.

## 4:3 display baseline

- Use original/core-provided aspect ratio for 4:3 console libraries.
- Do not enable widescreen hacks globally.
- GameCube: start with official Dolphin defaults, 2x internal resolution, and renderer selected by game compatibility; 3x is a per-game upgrade when stable.
- PlayStation 2: start at 2x internal resolution, then test 3x per game. Use Vulkan or OpenGL according to the emulator and title.
- PSP: keep original 16:9 output with letterboxing unless the game offers a safe alternative.

## Dolphin per-game cheats

- Identify the disc's exact six-character game ID and region before selecting a code. Separate regional copies need separate `GameSettings/<GAMEID>.ini` files even when the title is the same.
- Keep cheats per game. Do not invert a controller axis globally to repair one title unless the user explicitly wants that behavior everywhere.
- Dolphin's `[ActionReplay]` section accepts decrypted `XXXXXXXX YYYYYYYY` lines and encrypted `XXXX-XXXX-XXXXX` blocks. Put the identical `$Code Name` under `[ActionReplay_Enabled]`, and confirm the global Dolphin configuration has cheats enabled.
- Back up any existing per-game file before replacement. Merge unrelated settings instead of overwriting them.
- Prove activation as well as behavior. A short temporary `Logger.ini` with file logging, verbosity `4`, and `ActionReplay = True` can show the code name, decoded address, and written value. Restore the previous logger immediately after the test so per-frame cheat logging cannot fill storage or hurt performance. Finish with the requested stick movement in live gameplay.

## Test standard

For each configured emulator family, prove:

1. The app sees the intended ROM root.
2. A representative title boots past logos into interactive gameplay.
3. Built-in controls and audio work.
4. Aspect ratio and orientation are correct.
5. A native save can be created or loaded.
6. Exit returns to Cocoon and relaunch works.
