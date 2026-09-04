# RetroArch controls, states, and shaders

Use this reference when RetroArch is part of the setup. Treat its package, active configuration path, controller name, core, renderer, and override scope as live state.

## Discover before editing

1. Identify the installed RetroArch variant and version.
2. Open it once, then locate the active main configuration, append configuration, core and content overrides, controller autoconfiguration profile, save directory, state directory, shader directory, and system directory.
3. Record the physical controller name and mode exactly as RetroArch reports them. Android and ADB names may differ.
4. Back up only the files that will change. Do not assume a path from another Android device or RetroArch distribution.

## Keep the physical controller on port 1

Android can expose touch overlays, accessibility devices, external pads, or ADB-injected input as controllers. ADB input appears as a virtual device and can take port 1 during automated tests.

- Reserve the built-in controller for player 1 by its live RetroArch name when the installed build supports device reservation.
- Restart RetroArch after changing reservation or controller mode.
- Confirm the on-screen connection message identifies the physical controller on port 1.
- If the handheld has multiple controller modes, keep a tested autoconfiguration profile for each mode. Do not reuse raw Android key codes from another device.

## Configure one predictable hotkey layer

Use a dedicated enable button and chords that do not shadow ordinary gameplay. The useful minimum is:

- open or close the RetroArch menu;
- save state and load state;
- previous and next state slot;
- fast-forward and rewind;
- quit, with confirmation or a double press to prevent accidents.

Write bindings to the active main configuration. Mirror them in the matching physical-controller profile only when live testing proves that the installed frontend or controller mode needs it. Preserve separate profiles when the controller name changes.

Save states are tied to a core and often to a core version. Treat native in-game saves as the portable record of progress. The cheat sheet must say this plainly.

## Prove the hotkeys

Test with the physical controls in interactive gameplay, not only with ADB automation.

1. Open and close the menu.
2. Save a state and require the on-screen confirmation.
3. Move away from the saved scene, load it, and confirm the scene returns.
4. Change the state slot and require the on-screen slot message.
5. Test fast-forward, rewind when supported, and guarded quit.
6. Inspect the configured state directory and remove only a test state that did not exist before the test.

If gameplay input works but hotkeys fail in only one core, isolate the core and renderer before remapping the controller. Some Android core combinations have ignored frontend hotkeys while other cores worked with the same configuration. Check the current upstream issue tracker and build, compare a second maintained core, and record the core-specific limitation. Do not claim global hotkeys work until representative cores pass.

## Make a persistent cheat sheet

After testing, create a short user-facing note in an agreed host or device location. Include:

- each chord in plain language;
- the save-state compatibility warning;
- the active shader preset for each system family;
- any core-specific exception;
- the backup or rollback location.

Do not put secrets, device serials, ROM names, or private host paths in a public skill or repository.

## Use shader presets at a narrow scope

Check activation before replacing a preset that appears ineffective. `auto_shaders_enable` allows preset discovery, but `video_shader_enable = "false"` prevents shader rendering even when the correct `.slangp` file exists. Color correction is independent, so vivid colors do not prove that an LCD grid is active.

For a core-specific repair, merge `video_shader_enable = "true"` into `config/<CORE>/<CORE>.cfg` while keeping the existing directory presets and palette options. Use a narrower content-directory override when only one system using that core is in scope. Do not enable shaders globally merely to fix one platform.

Verify the running Quick Menu shows Video Shaders enabled and inspect an Android screen capture for the rendered effect. Then quit normally and relaunch from the frontend to prove the setting persists. An internal emulator screenshot may omit post-processing; prefer a capture of the displayed output for this check.

Update the selected shader package before choosing presets. Start at content-directory or core scope, test several games, and promote a preset to a broader scope only when the user wants consistent behavior.

- Monochrome and color handheld systems: start with a restrained LCD grid and a vivid but non-clipping palette. Avoid a washed-out global color-correction preset when the user wants a display-like color mode.
- Later color handheld systems: start with a light LCD grid or LCD3x-style preset. Keep small text and pixel edges clear.
- 16-bit home consoles: start with CRT Beam Simulator or a restrained CRT mask. Tune scanline strength, mask, bloom, and curvature one step at a time.
- Other systems: keep the original aspect ratio and use per-core or per-game presets when output resolution varies.

On a 120 Hz display, shader subframes can improve motion presentation without forcing global black-frame insertion. Black-frame insertion reduces brightness and can visibly flicker. Enable it only at the user's request and test comfort.

Verify dark scenes, bright gradients, scrolling motion, small text, performance, integer scaling, and menu readability. A preset loading without an error is not proof that it looks correct.

Useful public references:

- [Libretro input and controls](https://docs.libretro.com/guides/input-and-controls/)
- [Libretro configuration overrides](https://docs.libretro.com/guides/overrides/)
- [Libretro shaders](https://docs.libretro.com/guides/shaders/)
- [Retro Game Corps shader and overlay guide](https://retrogamecorps.com/2024/09/01/guide-shaders-and-overlays-on-retro-handhelds/)
- [Libretro CRT Beam Racing Simulator shader introduction](https://www.libretro.com/index.php/retroarch-first-program-to-support-blurbusters-crt-beam-racing-simulator-shader/)
