# Saves and native ports

Use this reference for save reconciliation, native decompilation ports, texture packs, and multi-screen mods.

## Save reconciliation

1. Inventory source and destination candidates with path, extension, byte size, modification time, and a hash where practical.
2. Group by game identity and emulator/core.
3. Account for region, serial, title ID, memory-card slot, and byte order.
4. Prefer native in-game saves over save states for migration.
5. Back up the destination before replacement.
6. Import one family at a time and prove progress in-game.
7. Preserve ambiguous or incompatible candidates in the backup.

Android scoped storage can hide app-owned paths from ADB. Use supported import/export flows and app-level proof instead of weakening permissions.

### RetroArch native saves

- Match the save to the exact content basename. RetroArch normally uses `.srm` for battery saves even when the source emulator used `.sav`.
- Inspect `savefile_directory` and `sort_savefiles_enable` in the active config. If sorting is enabled, use the exact core display-name directory; otherwise place the save in the configured root. Changing sorting is a deliberate migration choice, not a guess.
- When two ROM variants need the same source save, compare hashes first. Copy an identical save to both exact basenames only when the formats are compatible.
- Launch the game and verify recognizable in-game progress. File size and filename are not sufficient proof.

### Dolphin GameCube saves

- Read the active Slot A device setting before importing. Recent official Dolphin builds commonly default Slot A to a `GCI Folder`, but this is version-specific.
- With a GCI-folder card, the usual app-owned layout is `files/GC/<REGION>/Card A/`. Confirm the live path and region rather than assuming `USA`.
- Match the GCI header or filename title ID and region to the disc. Back up any existing destination, copy the `.gci`, verify its hash, then prove the expected slot in-game.
- With a raw memory-card device, use Dolphin's supported import flow instead of dropping a GCI beside the raw card.

## Native ports

- Confirm the project documents the user's lawful input requirements.
- Use only user-supplied ROMs, disc images, or extracted assets.
- Record upstream URL, commit or release, build variant, package ID, checksum, signer, and configuration changes.
- Keep replaceable assets separate from saves and user mods.
- Before an update, compare the installed and replacement signers. A signer mismatch makes uninstall and data loss a separate decision.
- Test controller input, aspect ratio, audio, save loading, suspend/resume, and launch from Cocoon.

## Multi-screen ports

- Stop unrelated external-display apps before testing so stale content cannot remain on another panel.
- Capture every panel and verify ownership visually.
- Confirm gameplay, HUD, map, inventory, touch targets, and aspect ratio on their intended screens.
- A process running on one screen does not prove the second screen belongs to the same app.

## Texture packs

Check title ID, region, directory name, emulator option, and pack version. File presence is insufficient: verify the emulator log or visible asset replacement proves the pack loaded.
