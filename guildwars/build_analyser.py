# click_schedule_plotter.py

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


class ClickSchedulePlotter:
    def __init__(
        self,
        cast_color="orange",
        rest_color="grey",
        req_cmap=cm.tab10,
        fig_size=(12, 6)
    ):
        """
        cast_color: färg för cast time
        rest_color: färg för rest time
        req_cmap: colormap för effect_time baserat på req
        """
        self.cast_color = cast_color
        self.rest_color = rest_color
        self.req_cmap = req_cmap
        self.fig_size = fig_size

    def plot_schedule(self, click_schedule, sim_time=120, title="Knapptryck med tider"):
        """
        click_schedule: lista av dicts med:
            key, interval, effect_time, rest_time, cast_time, cost, priority, offset, init, doonce, req
        """
        fig, ax = plt.subplots(figsize=self.fig_size)

        # Assign a color to each unique req
        unique_reqs = sorted(set(item["req"] for item in click_schedule))
        req_color_map = {req: self.req_cmap(i / max(1, len(unique_reqs) - 1))
                         for i, req in enumerate(unique_reqs)}

        for i, item in enumerate(click_schedule):
            t = item["offset"]
            first = True
            while t <= sim_time:
                if not first or item["init"]:
                    # Cast time
                    if item["cast_time"] > 0:
                        ax.broken_barh(
                            [(t, item["cast_time"])],
                            (i - 0.4, 0.8),
                            facecolors=self.cast_color,
                        )
                        start_effect = t + item["cast_time"]
                    else:
                        start_effect = t

                    # Effect time (color by req)
                    if item["effect_time"] > 0:
                        ax.broken_barh(
                            [(start_effect, item["effect_time"])],
                            (i - 0.4, 0.8),
                            facecolors=req_color_map[item["req"]],
                            alpha=0.8,
                        )

                    # Rest time 
                    if item["rest_time"] > 0:
                        rest_start = t + item["cast_time"]
                        ax.broken_barh(
                            [(rest_start, item["rest_time"])],
                            (i - 0.4, 0.8),
                            facecolors=self.rest_color,
                            alpha=0.5,
                        )

                    # Interval marker
                    ax.plot(t, i, marker="v", color="black", markersize=6)

                if item["doonce"]:
                    break
                t += item["interval"]
                first = False

        # Y-axis labels
        ax.set_yticks(range(len(click_schedule)))
        ax.set_yticklabels([item["key"] for item in click_schedule])

        ax.set_xlabel("Tid (sekunder)")
        ax.set_ylabel("Ability (key)")
        ax.set_title(title)

        # Legends
        legend_handles = [
            plt.Line2D([0], [0], color=self.cast_color, lw=6, label="Cast Time"),
            plt.Line2D([0], [0], color=self.rest_color, lw=6, label="Rest Time"),
        ]
        # Add effect_time legends per req
        for req, color in req_color_map.items():
            legend_handles.append(
                plt.Line2D([0], [0], color=color, lw=6, label=f"Effect Time (req {req})")
            )
        ax.legend(handles=legend_handles, loc="upper right")

        ax.grid(True, axis="x", linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()
