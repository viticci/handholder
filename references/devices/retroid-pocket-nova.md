# Retroid Pocket Nova profile

Use this profile only after live properties identify a Retroid Pocket Nova. It is a single-screen Android handheld built around a native 4:3, 120 Hz AMOLED panel.

## First-boot and system baseline

- Prefer the normal Android launcher during setup; set Cocoon as the home experience only after emulator launch paths work.
- Apply system updates before sideloading apps.
- Verify the Smooth Display quick-settings tile and the active display mode. The panel can remain at 60 Hz even when 120 Hz is the default mode; use 120 Hz when the user requests the guide-recommended setting or motion features such as black-frame insertion.
- A 30-minute screen timeout is useful during long setup and scraping sessions. Do not disable the screen lock or device security.
- Set force-landscape for console use if it does not break required portrait apps.
- Use Standard performance with Smart fan mode as a balanced default. Standard or low performance is enough for older systems; raise performance per game for GameCube or PlayStation 2 when needed.
- The built-in controller can use Nintendo-style or Xbox-style system navigation. Record the choice and map emulators consistently. Switching the quick-settings tile briefly disconnects the controller; wait for it to return and probe inputs again because its reported device name changes.
- Do not infer the RetroArch reservation name from the product name. A Nova in Xbox mode can identify itself to RetroArch with a different Retroid model label. Press one real built-in control, read RetroArch's connection message, and reserve that exact live name for player 1.
- M1 and M2 are useful as emulator hotkeys. Leave them as distinct buttons until mappings are tested.
- Optional battery-health settings include an 80 percent charge cap and slower charging. Do not change them without the user's preference.

## Storage

The device supports internal and removable storage. Follow the user's choice. For internal storage, use a simple root such as `/storage/emulated/0/ROMs` with one plainly named subfolder per platform and a separate BIOS directory when required. Check capacity before copying disc-based libraries.

## Display and graphics

- Preserve native 4:3 for GB, GBC, GBA, SNES, PS1, N64, GameCube, and most PS2 content.
- PSP remains 16:9 and should letterbox.
- AMOLED saturation is subjective. Do not install a third-party saturation tool or change global color without a user request and before/after verification.
- RetroArch Vulkan Slang shaders work well on the panel. Suitable starting points from public setup guides include LCD-grid styles for GB/GBC, LCD or GBA color-correction styles for GBA, and a restrained CRT preset for 4:3 TV systems.
- Black-frame insertion at 120 Hz is optional. It lowers brightness and visible flicker bothers some users; demonstrate it rather than enabling it silently.

## Emulator starting points

- RetroArch: GB/GBC, GBA, SNES, PS1, and N64 when the selected cores pass testing.
- Official Dolphin: GameCube. Start at 2x internal resolution and use per-game renderer changes.
- PPSSPP: PSP, with original aspect ratio.
- PlayStation 2: research the current ARM64 options. ARMSX2 is an open-source starting point when its current Android release supports the device; retain a community-patched fallback only when provenance and signer are understood.

Do not install Wii, DS, or 3DS components when those platforms are excluded.

## Guide-derived tips to verify live

Two 2026 setup guides emphasized: skip the vendor's bulk preinstall list in favor of current official releases; use a frontend only after direct emulator setup; configure ROM and BIOS roots before scraping; save RetroArch overrides at the correct scope; and use per-game settings for GameCube and PlayStation 2 instead of aggressive global hacks. Treat exact versions and third-party driver recommendations from videos as dated observations.
