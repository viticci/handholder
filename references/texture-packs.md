# Replacement texture packs

Use this reference for user-created high-resolution or alternate texture packs. A copied folder is not an installed pack. Prove that the emulator loads the replacement assets in gameplay.

## Confirm compatibility and provenance

1. Identify the exact game title ID, serial, region, revision, emulator, renderer, and pack format from live state.
2. Prefer the pack author's project page or another source with clear provenance, version history, installation notes, and license terms.
3. Record the source URL, pack version, archive checksum, expected directory name, and emulator option it requires.
4. Do not download commercial game data, extracted original assets, BIOS data, or keys. Use only lawful user-created replacements and user-supplied game backups.

## Inspect before copying

- Measure the archive and extracted file count and size. Preserve a user-appropriate free-space reserve.
- List archive contents before extraction. Reject absolute paths, parent traversal, unexpected symbolic links, executables that are not required, and metadata-only clutter.
- Extract to staging. Keep the downloaded archive and source pack unchanged until launch testing passes.
- Confirm the images and compression format are supported by the installed Android emulator and renderer.
- Back up an existing pack with the same destination identity before replacement.

## Emulator-specific checks

### Dolphin

- Match the game ID and documented custom-texture layout.
- Enable custom texture loading only for the intended game or configuration scope. Texture prefetch can consume substantial memory; test before enabling it.
- A pack can work on desktop and still render incorrectly in an Android renderer. If visible corruption is isolated to one DDS encoding, convert a staged copy to a supported lossless image format, count conversion failures, and test again. Do not rewrite the source pack or assume all DDS files are bad.
- Keep widescreen hacks separate from texture replacement. Do not enable a global widescreen hack to make a pack fit.

Reference: [Dolphin resource packs](https://github.com/dolphin-emu/dolphin/blob/master/docs/ResourcePacks.md)

### PPSSPP

- Root the pack at the exact game ID expected by PPSSPP.
- Prefer PPSSPP's supported in-app archive import when the pack follows its documented layout.
- Enable texture replacement and confirm the active renderer supports the pack.
- Check for region-specific IDs and pack configuration files before copying one pack across variants.

Reference: [Using PPSSPP texture replacement packs](https://dev.ppsspp.org/docs/reference/use-texture-replacement/)

### Mupen64Plus and GLideN64

- Confirm that the selected core, renderer, and build support the pack type and high-resolution texture option.
- Discover the active cache and texture directories live. HTC, HTS, and other cached packs can be large and renderer-specific.
- If controls or hotkeys fail only in this core, treat that as a separate core-input issue; do not change texture paths to fix it.

Reference: [Libretro Mupen64Plus-Next](https://docs.libretro.com/library/mupen64plus/)

### PlayStation and PlayStation 2

- Verify that the active emulator or core supports replacement textures in its installed build.
- Do not switch emulators, change BIOS data, or widen the task merely to make a pack compatible.
- Skip a pack when the active emulator cannot load it safely or the result cannot be launch-tested.

## Prove the pack loaded

For each pack:

1. Launch a known scene with visible replacements.
2. Inspect emulator logs for actual replacement loads or errors.
3. Compare a screenshot with the pack disabled and enabled when the difference is not obvious.
4. Check for missing, black, transparent, scrambled, or over-sharpened textures.
5. Test interactive gameplay, frame pacing, memory pressure, suspend/resume, and a clean relaunch from the frontend.
6. Record pass, partial pass, failure, or not testable. Do not report installation as success without load proof.

When many packs are requested, install and test them in small batches. Stop before the storage reserve is crossed. Roll back only the exact failed pack and preserve the diagnostic log.
