from talon import Module, settings

mod = Module()

mod.tag(
    "rango_direct_clicking",
    desc="Tag for enabling direct clicking in Rango",
)
mod.tag(
    "rango_exclude_singles",
    desc="Tag for excluding hints that contain only one letter",
)
mod.tag(
    "rango_number_hints",
    desc="Tag for enabling using numbers for hints in Rango",
)
