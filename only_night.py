# Ported by brostos to api 8
# Tool used to make porting easier.(https://github.com/bombsquad-community/baport)
"""Only Night."""

# ba_meta require api 9

from __future__ import annotations

from typing import TYPE_CHECKING

import babase
import bascenev1 as bs
from bascenev1._gameactivity import GameActivity

if TYPE_CHECKING:
    pass


# ba_meta export babase.Plugin
class OnlyNight(babase.Plugin):
    GameActivity.old_on_transition_in = GameActivity.on_transition_in

    def new_on_transition_in(self) -> None:
        self.old_on_transition_in()
        gnode = bs.getactivity().globalsnode
        if self.map.getname() in [
            "Monkey Face",
            "Rampage",
            "Roundabout",
            "Step Right Up",
            "Tip Top",
            "Zigzag",
            "The Pad",
        ]:
            gnode.tint = (1.3, 1.2, 1.0)
        gnode.ambient_color = (1.3, 1.2, 1.0)
        gnode.vignette_outer = (0.57, 0.57, 0.57)
        gnode.vignette_inner = (0.9, 0.9, 0.9)
        gnode.vr_camera_offset = (0, -0.8, -1.1)
        gnode.vr_near_clip = 0.5
        cols = [(0.10, 0.3, 0.5), (0.6, 0.3, 0.6), (0.6, 0.3, 0.1),
                (0.2, 0.4, 0.1), (0.4, 0.3, 0.7), (0.10, 0.3, 0.5)]
        elif self.map.getname() in [
            "Big G",
            "Bridgit",
            "Courtyard",
            "Crag Castle",
            "Doom Shroom",
            "Football Stadium",
            "Happy Thoughts",
            "Hockey Stadium",
        ]:
            gnode.tint = gnode.tint = (1.3, 1.2, 1.0)
        gnode.ambient_color = (1.3, 1.2, 1.0)
        gnode.vignette_outer = (0.57, 0.57, 0.57)
        gnode.vignette_inner = (0.9, 0.9, 0.9)
        gnode.vr_camera_offset = (0, -0.8, -1.1)
        gnode.vr_near_clip = 0.5
        cols = [(0.10, 0.3, 0.5), (0.6, 0.3, 0.6), (0.6, 0.3, 0.1),
                (0.2, 0.4, 0.1), (0.4, 0.3, 0.7), (0.10, 0.3, 0.5)]
        else:
            gnode.tint = gnode.tint = (1.3, 1.2, 1.0)
        gnode.ambient_color = (1.3, 1.2, 1.0)
        gnode.vignette_outer = (0.57, 0.57, 0.57)
        gnode.vignette_inner = (0.9, 0.9, 0.9)
        gnode.vr_camera_offset = (0, -0.8, -1.1)
        gnode.vr_near_clip = 0.5
        cols = [(0.10, 0.3, 0.5), (0.6, 0.3, 0.6), (0.6, 0.3, 0.1),
                (0.2, 0.4, 0.1), (0.4, 0.3, 0.7), (0.10, 0.3, 0.5)]

    GameActivity.on_transition_in = new_on_transition_in
