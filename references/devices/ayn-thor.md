# AYN Thor profile

Use this profile only after live properties identify an AYN Thor. It is a dual-screen Android handheld; all IDs below must be discovered, not copied from an earlier device.

## Device-specific checks

- Enumerate both physical displays and their logical input displays.
- Capture both panels after every layout change.
- Find the built-in controller by its reported name; do not assume an input event number.
- Cocoon can place its grid and selected-item detail on different panels and can swap them.
- Stop unrelated dual-screen apps before validating a port.

## Proven app families

These projects have been used on Thor and require fresh release and lawful-input checks:

- Cocoon
- Dusklight
- Gen1Recomp and its separate Kanto-oriented fork
- Zelda3
- Project Picori
- Super Metroid Android ports
- Azahar-hosted Super Mario 64 3DS builds
- GameNative

Keep official and forked packages independent. Back up each data root separately.

Package IDs are useful discovery anchors, not current-release guarantees:

| App family | Observed package ID |
|---|---|
| Cocoon | `rip.moth.cocoonshell` |
| Dusklight | `dev.twilitrealm.dusk` |
| Gen1Recomp official | `com.theboisclub.pokemonred` |
| Gen1Recomp Kanto-oriented fork | `io.github.averageconsumer.gen1recomp.androidtest` |
| Zelda3 | `com.dishii.zelda3` |
| Project Picori | `dev.picori.tmc` |
| Super Metroid | `com.raekwon.supermetroid` |
| Azahar | `org.azahar_emu.azahar` |
| GameNative | `app.gamenative` |

## Dual-screen proof standard

For every dual-screen app or mod:

1. Stop unrelated external-display apps.
2. Capture both physical panels before launch.
3. Launch from Cocoon and capture both panels again.
4. Confirm both surfaces belong to the same foreground app.
5. Verify top-screen gameplay and the intended lower-screen HUD, map, inventory, or touch UI.
6. Test controls, audio, aspect ratio, suspend, resume, exit, and relaunch from Cocoon.

A live process or one correct panel is not sufficient evidence.

## Port-specific recovery clues

- Dusklight: match the lawful disc region, save region, and texture-pack title ID. Prove textures through visible replacement or logs, not file presence. A correct dual-screen layout shows gameplay above and HUD, map, or items below.
- Project Picori: a blank or broken lower panel can come from incomplete dual-screen assets or configuration. Restore the documented port assets before treating it as a hardware fault.
- Super Mario 64 3DS Ultimate in Azahar: `n3ds_wide_mode = 0` corrected a stretched or zoomed upper screen in one tested build. Stop stale external-display activities before judging the lower panel.
- Gen1Recomp: the official launcher and Kanto-oriented fork are separate packages with separate data. In `0.1.79`, Gold's nested options could disagree with the launcher's flat touch-control option, and raw Generation 2 `.sav` import was unsupported. Preserve saves and recheck newer releases rather than forcing conversion.
- GameNative: keep it as a separate home or dock shortcut when requested; do not bury it inside a native-mod folder unless the user asks.

## Known historical pitfalls

- Physical display IDs, logical input display IDs, and controller event paths changed across connections.
- A broken lower panel in a native port was caused by the port's configuration/assets, not the hardware.
- A stale external-display activity once showed one game on the top panel and another on the bottom.
- Gen1Recomp Gold support did not accept a raw Generation 2 save in version `0.1.79`; preserve the file and recheck newer releases.
- A public Generation 1 voxel mod did not support Gold when tested. Do not infer compatibility from screenshots or a headline.
- Super Mario 64 3DS Ultimate froze at its title screen in an older Azahar test. Recheck the current upstream issue and build before claiming it works.
- Cocoon Edit Grid used A to pick up and drop tiles; Y changed size.
