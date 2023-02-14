import pixray_module

pixray_module.run("pandas made of shiny metal")

pixray_module.run("pandas made of molten lava", outdir="outputs/fireout")

pixray_module.run("that's one content panda #pixelart", "pixel", outdir="outputs/pixel", )

pixray_module.run("an extremely hairy panda bear", "vdiff", custom_loss="aesthetic", outdir="outputs/hairout")

pixray_module.run("the ghost of a panda bear that died long ago", outdir="outputs/death", custom_loss="aesthetic")
